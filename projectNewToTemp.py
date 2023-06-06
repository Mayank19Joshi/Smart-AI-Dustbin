print('projectNewToTemp.py BEGIN')
import time
import os
import shutil
from openpyxl import load_workbook
import easyocr



# Load the EasyOCR model
reader = easyocr.Reader(['en'])

# Define a function to extract text from an image
def textFromImage(imagePath):
    image = os.path.abspath(imagePath)
    result = reader.readtext(image)
    text = ""
    for r in result:
        text += r[1] + " "
    #print("The text is ",text)
    #input()
    return text

path = os.getcwd()+"\\images_project_cam"
i = 0
id = 0

def process(path, j):
    global id
    print(path)
    newpath = path+"\\Temp\\"+str(id)+".jpeg"
    shutil.move(path+ "\\New\\"+j, newpath)
    resultText = textFromImage(newpath)
    #delete top
    #print("result text is ",resultText)
    #input()
    #exit(1)
    #delete bottom
    print('Initialized second column')    
    print('Calling data id to spread Sheet')
    sheetpath = path+"\\projectData.xlsx"
    wb = load_workbook(filename=sheetpath)
    sht = wb.active
    sht["A"+str(id+2)] = str(id)
    sht["B"+str(id+2)] = resultText #done by text recognition program
    sht["C"+str(id+2)] = "Unknown"
    wb.save(sheetpath)
    print('Added data')
    
    print('Calling ProjectMailSystemCheck.py')
    #delete top
    #resultText = "Kurkure"
    #delete bottom
    os.system('python ProjectMailSystemCheck.py '+newpath+' '+resultText)
    print('Returned from ProjectMailSystemCheck.py')
    id = id+1
#for infinite loop; fooling interpreter by reassigning i to 0 when i reaches 100
while(i<100):
    i=i+1
    if i == 100:
        i = 0
    time.sleep(1)
    try:
        direcs = os.listdir(path+"\\New")
        if(len(direcs) != 0):
            for j in direcs:
                process(path,j)
        else:
            print(direcs)
    except Exception as e:
        print(e)
print('projectNewToTemp.py END')
