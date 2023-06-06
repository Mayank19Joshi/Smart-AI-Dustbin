from openpyxl import Workbook
import os
path = os.getcwd()+"\\images_project_cam\\projectData.xlsx"
if(os.path.exists(path)):
    print("File already exists")
else:
    print('Creating file')
    wb = Workbook()
    sht = wb.active
    sht['A1'] = 'Image id'
    sht['B1'] = 'Name by File'
    sht['C1'] = 'Name by Client'
#    print(sht['F1']. value == None)
    wb.save(path)
    
