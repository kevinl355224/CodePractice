#用matplotlib 產生兩張圖，並一起顯示
import matplotlib.pylab as plt
import numpy as np

def f(t):   #使用函數做遞減的運算
    return np.cos(2*np.pi*t)*np.exp(-t)


#設定兩個數列
t1 = np.arange(0.0,5.0,0.1)              #設定一個0~5間隔為0.1的數列
t2 = np.arange(0.0,5.0,0.02)             #設定一個0~5間隔為0.2的數列

plt.subplot(2,1,1)                       #建立一個包含兩行一列的圖，並把目前繪製焦點放在第一張子圖
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')     #第一張圖有兩個x軸數值(t1,t2),兩個y的值(f(t1),f(t2))
                                         #第一組的'bo'是藍色點圖，'k'是黑線

plt.subplot(2,1,2)                       #建立一個包含兩行一列的圖，並把目前繪製焦點放在第一張子圖
plt.plot(t2,np.cos(2*np.pi*t2),'r--')    #第二張圖只有一個x軸數值t2，一個y軸數值np.cos(2*np.pi*t2)
                                         #'r--'是紅色虛線
plt.show()      #秀出全部圖片