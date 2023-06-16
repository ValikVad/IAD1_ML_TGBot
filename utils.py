import logging
from PIL import Image
import cv2
from matplotlib import pyplot as plt
import numpy as np

from paddleocr import PaddleOCR
import pytesseract




from transformers import FSMTForConditionalGeneration, FSMTTokenizer



def text_translate(text, lang):
    print("translate\n")
    if (lang == "en"):
        mname = "facebook/wmt19-en-ru"
        tokenizer = FSMTTokenizer.from_pretrained(mname, max_new_tokens=1000)
        model = FSMTForConditionalGeneration.from_pretrained(mname)
    else:
        ru2en = "facebook/wmt19-ru-en"
        tokenizer = FSMTTokenizer.from_pretrained(ru2en, max_new_tokens=1000)
        model = FSMTForConditionalGeneration.from_pretrained(ru2en)
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(decoded)
    return(decoded)

def text_recognise(image, lang):
    print(lang)
    if (lang == "en"):
        eng_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=False)
        # print(image)
        result_ocr = eng_model.ocr(np.array(image))
        result_eng_text = str()
        for res in result_ocr[0]:
            result_eng_text += res[1][0]

        return result_eng_text
    else:
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to remove some noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        result = pytesseract.image_to_string(Image.fromarray(img),lang='rus')
        result = result.split("\n")

        result_str = str()
        for i in result:
            result_str += i + ' '
        # result_str = result_str.replace("\x0c"," ")
        # result_str = result_str.replace("\n"," ")
        # # result_str = "___"
        print(result_str)
        return result_str
