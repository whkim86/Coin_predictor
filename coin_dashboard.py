# streamlit run app.py
# cd C:\Users\woohy\Desktop\streamlit_fd\
# streamlit run dashboard.py

# git add -A
# git commit -m 'commit message'
# git push origin dashborad 


import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import matplotlib.dates as mdates
import numpy as np
import time
 



## 보이기 
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            GithubIcon {visibility: hidden;}
            #header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

## 숨기기 
# hide_streamlit_style = """
#             <style>
#             MainMenu {visibility: hidden;}
#             #footer {visibility: hidden;}
#             GithubIcon {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# 현재 날짜 가져오기
today = datetime.today()
# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")


st.title("비트코인 일(Day)예측 대시보드")
st.markdown(f'#### [비트코인, {formatted_date} 👈 예측결과 ] ')


st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')









# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_Day_v3.csv'
# 데이터 불러오기
data = pd.read_csv(data_url)
data3 = data[data['GRP'] == 'Set3'][['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]].dropna()

select_date = st.selectbox(
    '💡 예측날짜 선택 ',
    data3['pred_day'].sort_values(ascending=False).unique()
)


data3 = data3.rename(columns={'pred_day': '예측일'})
data3 = data3.rename(columns={'close_up': '종가상승확률'})
data3 = data3.rename(columns={'high_up': '고점갱신확률'})
data3 = data3.rename(columns={'low_up': '저점상승확률'})
# 💻 🧠 👋 👈
st.markdown(f'#### 💻 비트코인 예측일 :  {select_date} 👈 9시 기준, 예측결과 ')

data3_1 = data3[ (data3['coin'] == 'BTC')  & (data3['예측일']==select_date)  &  (data3['SEQ'] == 1)]

a = data3_1['종가상승확률'].unique()
b = data3_1['고점갱신확률'].unique()
c = data3_1['저점상승확률'].unique()
st.markdown(f'##### 👋 익일 종가 상승확률 : {a}  ')
st.markdown(f'##### 👋 익일 고점 상승확률 : {b}  ')
st.markdown(f'##### 👋 익일 저점 상승확률 : {c}  ')

st.markdown(f'######    ※ 확률 수치 참고  ')
st.markdown(f'######    상승확률 100 ~ 77% 인 경우 상승가능성 매우 높음  ')
st.markdown(f'######    상승확률 76 ~ 59% 인 경우 상승가능성 높음  ')
st.markdown(f'######    상승확률 58 ~ 40% 인 경우 중립  ')
st.markdown(f'######    상승확률 39 ~ 21% 인 경우 하락가능성 높음  ')
st.markdown(f'######    상승확률 20 ~ 0% 이상인 경우 하락가능성 매우 높음  ')


# 
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data3_1 = data3[ (data3['coin'].isin(select_multi_coin))  & (data3['예측일']==select_date)  &  (data3['SEQ'] >= min(seqs)) & (data3['SEQ'] <= max(seqs))]
st.markdown(f'### 3. 매수매도결정 , 예측날짜:  {formatted_date} 9시 기준')

data3_1.index = [''] * len(data3_1)

st.markdown(f'###### 예측일 :  {select_date}, 예측건수 : 1 ~ {max(seqs)} ')

st.write(data3_1[[ 'date','coin', 'SEQ', '종가상승확률','고점갱신확률','저점상승확률']])



# st.sidebar 를 통해 사이드바를 생성하고 내용을 넣을 수 있음.
# st.sidebar.text_input : 사이드바에 텍스트를 입력할 수 있는 요소를 만듦
# st.sidebar.date_input : 사이드바에 날짜를 입력할 수 있는 요소를 만듦

# c("Pred1", "Pred2","Pred6", "Pred7","Pred9", "Pred12","Pred15",
#                                  "Pred18","Pred21", "Pred24","Pred27", "Pred33","Pred34", "Pred37","Pred52")





data4 = data[data['GRP'] == 'Set4' ][['GRP', 'pred_day', 'coin', 'SEQ', 'date', 'variable', 'value_close', 'value_high', 'value_low', 'LOW_VL', 'HIGH_VL', 'CL_VL']]

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_coin = st.selectbox(
    '👈 Select Coin Symbols For #4',
    # data4['coin'].sort_values(ascending=True).unique()
    ['BTC'] + list(data1[(data1['예측일'] == select_date) ].sort_values(by='추천순서1', ascending=True).coin.unique())
)
# ['all'] + list(data_coin_a['coin'].sort_values(ascending=True).unique())

data4 = data4.rename(columns={'pred_day': '예측일'})
# (data4['coin'].isin(select_multi_coin)) |
data4_1 = data4[(  ( (data4['coin'] == select_coin) ) ) & (data4['예측일'] == select_date) ]

data4_2 = data3[ (data3['coin'] == select_coin)  & (data3['예측일'] == select_date)  &  (data3['SEQ'] <= 1) ][['예측일','coin','종가상승확률','고점갱신확률','저점상승확률']]





data4_1CLx = data4_1[data4_1['variable'] == 'Pred1'][['date']]
# data4_1CLx = ['2024-' + text[:5] for text in data4_1CLx.date ] 
data4_1CLx = list(range(1, len(data4_1CLx.date)+1)) 

# data4_1CLx = pd.to_datetime(data4_1CLx)


# ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
# ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)

data4_1CLy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_close']]

data4_1CLy = data4_1[data4_1['variable'] == 'Pred1'][['value_close']]

data4_2CLy = data4_1[data4_1['variable'] == 'Pred2'][['value_close']]
data4_3CLy = data4_1[data4_1['variable'] == 'Pred6'][['value_close']]
data4_4CLy = data4_1[data4_1['variable'] == 'Pred7'][['value_close']]
data4_5CLy = data4_1[data4_1['variable'] == 'Pred9'][['value_close']]
data4_6CLy = data4_1[data4_1['variable'] == 'Pred12'][['value_close']]
data4_7CLy = data4_1[data4_1['variable'] == 'Pred15'][['value_close']]
data4_8CLy = data4_1[data4_1['variable'] == 'Pred18'][['value_close']]
data4_9CLy = data4_1[data4_1['variable'] == 'Pred21'][['value_close']]
data4_10CLy = data4_1[data4_1['variable'] == 'Pred24'][['value_close']]
data4_11CLy = data4_1[data4_1['variable'] == 'Pred27'][['value_close']]
data4_12CLy = data4_1[data4_1['variable'] == 'Pred33'][['value_close']] #
data4_13CLy = data4_1[data4_1['variable'] == 'Pred34'][['value_close']] #
data4_14CLy = data4_1[data4_1['variable'] == 'Pred37'][['value_close']]
data4_15CLy = data4_1[data4_1['variable'] == 'Pred52'][['value_close']] # 

data4_1Hhy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_high']]

data4_1Hhy = data4_1[data4_1['variable'] == 'Pred1'][['value_high']]
data4_2Hhy = data4_1[data4_1['variable'] == 'Pred2'][['value_high']]
data4_3Hhy = data4_1[data4_1['variable'] == 'Pred6'][['value_high']]
data4_4Hhy = data4_1[data4_1['variable'] == 'Pred7'][['value_high']]
data4_5Hhy = data4_1[data4_1['variable'] == 'Pred9'][['value_high']]
data4_6Hhy = data4_1[data4_1['variable'] == 'Pred12'][['value_high']]
data4_7Hhy = data4_1[data4_1['variable'] == 'Pred15'][['value_high']]
data4_8Hhy = data4_1[data4_1['variable'] == 'Pred18'][['value_high']]
data4_9Hhy = data4_1[data4_1['variable'] == 'Pred21'][['value_high']]
data4_10Hhy = data4_1[data4_1['variable'] == 'Pred24'][['value_high']]
data4_11Hhy = data4_1[data4_1['variable'] == 'Pred27'][['value_high']]
data4_12Hhy = data4_1[data4_1['variable'] == 'Pred33'][['value_high']] #
data4_13Hhy = data4_1[data4_1['variable'] == 'Pred34'][['value_high']] #
data4_14Hhy = data4_1[data4_1['variable'] == 'Pred37'][['value_high']]
data4_15Hhy = data4_1[data4_1['variable'] == 'Pred52'][['value_high']] # 

data4_1Lwy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_low']]

data4_1Lwy = data4_1[data4_1['variable'] == 'Pred1'][['value_low']]
data4_2Lwy = data4_1[data4_1['variable'] == 'Pred2'][['value_low']]
data4_3Lwy = data4_1[data4_1['variable'] == 'Pred6'][['value_low']]
data4_4Lwy = data4_1[data4_1['variable'] == 'Pred7'][['value_low']]
data4_5Lwy = data4_1[data4_1['variable'] == 'Pred9'][['value_low']]
data4_6Lwy = data4_1[data4_1['variable'] == 'Pred12'][['value_low']]
data4_7Lwy = data4_1[data4_1['variable'] == 'Pred15'][['value_low']]
data4_8Lwy = data4_1[data4_1['variable'] == 'Pred18'][['value_low']]
data4_9Lwy = data4_1[data4_1['variable'] == 'Pred21'][['value_low']]
data4_10Lwy = data4_1[data4_1['variable'] == 'Pred24'][['value_low']]
data4_11Lwy = data4_1[data4_1['variable'] == 'Pred27'][['value_low']]
data4_12Lwy = data4_1[data4_1['variable'] == 'Pred33'][['value_low']] #
data4_13Lwy = data4_1[data4_1['variable'] == 'Pred34'][['value_low']] #
data4_14Lwy = data4_1[data4_1['variable'] == 'Pred37'][['value_low']]
data4_15Lwy = data4_1[data4_1['variable'] == 'Pred52'][['value_low']] # 



st.set_option('deprecation.showPyplotGlobalUse', False)

# st.header("Single Select Coin Data")
st.markdown(f'### 4. 코인차트 , 예측날짜:  {select_date} 기준')
st.markdown(f'###### {formatted_date} 기준, 6일 전 데이터까지만 시각화 조회가능')


# close_up = data4_2['close_up'].values
# high_up = data4_2['high_up'].values
# low_up = data4_2['low_up'].values

# data4_2.close_up, data4_2.high_up, data4_2.low_up
# st.markdown(f'#### {select_coin} , 6 day predict date:  {select_date} {close_up, high_up, low_up}')

data4_2.index = [''] * len(data4_2)
st.write(data4_2)
    
    
    
    

    
    
    
    
    
    
    
    
    
col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
# column 1 에 담을 내용
# Plotting the first set of points
    fig, ax = plt.subplots()
    ax.plot(data4_1CLx, data4_1CLy['value_close'], linestyle='-', marker='None', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1CLy['value_close']), np.max(data4_1CLy['value_close']))
    ax.set_ylim(np.min(data4_1CLy['value_close'])*0.92, np.max(data4_1CLy['value_close'])*1.08)
    ax.set_facecolor('#e0ffff')
    
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_2CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_12CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_13CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_15CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_3CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_4CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_5CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_6CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
    
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_2Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_12Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_13Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_15Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_3Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_4Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_5Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_6Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_2Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_12Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_13Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_15Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_3Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_4Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_5Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_6Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    # ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("low ~ high range")
    ax.set_title(f'{select_coin} , 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.tick_params(axis='both', which='both', length=1, width=0.5)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)
    
    ax.plot(data4_1CLx[:(len(data4_1Hhy0.value_high))], (data4_1Hhy0.value_high), linestyle='--', marker='*', color='black', linewidth=1)
    ax.plot(data4_1CLx[:(len(data4_1Lwy0.value_low))], (data4_1Lwy0.value_low), linestyle='--', marker='*', color='black', linewidth=1)


    # plt.show()
    st.pyplot(fig)



with col2 :
  # column 2 에 담을 내용
    fig, ax = plt.subplots()
    ax.plot(data4_1CLx, data4_1CLy['value_close'], linestyle='-', marker='None', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1CLy['value_close'])*0.92, np.max(data4_1CLy['value_close'])*1.08)
    
    
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_2CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_12CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_13CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_15CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_3CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_4CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_5CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_6CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("close")
    ax.set_title(f'{select_coin} , close 6 day predict date :  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)




    # plt.show()
    st.pyplot(fig)

col3,col4 = st.columns([1,1])


with col3 :
  # column 1 에 담을 내용
    fig, ax = plt.subplots()
    ax.plot(data4_1CLx, data4_1Hhy['value_high'], linestyle='-', marker='None', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1Hhy['value_high'])*0.92, np.max(data4_1Hhy['value_high'])*1.08)
    
    
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_2Hhy.value_high)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_12Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_13Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_15Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_3Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_4Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_5Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_6Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_7Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_8Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_9Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_10Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("high")
    ax.set_title(f'{select_coin} , high 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1Hhy.value_high[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1Hhy0.value_high))], (data4_1Hhy0.value_high), linestyle='-', marker='*', color='black', linewidth=2)
    # plt.show()
    st.pyplot(fig)
    


with col4 :
    fig, ax = plt.subplots() 
    ax.plot(data4_1CLx, data4_1Lwy['value_low'], linestyle='-', marker='o', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1Lwy['value_low'])*0.92, np.max(data4_1Lwy['value_low'])*1.08)
    
     
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_2Lwy.value_low)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_12Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_13Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_15Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_3Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_4Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_5Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_6Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_7Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_8Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_9Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_10Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("low")
    ax.set_title(f'{select_coin} , low 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1Lwy.value_low[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1Lwy0.value_low))], (data4_1Lwy0.value_low), linestyle='-', marker='*', color='black', linewidth=2)
    # plt.show()
    st.pyplot(fig)


    
