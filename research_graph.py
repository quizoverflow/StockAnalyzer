import pandas as pd
from  matplotlib import pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from datetime import datetime
from pykrx import stock
import numpy as np



def make_dataframe(term,pp,plist):
    if pp == 1:
        st_df =pd.DataFrame(
        {'time':[x for x in range(len(plist[-1*term:-1]))],
        'delta' : plist[-1*term:-1]
        }
        )
        return st_df
    else:
        st_df =pd.DataFrame(
        {'time':[x for x in range(len(plist[-1*term:-1]))],
        'delta' : plist[-1*term:-1]
        }
        )
        return st_df

def get_priceGraph(term,num,dataframe):
    global future_list
    plt.rcParams["figure.figsize"] = (12, 6)
    sns.regplot(x='time', y='delta', data=dataframe)   
    plt.xlim(dataframe['time'].min()-1, dataframe['time'].max()+term//5)
    plt.grid()
    plt.savefig(f"graph {num}.png",edgecolor="blue",facecolor = "white",format='png',dpi=200)
    z=np.polyfit(dataframe['time'][-term:-1], dataframe['delta'][-term:-1], 1) # 기울기와 절편 확인   ... 30 거래일 기준
    f=np.poly1d(z) # f(x): f함수에 x값을 넣으면 y값을 계산해 줌
    future_price = f(dataframe['time']+(term//5))[0]
    future_list.append(future_price)
    return f"추세선 기울기 ={z}\n향후 {term/5}일 후 예상 수치 = {future_price}"



def get_perGraph(term,num,dataframe):
    plt.rcParams["figure.figsize"] = (12, 6)
    sns.regplot(x='time', y='delta', data=dataframe)   
    plt.xlim(dataframe['time'].min()-1, dataframe['time'].max()+term//5)
    plt.grid()
    plt.savefig(f"graph {num}.png",edgecolor="blue",facecolor = "white",format='png',dpi=200)

    z=np.polyfit(dataframe['time'][-term:-1], dataframe['delta'][-term:-1], 1) # 기울기와 절편 확인   ... 30 거래일 기준
    f=np.poly1d(z) # f(x): f함수에 x값을 넣으면 y값을 계산해 줌
    return f"추세선 기울기 ={z}\n향후 {term/5}일 후 예상 수치 = {f(dataframe['time']+(term//5))[0]}"

def draw_all_graph(code):
    global future_list
    future_list = []
    #데이터 불러오기
    now = datetime.now()
    today_date = str(now.date())
    today_date = today_date[0:4] + today_date[5:7] +today_date[8:10]

    perdata = stock.get_market_fundamental_by_date("20150101",today_date,code)
    per_dict = perdata["PER"].to_dict()
    per_list = list(per_dict.values())

    pricedata = stock.get_market_ohlcv_by_date("20150101",today_date,code)

    price_dict = pricedata["종가"].to_dict()
    price_list = list(price_dict.values())

    a = get_perGraph(30,1,make_dataframe(30,0,per_list))
    b = get_priceGraph(30,2,make_dataframe(30,0,price_list))
    c = get_priceGraph(60,3,make_dataframe(90,0,price_list))
    d = get_priceGraph(270,4,make_dataframe(270,0,price_list))
    regression = [a,b,c,d,future_list]
    return regression




"""  
z=np.polyfit(st_df['time'][-10:-1], st_df['delta'][-10:-1], 1) # 기울기와 절편 확인   ... 30 거래일 기준
f=np.poly1d(z) # f(x): f함수에 x값을 넣으면 y값을 계산해 줌
print(z[0], z[1])
print(f(1))

#statsmodel을 통해 회귀식의 회귀계수(기울기, 절편) 확인
print(ols('delta ~ time', data=st_df).fit().summary())


 """

