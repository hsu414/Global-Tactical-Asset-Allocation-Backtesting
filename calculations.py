
import datetime
import yfinance as yf 
import pandas as pd


# calculate monthly performance
def calNMonthlyPerformanceMean(monthlyAvgPrice, months):

    performance =pd.DataFrame(columns= monthlyAvgPrice.columns)
    currentPrice = monthlyAvgPrice.iloc[-1]


    for n in months:
        performance= performance.append((currentPrice-monthlyAvgPrice.iloc[-1-n])*100/monthlyAvgPrice.iloc[-1-n],ignore_index=True)
    # print('performance table')
    # print(performance)
    return performance.mean()

def buyWhatThisMonth(tickers):
    # getFinanceData
    financeRecords= pd.DataFrame(dtype=float)
    financeRecords= yf.download(tickers, period='1y')['Adj Close']
    # print(financeRecords) 

    # filter the candidate which current price > 200 avg
    Avg200 = financeRecords.tail(200).mean(axis=0)
    candidates =  financeRecords[financeRecords.tail(1)>Avg200].dropna(axis=1, how='all').columns
    financeRecords= financeRecords[candidates]
    # print('Avg200')
    # print(Avg200)
   
    currentPrices = financeRecords.tail(1)
    financeRecords.drop(financeRecords.tail(1).index,inplace=True)
    monthlyAvgPrice = financeRecords.groupby(pd.Grouper(freq='M')).mean()

    # print('MonthlyAvgPrice')
    # print(monthlyAvgPrice)
    # print('CurrentPrice')
    # print(currentPrices)

        
    monthlyPerformanceMean= calNMonthlyPerformanceMean(monthlyAvgPrice[candidates], [1,3,6,11])
    # print('monthly performance mean')
    # print(monthlyPerformanceMean)

    #determine who has the best performance
    top3= monthlyPerformanceMean.sort_values(axis='index', ascending = False).iloc[0:3]
    


    return currentPrices[top3.index]
        


asset_class = ['VTV', 'MTUM', 'VBR', 'DWAS', 'EFA', 'EEM', 'IEF', 'IGOV', 'LQD', 'TLT', 'GSG', 'IAU', 'VNQ']
stocks =['XDWC.DE', 'LESW.DE', 'XDWI.DE', 'ENER.MI', 'LAFRI.MI', 'X022.DE', 'AUTP.MI', 'FOO.MI', 'LEEU.DE', 'RTA.MI', 'ZPRX.F', 'ZPRV.F', 'GIGB.L', 'GDXJ.MI', 'SMH', 'ESPO.MI', 'ESPO', 'XAD3.MI', 'BLUM.DE', 'CBSX.F', 'CYBR.MI', 'LERN.MI', 'FOOD.MI', 'ECOM.MI', 'AIAI.MI', 'DOCT.MI', 'BATT.MI', 'ETLF.F', 'BIOT.MI', 'ISPY.MI', 'GLUG.MI', 'WCLD.MI', 'PHPD.MI', 'PHPT.MI', 'VOLT.MI', 'WTAI.MI', 'DFE.MI', 'DGSE.MI', 'CSRU.MI', 'INDI.MI', 'IKOR.MI', 'SPYA.DE', 'COPA.MI', 'EXV6.DE', '18MS.F', 'C5S.MI', 'LINK-EUR', 'DOT1-EUR', 'ADA-EUR', 'LTC-EUR', 'EOS-EUR', 'COMP1-EUR', 'KNC-EUR', 'ATOM1-EUR', 'KSM-EUR', 'UNI3-EUR', 'MKR-EUR', 'SNX-EUR', 'AAVE-EUR', 'VGWE.F', 'EUNL.F', '5MVL.DE', 'EUNI.DE', 'DOGE-EUR', 'XRP-EUR', 'TRX-EUR', 'AMAL.MI', 'PIGI.L', '0P00016MCQ.F', 'ITEP.L','XMLC.F','CAPU.MI', 'CAPE.MI', 'EUNY.F', 'WTED.F', 'C030.DE','3OIL.L', '3HCL.MI', 'LCOP.MI', 'COPA.MI', '3NIL.MI', 'NICK.MI', '3SIL.MI', 'LSIL.MI', 'SOYB.MI', 'SOYO.MI', 'LCOR.MI', 'CORN.MI', 'LNGA.MI', '3NGL.MI', 'NGAS.MI',  'CRUD.MI', 'LOIL.MI', '2PAL.MI', 'QQQ3.MI', 'AIGA.MI', 'LAGR.MI', '3UBS.MI', '3BUL.MI', '5BUS.MI', '3EUL.MI', '3USS.MI', 'GLD', 'TLT', 'EXXT.DE', 'SLV', 'IEMG', 'URTH', '^GSPC', '^RUT', 'BTC-EUR', 'ETH-EUR', '^N225', 'ILTB', 'IWDP.SW', 'DISVX', 'VBR', 'DGS', 'IPRE.DE', 'IUSP.AS', 'GMF', 'INIVX', 'ICVT', 'DGTL.MI', 'HEAL.MI', 'CEMG.F', 'INRG.MI', 'RBOD.L', 'FM', 'VNM', 'LRGF', 'IFSE.MI', 'IHREF', 'EPP', 'SLY', 'EXSE.DE', 'EWX', 'SCJ', 'LQD', 'MTE.PA', 'ZPRS.F', 'TIP', 'GSG', 'IAU', 'VNQ', 'CNYA', 'MCHI', 'EWT', '^TECDAX', '^MDAXI','AGED.MI', 'ECAR.MI', 'PSLV', 'LOCK.MI', 'EEMS', 'VUKE.L', 'IEUS', 'IYC','EWG', 'EWGS', 'WOOD', 'IH2O.MI', 'DFE', 'EXH1.DE', 'EXV1.DE', 'EXV9.DE', 'EXV5.DE', 'EXV3.DE', 'QDVG.F', 'ISRHF', 'IUIT.SW', 'IMSXF', 'ISRUF', 'QDVK.F', '2B7A.DE', '2B7B.DE', 'IUCS.SW', 'IUCM.SW', 'EXV8.DE', 'EXV7.DE', 'EXV4.DE', 'EXV6.DE', 'EXV2.DE', 'EXH2.DE', 'EXH3.DE', 'EXH4.DE', 'EXH5.DE', 'EXH6.DE', 'EXH7.DE', 'EXH8.DE', 'EXH9.DE', 'IS04.F', 'IS05.F', 'IS0S.F', 'VEGI', 'IBGZ.MI', 'IBB1.DE', 'EUN1.F', 'EUN2.F', 'EUN3.F', 'EUN4.F', 'EUN5.F', 'EUN6.F', 'EUN8.DE', 'EUN9.F','IS06.F', 'IS07.DE', 'IBC2.DE', 'IBC3.DE', 'IBC4.DE', 'IBC5.DE', 'IBC6.DE', 'IBC7.DE', 'IBC9.F', 'IEMO.MI', 'XDN0.DE', 'GLUX.MI', 'SFTRY.SW', 'DIGI.DE', 'EMQQ.MI', 'EMQQ', 'SKYY.MI', 'ITEK.MI', 'H41J.DE', 'BCHN.MI', 'BCHN.L', 'MLPS.MI', 'IQSA.DE', 'EMV.MI', 'IBCJ.DE', 'C005.DE', 'MD4X.DE', 'LBRA.DE', 'LGWT.DE', 'EIDO', 'XMKO.MI', 'DBXV.DE', 'SMART.MI', 'IQCT.MI'
,'IUST.DE', 'IBCI.DE', 'IUS5.F', 'CSBGE7.MI', 'SXRP.F', 'SXRQ.F', 'CSBGU3.MI', 'CSBGU7.MI', 'CSBGU3.MI', 'IS02.DE', 'IUS7.F', 'EUN5.F', 'IS0R.F', 'IBCC.F', 'IS04.F', 'IUSU.F', 'IUSM.F', 'IBCA.F', 'EUN8.DE', 'IBCL.F', 'EUNW.F', 'EUN5.F', 'IBCI.F', 'IUST.F', 'IS0R.F', 'IUSP.F', 'IUS7.F', 'IS3C.F', 'CONV.MI'] 

print(buyWhatThisMonth(stocks))