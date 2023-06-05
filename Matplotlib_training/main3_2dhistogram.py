#2d的直方圖練習
import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.random.standard_normal(n)                                    #產生1萬個,均值0，標準差1的隨機數
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)              #產生1萬個y隨機數


# np.linspace(-4, 4, 42) linspace函式在 -4 到 4 之間產生等距的42個數字
# 譬如 np.linspace(0,10,5) print -> [ 0. 2.5 5. 7.5 10.] 五個數字
xedges, yedges = np.linspace(-4, 4, 42), np.linspace(-25, 25, 42)   

# np.histogram2d(x, y, (xedges, yedges)) 產生2d直方圖
# x,y 一維中的數據，上面x,y各有一萬個
# bin = (xedges, yedges) 指定直方圖的邊界
hist, xedges, yedges = np.histogram2d(x, y, (xedges, yedges))

# np.clip(a,a_min,a_max) 接受一組數列 a ,限制範圍在 a_min,a_max
# 譬如   
# a = np.array([1, 2, 3, 4, 5])
# a_clipped = np.clip(a, 2, 4) 
# print(a_clipped) ====> [ 2 2 3 4 4 ] 1比2小變成1，5比4大變成4

# np.digitize(x,xedges)
# 譬如    
# x = np.array([1, 3, 5, 2, 4])
# xedges = np.array([2, 4])
# indices = np.digitize(x, xedges) =====> [0,1,2,0,1]
# 因為 xedges 有兩個數字，因此三個箱子
#       箱子0   <= 第一個數字(2)
#                  第一個數字(2)  <   箱子1   <= 第二個數字(4)
#                                            <  第二個數字(4)      箱子2
#所以np.digitize(x,xedges) 將一萬個標準差1的數字分到 -4 ~ 4 之間 42個範圍 並將範圍限制在 0 ~ 42 之間

xidx = np.clip(np.digitize(x, xedges), 0, hist.shape[0]-1)
yidx = np.clip(np.digitize(y, yedges), 0, hist.shape[1]-1)
c = hist[xidx, yidx]      #二維數值


# 在x,y一維空間，帶入數量c的二維數值
plt.subplot(2,2,1)
plt.scatter(x, y,c=c)  

# y 數量一維圖
plt.subplot(2,2,2)    
# 將 x 顛倒
plt.gca().invert_xaxis()
# 將y標籤移到右邊
plt.tick_params(axis='y', labelleft=False, labelright=True, left=False, right=True)
# 更改水平方向，以實現 90 度旋轉
plt.hist(y,orientation= "horizontal",bins=100) 

# x數量一維圖
plt.subplot(2,2,3)
plt.hist(x,bins = 100)
plt.show()