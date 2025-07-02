from django.shortcuts import render
from Func import image_to_text_ocr
from filemanager.models import OCRHistory

def home(request):
    if request.method=='POST':
        image = request.FILES.get('image_file')
        print(image)
        ocr = image_to_text_ocr.image_to_string(image)
        if ocr['status'] == True:
            try:
                ocr_history = OCRHistory(image=image) 
                ocr_history.file.save(ocr['file'].name, ocr['file']) 
                ocr_history.save()
                data = {
                    'msg':'OCR Completed',
                    'file':ocr_history.file.url
                }
                return render(request,'index.html',data)
            except Exception as e:
                print(e)
                data = {
                'msg':'Something went wrong!!'
                }
                return render(request,'index.html',data)
        else:
            data = {
                'msg':'Failed to upload!'
            }
            return render(request,'index.html',data)

    return render(request,'index.html')