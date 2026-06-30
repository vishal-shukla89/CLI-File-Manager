from pathlib import Path
import os

#create a function which shows all file present in folder
def readfileAndfolder():
    path=Path('')
    # PRO TWEAK: Changed rglob to glob so it doesn't search the whole computer
    items=list(path.glob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")

#to create a function to read file operations
def createfile():
    try:
        readfileAndfolder()
        name=input("Enter the name of file you want to create :- ")
        p=Path(name)
        if not p.exists() :
            with open(p,'w') as fs:
                data=input("Enter the data you want to write inside file:- ")
                fs.write(data)
              
                print("File CREATED SUCCESSFULLY")
        else:
            print("File Already Exists !!!!")
    except Exception as err:
        print(f"An error occured as {err}")

#to create a function to read file operation 
def readfile():
    try:
        readfileAndfolder()
        name=input("Enter the file name you want to read :- ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                print(fs.read())
            print("File Readed SUCCESSFULLY !!!")
        else:
            print(" NO, such file Exists")
    except Exception as err:
        print(f"An error occured as {err}")

#to create a function to update file 
def updatefile():
    try:
        readfileAndfolder()
        name=input("Enter the name of file which you want to update :- ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 if you want to rename file ")
            print("press 2 if you want to overwrite the file ")
            print("press 3 if you want to append data inside file ")
            res=int(input("Enter your choice b/w 1 to 3 :- "))
            if res==1:
                name2=input("Enter the new name of file:- ")
                p2=Path(name2)
                p.rename(p2)
                print("File RENAMED SUCCESSFULLY !!!")
            if res==2:
                with open(p,'w') as fs:
                    data=input("Enter the Data whatyou want to overwrite inside file:- ")
                    fs.write(data)
                   
                    print("FILE OVERWRITTEN SUCCESSFULLY !!!!")
            if res==3:
                with open(p,'a') as fs:
                    data=input("Enter the Data whatyou want to append inside file:- ")
                    fs.write("\n"+data)
                    
                    print("DATA APPENDED SUCCESSFULLY !!!!")
        else:
            print("NO such file exists !!")
    except Exception as err:
        print(f"An error occured as {err}")

# to create a function to delete file op
def deletefile():
    try:
        readfileAndfolder()
        name=input("Enter the file name you want to delete:- ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETED SUCCESSFULLY !!!")
        else:
            print("NO such file exists !!!")
    except Exception as err:
        print(f"An error occured as {err}")


# PRO TWEAK: Added 'while True' loop so the app stays open. Added option 5 to break the loop.
while True:
    print("\nPress 1 to create a file")
    print("Press 2 to read a file")
    print("Press 3 to update a file")
    print("Press 4 to delete a file")
    print("Press 5 to EXIT")

    check=int(input("\nEnter your choice between 1 to 5 :- "))
    if check==1:
        createfile()
    elif check==2:
        readfile()
    elif check==3:
        updatefile()
    elif check==4:
        deletefile()
    elif check==5:
        print("Closing the File Manager.")
        break
