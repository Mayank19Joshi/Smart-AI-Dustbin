print('projectCreateFolders.py BEGIN')
import os
import getpass
path=os.getcwd()
#path = "C:\\Users\\"+getpass.getuser()+"\\desktop"
def InitializeFolders(path):
    try:
        os.mkdir(path+"\\images_project_cam")
    except Exception as e:
        pass
    finally:
        
        print("images_project_cam folder created on desktop")
        path = path+"\\images_project_cam"
        print(path)

    try:
        os.mkdir(path+"\\New")
    except Exception as e:
        pass
    finally:
        print("New folder created in images_project_cam")
    try:
        os.mkdir(path+"\\Dry")
    except Exception as e:
        pass
    finally:
        print("Dry folder created in images_project_cam")
    try:
        os.mkdir(path+"\\Temp")
    except Exception as e:
        pass
    finally:
        print("Temp folder created in images_project_cam")
    try:
        os.mkdir(path+"\\Wet")
    except Exception as e:
        pass
    finally:
        print("Wet folder created in images_project_cam")
    try:
        os.mkdir(path+"\\Recommend")
    except Exception as e:
        pass
    finally:
        print("Recommend folder created in images_project_cam")
InitializeFolders(path)
print('projectCreateFolders.py END')
