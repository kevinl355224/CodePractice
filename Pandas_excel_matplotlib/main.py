#嘗試使用Pandas導入旅遊資料，並整理出歷年旅遊人數比較，匯出成圖
#導入pandas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

from matplotlib.font_manager import FontProperties as font

font1 = font(fname="noto_sans_tc/NotoSansTC-Medium.otf")

def year_1(n,year_now): #辨認年別，並回傳True、False
    if  n == year_now:
        return True
    else :
        return False

df = pd.read_excel("歷年國內主要觀光遊憩據點遊客人數月別統計.xlsx") #讀取excel檔案

list_sum = []
list_date = []

#製作顏色標籤
color_list = plt.get_cmap('tab10')(range(10))

big_color_list = []
for n in color_list:
    [big_color_list.append(n) for i in range(12)]


labels = []
for n in range(10):
    [labels.append(str(i+1)+"\n月") for i  in range(12)]


First_year = 2012
end_year = 2022
sum = 0
year_now = First_year

while year_now < end_year:

    dY = df["年別"].apply(year_1,year_now=year_now) #判斷當年

    for m in range(12): #一年12個月
        sum = 0 #每月人數重製
        month = str(m+1)+"月"
        for n in df[month][dY].fillna(0):#合計當年某月全部
            sum += n
        list_date.append(str(year_now)+"年"+month)
        list_sum.append(sum)
    year_now+=1


for i, color in enumerate(color_list) :
    plt.plot((),(), color=color, label=f'20{i+11}')

plt.title("國內旅遊歷年人數",font = font1)
plt.bar(list_date,list_sum,color = big_color_list)


plt.xticks(list_date,labels=labels,fontproperties = font1,fontsize = 5)
plt.xlabel("年別",font=font1)
plt.ylabel("人\n數\n(億)",font=font1,rotation = 0,labelpad= 10)

plt.legend(loc='upper left')

plt.show()