import os
from pathlib import Path
from datetime import datetime


# 創建檔案
def makeFile(fileName):
    print("---------------", fileName)
    file_path = Path(fileName)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(fileName):
        Path(f"{fileName}").touch()
# 把資料寫入檔案中
def writeFile(fileName, text):
    f = open(fileName, 'a', encoding="UTF-8")
    f.write(text)
    f.close()
# 刪除單一file
def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

# 建立檔案的method (在這裡新增單一的makeFile)
def createCollection(fileList):
    #創建中午班、下午班、醫療、請假 等 txt 檔案
    now = datetime.now()
    current = str(now.strftime("%Y-%m-%d %H:%M"))
    for file in fileList:
        makeFile(f'./records/{file}')
        writeFile(f'./records/{file}', "【檔案建立時間: " + current + "】\n\n")
# 刪除之前匯出的所有txt file
def deleteCollection(fileList):
    for file in fileList:
        deleteFile(f'./records/{file}')

def classifyRecords(tempString):
    print("tempString = " + tempString)

    for i in range(len(tempString)):
        if tempString[i:i+2] == "請假":
            writeFile("./records/personal_leave.txt", tempString+"\n------------\n")
            break
        if tempString[i:i+2] == "醫療":
            writeFile("./records/medical_treatment.txt", tempString+"\n------------\n")
            break
        if tempString[i:i+2] == "醫院":
            writeFile("./records/medical_treatment.txt", tempString+"\n------------\n")
            break
        if tempString[i:i+2] == "中午":
            writeFile("./records/noon.txt", tempString+"\n------------\n")
            break        
        if tempString[i:i+2] == "下午":
            writeFile("./records/afternoon.txt", tempString+"\n------------\n")
            break
        if tempString[i:i+2] == "環校":
            writeFile("./records/night.txt", tempString+"\n------------\n")
            break
        if i == len(tempString)-1:
            writeFile("./records/other.txt", tempString+"\n-------------\n")
    tempString = ""