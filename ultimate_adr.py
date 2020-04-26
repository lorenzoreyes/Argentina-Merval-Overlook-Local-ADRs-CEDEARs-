import pandas as pd
import pandas_datareader as data
import datetime as dt

# Part 1 get your data= adr and local stocks plus official exchange rate previous capital control

stock = ['BMA', 'BMA.BA', 'CEPU', 'CEPU.BA',  'CRESY', 'CRES.BA', 'EDN', 'EDN.BA',
        'GGAL', 'GGAL.BA', 'IRS', 'IRSA.BA', 'LOMA', 'LOMA.BA','PAM', 'PAMP.BA',
        'SUPV', 'SUPV.BA', 'TEO', 'TECO2.BA', 'TGS', 'TGSU2.BA','YPF', 'YPFD.BA', 'ARS=X']

start = dt.datetime(2019,4,1)

end = dt.datetime.today()

df = data.DataReader(stock, 'yahoo', start, end)['Adj Close']

data = pd.DataFrame(data=df)
# rename tickets due recognition problem to call columns
data = data.rename(columns={'BMA.BA':'BMABA', 'CEPU.BA':'CEPUBA', 'CRES.BA': 'CRESBA', 'EDN.BA':'EDNBA',
                            'GGAL.BA':'GGALBA', 'IRSA.BA':'IRSABA', 'LOMA.BA':'LOMABA', 'PAMP.BA':'PAMPBA',
                            'SUPV.BA':'SUPVBA', 'TECO2.BA':'TECO2BA', 'TGSU2.BA':'TGSU2BA', 'YPFD.BA':'YPFDBA',
                            'ARS=X':'USDARS'})

data = data.fillna(method='ffill')

cable = pd.DataFrame(data=None)

# Part 2 make a sheet of every stock ccl by dividing (stock/adr) multiply it convertion ratio stated

cable['BMA'] = (data.BMABA / data.BMA) * 10
cable['CEPU'] = (data.CEPUBA / data.CEPU) * 10
cable['CRES'] = (data.CRESBA / data.CRESY) * 10
cable['EDN'] = (data.EDNBA / data.EDN) * 20
cable['GGAL'] = (data.GGALBA / data.GGAL) * 10
cable['IRSA'] = (data.IRSABA / data.IRS) * 10
cable['LOMA'] = (data.LOMABA / data.LOMA) * 5
cable['PAMP'] = (data.PAMPBA / data.PAM) * 25
cable['SUPV'] = (data.SUPVBA / data.SUPV) * 5
cable['TECO2'] = (data.TECO2BA / data.TEO) * 5
cable['TGSU2'] = (data.TGSU2BA / data.TGS) * 5
cable['YPF'] = (data.YPFDBA / data.YPF)
c = cable.T
cable['MIN'] = c.min()
cable['MAX'] = c.max()
cable['Rango'] = (c.max() / c.min()) - 1  # create an spectre interval of opportunities gap to arbitrage
cable['USDARS'] = data.USDARS

writer = pd.ExcelWriter('ultimate adr.xlsx', engine='xlsxwriter')

data.to_excel(writer, sheet_name='local y adr')

cable.to_excel(writer, sheet_name='cable')

writer.save()