#IdTest( 身分證 )   判斷身分證是否合法 return 合法 / 不合法
#ID_Find_Loc( 身分證 ) return 縣市

raw_data = """A=10 B=11 C=12 D=13 E=14 F=15 G=16 H=17 I=34 J=18 K=19 L=20
M=21 N=22 O=35 P=23 Q=24 R=25 S=26 T=27 U=28 V=29 W=32 X=30
Y=31 Z=33"""
list_en_num = raw_data.split()
#創建對照字典
dict_en_num = {}
for n in list_en_num:
    dict_en_num[n[0]]=n[2:4]

raw_data2 = """A台北市 B台中市 C基隆市 D台南市 E高雄市 F台北縣
G宜蘭縣 H桃園縣 I嘉義市 J新竹縣 K苗栗縣 L台中縣
M南投縣 N彰化縣 O新竹市 P雲林縣 Q嘉義縣 R台南縣
S高雄縣 T屏東縣 U花蓮縣 V台東縣 W金門縣 X澎湖縣
Y陽明山 Z連江縣"""
list_num_loc = raw_data2.split()
dict_num_loc = {}
for n in list_num_loc:
    dict_num_loc[n[0]] = n[1:4]

def IdTest(ID):
    #由英文轉為數字，十位數加上個位數*9
    num1 = int(dict_en_num[ID[0]][0])+int(dict_en_num[ID[0]][1])*9
    num2 = 0
    for n in range(0,8):
        num2 = num2 + int(ID[n+1])*(8-n)
    num2+=int(ID[9])
    correct = (num1 + num2)%10
    #相加
    if correct == 0:
        return "合法"
    else:
        return "不合法"
    
def ID_Find_Loc(id)->str:
    return (dict_num_loc[id[0]])
