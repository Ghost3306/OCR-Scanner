import cv2
import pytesseract
import numpy as np
import os
from datetime import datetime
from django.core.files.base import ContentFile
datafile = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def image_to_string(image):
    # image = cv2.imread(r"present.j    pg")
    try:
        file_bytes = image.read()  
        np_arr = np.frombuffer(file_bytes,np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        data = pytesseract.image_to_string(image_rgb)

        ocr_data = pytesseract.image_to_data(image_rgb,output_type=pytesseract.Output.DICT)
        # print(type(ocr_data))
        #print(ocr_data)
        n_boxes = len(ocr_data['text'])



        lines = {}
        for i in range(n_boxes):
            if int(ocr_data['conf'][i]) > 0: 
                block_num = ocr_data['block_num'][i]
                line_num = ocr_data['line_num'][i]
                key = (block_num, line_num)
                if key not in lines:
                    lines[key] = []
                lines[key].append(ocr_data['text'][i])
            
        # Print lines
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join('Func', 'DataFiles')  
        os.makedirs(folder_path, exist_ok=True)  
        file_path = os.path.join(folder_path, f"{timestamp}.txt")
        
        extracted_text = ""
        with open(file_path, "w", encoding='utf-8') as f:
            for key in sorted(lines.keys()):
                line_text = ' '.join(word for word in lines[key] if word.strip() != '')
                f.write(line_text + "\n")
                extracted_text +=line_text + "\n"
        txt_filename = f"{timestamp}.txt"
        txt_content = ContentFile(extracted_text)
        txt_content.name = txt_filename  
        return {
            'status':True,
            'file':txt_content
        }
    except Exception as e:
        print(e)
