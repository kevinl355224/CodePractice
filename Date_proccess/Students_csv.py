#使用 csv 函試庫 讀取 處理 並輸出 csv 檔案
#要注意，可以使用for迴圈，將list 由 writerow 函式 一行一行寫入
#不用像pandas要使用 series將資料整理，再用 _append 傳入新的 pd(類別) 

import csv

result = []

dept = {
    "66": "資訊管理系",
    "56": "應用外語系",
    "46": "多媒體設計系",
    "36": "會計資訊系",
    "26": "企業管理系",
    "16": "資訊工程系",
}

city = {
    "A": "台北市",
    "B": "台中市",
    "C": "基隆市",
    "D": "台南市",
    "E": "高雄市",
    "F": "新北市",
    "G": "宜蘭縣",
    "H": "桃園市",
    "I": "嘉義市",
    "L": "台中縣",
    "J": "新竹縣",
    "K": "苗栗縣",
    "M": "南投縣",
    "N": "彰化縣",
    "O": "新竹市",
    "P": "雲林縣",
    "Q": "嘉義縣",
    "T": "屏東縣",
    "U": "花蓮縣",
    "V": "台東縣",
    "W": "金門縣",
    "X": "澎湖縣",
    "Z": "連江縣",
}


# 開啟 CSV 檔案
with open("QUIZ/0531/st_info.csv", newline="", encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    index = 0
    # 以迴圈輸出每一列
    for row in rows:
        if index == 0:
            index += 1
            continue
        sex = ""
        if row[0][1] == "1":
            sex = "男"
        elif row[0][1] == "2":
            sex = "女"
        result.append(
            [
                row[0],
                row[1],
                row[2][0] + "O" + row[2][2],
                dept[row[1][3:5]],
                sex,
                city[row[0][0]]
            ]
        )
        index += 1
#print(type(result[0]))

with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)
  #for迴圈外新增一行column
  writer.writerow(['身分證','學號','姓名','科系', '性別', '居住地'])
  for r in result:
    writer.writerow(r)