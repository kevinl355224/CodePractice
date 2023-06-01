#使用pandas讀取資料，並處理後，創建csv檔案

import pandas as pd
#新增import路徑 要找到函試庫所在位置
import sys
sys.path.append("C:\\Def_ID_process")
#import 身分證辨識函試庫
from ID_process import ID_Find_Loc

#建立科系dic
raw_D_data =""" '66':'資訊管理系'
'56':'應用外語系'
'46':'多媒體設計系'
'36':'會計資訊系'
'26':'企業管理系'
'16':'資訊工程系' """
Dept_dict = {}
Dept_list = raw_D_data.split()
x = Dept_list[0].split("'")[1]
for n in Dept_list:
    #將list由單引號'分割，再放入dict
    Dept_dict[n.split("'")[1]]=n.split("'")[3]
    
df = pd.read_csv("QUIZ/0531/st_info.csv",encoding="utf-8")
New_df = pd.DataFrame(columns=["身分證","學號","姓名","科系","性別","居住地"])

# pandas.values 轉為LIST[LIST]
df_list = df.values
for n in df_list:
    #ID身分證
    ID = n[0]
    #學號
    sdno = n[1]
    #姓名處理
    name = n[2][0]+"O"+n[2][1]
    #"科系"學號4~6碼是科系
    dept = Dept_dict[str(n[1])[3:5]]
    #性別 身分證第二碼 1男 2女 
    if n[0][1] == "1":
        sex = "男"
    else:
        sex = "女"
    #根據身分證回傳居住地
    Loc = ID_Find_Loc(n[0])
    info = pd.Series([ID,sdno,name,dept,sex,Loc],index=["身分證","學號","姓名","科系","性別","居住地"])
    #append series進DF //不知道為何要多個_
    New_df = New_df._append(info,ignore_index=True)

#創建CSV檔案
New_df.to_csv("studentsResult.csv",encoding="utf-8",index=False)