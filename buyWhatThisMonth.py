#KamiiGTAA
#import necessary libraries
#pip install lib
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas as pd
import datetime
from functools import reduce

#function to calculate the date
#if the last day of a month is not a week day, the end date needs to be manually adjusted
def startTime_calc(period, start='none'):
    if start == "none" :
        this_month = datetime.datetime.now().month
        this_year = datetime.datetime.now().year 
    else:
        this_month = int(start.split('-')[1])
        this_year = int(start.split('-')[0])
    print(this_month,this_year)
 
    start_month = this_month - period
    start_year = this_year
    start_date = '01'
    end_year = this_year

    end_month = this_month - 1 
    #if the last day of a month is not a week day, the end date needs to be manually adjusted
    end_date = '31'

    if(end_month == 0):
       end_month = 12
       end_year = this_year - 1
        
    while(start_month <= 0):
        start_month = 12 + start_month 
        start_year = this_year - 1 
    string_start = calc_String(start_month)
        
    if(end_month == 4 or end_month == 6 or end_month == 9 or end_month == 11):
        end_date = '30'
    elif(end_month == 2):
        end_date = '28'
    string_start = calc_String(start_month)
    string_end = calc_String(end_month)
               
    start = str(start_year) + '-' + string_start + '-' + start_date
    end = str(end_year) + '-' + string_end + '-' + end_date

    return start, end

#macht Datum zweistellig 1.8 - 01.08
def calc_String(numb):
    
    if(numb < 10):
        string = '0' + str(numb)
        
    else:
        string = str(numb)
    
    return string


def geFinancetData(tickers,start,end):
    financeRecords = pd.DataFrame()

    #for ticker in tickers:
    df = web.get_data_yahoo(tickers,
                        start,
                        end)
    financeRecords = df[["Adj Close"]]   
           
    return financeRecords


# monthlyAvgPrice: panda.df months: [1, 3, 6, 12]
def calNMonthlyPerformanceMean(monthlyAvgPrice, months):
    monthlyPerformance =pd.DataFrame(columns= monthlyAvgPrice.columns)

    for n in months:
        monthlyPerformance= monthlyPerformance.append((monthlyAvgPrice.iloc[-1]-monthlyAvgPrice.iloc[-1-n])*100/monthlyAvgPrice.iloc[-1-n],ignore_index=True)
    #print('monthlyPerformance')
    #print(monthlyPerformance)
   
    return monthlyPerformance.mean()


def findBestCandidates(acc, cur):
    if acc.avgPerformance > cur.avgPerformance:
        return acc.ticker
    else: 
        return cur.ticker


def buyWhatThisMonth(tickers, this_month):
    # getFinanceData
    [start, end] =  startTime_calc(13, this_month)
    print(start, end) 
    financeRecords= geFinancetData(tickers, start, this_month )
    financeRecords= financeRecords['Adj Close']

    #sort the candidate which current price > 200 avg
    candidates =  financeRecords[financeRecords.tail(1)>financeRecords.tail(200).mean(axis=0)].dropna(axis=1, how='all').columns
    financeRecords= financeRecords[candidates]
   
    currentPrices = financeRecords.tail(1)
    financeRecords.drop(financeRecords.tail(1).index,inplace=True)
    monthlyAvgPrice = financeRecords.groupby(pd.Grouper(freq='M')).mean()
    #print('MonthlyAvgPrice')
    #print(monthlyAvgPrice)
    #print('CurrentPrice')
    #print(currentPrices)

     

    monthlyPerformanceMean= calNMonthlyPerformanceMean(monthlyAvgPrice[candidates], [1,3,6,12])

    #determine who has the best performance
    top3= monthlyPerformanceMean.sort_values(axis='index', ascending = False).iloc[0:3]
    #print(top3)
    

    return currentPrices[top3.index]



tickers = ['VTV', 'MTUM', 'VBR', 'DWAS', 'EFA', 'EEM', 'IEF', 'IGOV', 'LQD', 'TLT', 'GSG', 'IAU', 'VNQ']
#buyWhatThisMonth(tickers, '2019-01-01')
financeRecords= web.get_data_yahoo(tickers, '2020-12-01', '2021-01-01' )


