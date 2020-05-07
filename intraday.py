import pandas as pd
import yfinance as yahoo
import numpy as np
import datetime as dt

start = dt.datetime(2020,4,29,11,0,0)
end =  dt.datetime(2020,4,29,15,59,59)

csv1 = r'merval4mayo.csv'
csv2 = r'adr4mayo.csv'

merval = yahoo.download(tickers="BMA.BA	CEPU.BA	CRES.BA	EDN.BA	GGAL.BA	IRSA.BA	LOMA.BA	PAMP.BA	SUPV.BA	TECO2.BA TGSU2.BA YPFD.BA", period="1d", interval = "1m")['Adj Close']

adr = yahoo.download(tickers="BMA CEPU CRESY EDN GGAL IRS LOMA PAM SUPV TEO TGS YPF", period= "1d", interval = "1m")['Adj Close']

merval = pd.DataFrame(data=merval)

merval = merval.rename(columns={'BMA.BA': 'BMABA', 'CEPU.BA': 'CEPUBA', 'CRES.BA': 'CRESBA',	'EDN.BA': 'EDNBA',
                                'GGAL.BA': 'GGALBA', 'IRSA.BA': 'IRSABA',	'LOMA.BA': 'LOMABA', 'PAMP.BA': 'PAMPBA',
                                'SUPV.BA': 'SUPVBA', 'TECO2.BA': 'TECO2BA', 'TGSU2.BA': 'TGSU2BA', 'YPFD.BA': 'YPFDBA'})

merval = merval.fillna(method='ffill')

merval = merval.iloc[:300,:]

adr = pd.DataFrame(data=adr)

adr = adr.fillna(method='ffill')

adr = adr.iloc[90:,:]

merval.to_csv(csv1)
adr.to_csv(csv2)


a = 'adr4mayo.csv'
m = 'merval4mayo.csv'
aa = open(a, 'r')
mm = open(m, 'r')
adr = pd.read_csv(a)
merval = pd.read_csv(m)
panorama = pd.DataFrame(data=None)

cable = pd.DataFrame(data=None)
cable['BMA'] = (merval.BMABA / adr.BMA) * 10
cable['CEPU'] = (merval.CEPUBA / adr.CEPU) * 10
cable['CRES'] = (merval.CRESBA / adr.CRESY) * 10
cable['EDN'] = (merval.EDNBA / adr.EDN) * 20
cable['GGAL'] = (merval.GGALBA / adr.GGAL) * 10
cable['IRSA'] = (merval.IRSABA / adr.IRS) * 10
cable['LOMA'] = (merval.LOMABA / adr.LOMA) * 5
cable['PAMP'] = (merval.PAMPBA / adr.PAM) * 25
cable['SUPV'] = (merval.SUPVBA / adr.SUPV) * 5
cable['TECO2'] = (merval.TECO2BA / adr.TEO) * 5
cable['TGSU2'] = (merval.TGSU2BA / adr.TGS) * 5
cable['YPF'] = (merval.YPFDBA / adr.YPF)
c = cable.T
cable['MIN'] = c.min()
cable['MAX'] = c.max()
cable['Rango'] = (c.max() / c.min()) - 1

writer = pd.ExcelWriter('galponcitos.xlsx', engine='xlsxwriter')

adr.to_excel(writer, sheet_name='adrs')

merval.to_excel(writer, sheet_name='merval')

cable.to_excel(writer, sheet_name='cable')

writer.save()