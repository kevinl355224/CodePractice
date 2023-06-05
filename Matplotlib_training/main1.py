#用簡單的輸入、輸出製作折線圖，並練習各個參數應用
import matplotlib.pyplot as plt #imort 繪圖套件
import matplotlib.font_manager as fm #import字體管理

#設定字體檔案位置
font_path = 'Fonts/SourceHanSansCNRegular.otf'
font = fm.FontProperties(fname=font_path)

#設置DATA
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

lables_d = ["第一年","第二年","第三年","第四年"]        #設置x軸想顯示的標籤
lables = []

plt.subplots_adjust(bottom=.15)

for n in lables_d :          #在字串中加入跳行，實現豎直文字
    lables.append('\n'.join(n))

#設定圖片格式
plt.title("人口成長趨勢圖",fontproperties = font)
plt.xlabel ("年份",fontproperties = font)
plt.ylabel("人\n口",fontproperties = font,rotation = 0,labelpad=10)     #lablepad讓標籤往左邊一點
plt.xticks(ticks = year,                                # x軸有哪些資料標籤 (list)
           labels  = lables,                            # x軸資料標籤想顯示的型態，必須與ticks數量一致(list)
           color = '#f00',                              # 字體顏色
           fontsize=10,                                 # 字體大小
           rotation = 15,                               # 字體旋轉程度
           fontproperties = font)                       # 字體格式

plt.plot(year,pop)  #圖片帶入x,y值
plt.show()          #顯示圖片