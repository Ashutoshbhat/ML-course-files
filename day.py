import matplotlib.pyplot as plt
import yfinance as yf
nifty50=yf.download('^NSEI',start ='2020-01-01',end='2024-05')
plt.plot(nifty50.index,)



x=[1,2,3,4,5,6,7,8,9,10]
y=[3,5,55,7,8,4,5,6,7,4]
y2=[12,34,56,67,89,45,32,12,1,3,]


plt.plot(x,y,linestyle ='-',color='red',marker='*',label='x vsy example')
plt.plot(x,y2,linestyle ='--',color='blue',marker='o',label='second label x vs y2')
plt.title("example of matplotlib lineplot")
plt.xlabel("example x values")
plt.ylabel("example y values")
plt.legend()


plt.show()