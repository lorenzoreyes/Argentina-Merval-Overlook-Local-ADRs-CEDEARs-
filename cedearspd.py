import yfinance as yahoo
import pandas as pd



data = yahoo.download(tickers="AAPL AAPL.BA ABT ABT.BA AIG AIG.BA AMD AMD.BA "
            "AMZN AMZN.BA BA BA.BA BABA BABA.BA  BMY BMY.BA BBD BBD.BA BBVA BBV.BA C "
            "C.BA CVX CVX.BA DIS DISN.BA DESP ERJ ERJ.BA DESP.BA FB FB.BA GE GE.BA " 
            "GLOB GLNT.BA GOLD GOLD.BA GOOGL GOOGL.BA GS GS.BA HPQ HPQ.BA JPM JPM.BA "
            "KO KO.BA MELI MELI.BA MRK MRK.BA MMM MMM.BA MSFT MSFT.BA NEM NEM.BA NFLX NFLX.BA "
            "PBR PBR.BA PG PG.BA SAN RIO.BA TSLA TSLA.BA TRIP TRIP.BA V V.BA "
            "VALE VALE.BA WFC WFC.BA WMT WMT.BA X X.BA", period="1y")['Adj Close']

data = data.fillna(method='ffill')

data = data.rename(columns={'AAPL.BA': 'AAPLBA','ABT.BA':'ABTBA', 'AIG.BA':'AIGBA', 'AMD.BA':'AMDBA',
                            'AMZN.BA':'AMZNBA', 'BA.BA':'BAB', 'BABA.BA':'BABABA',
                            'BMY.BA':'BMYBA', 'BBD.BA':'BBDBA','BBV.BA':'BBVBA','C.BA':'CBA',
                            'CVX.BA':'CVXBA','DISN.BA':'DISNBA','DESP.BA':'DESPBA','ERJ.BA':'ERJBA','FB.BA':'FBBA',
                            'GE.BA':'GEBA','GOLD.BA':'GOLDBA','GOOGL.BA':'GOOGLBA','GS.BA':'GSBA', 'GLNT.BA':'GLNTBA',
                            'HPQ.BA':'HPQBA','JPM.BA':'JPMBA','KO.BA':'KOBA','MELI.BA':'MELIBA',
                            'MRK.BA':'MRKBA','MMM.BA':'MMMBA','MSFT.BA':'MSFTBA','NEM.BA':'NEMBA',
                            'PG.BA':'PGBA','NFLX.BA':'NFLXBA','PBR.BA':'PBRBA','RIO.BA':'RIOBA',
                            'TSLA.BA':'TSLABA','TRIP.BA':'TRIPBA','V.BA':'VBA','VALE.BA':'VALEBA',
                            'WFC.BA':'WFCBA','WMT.BA':'WMTBA','X.BA':'XBA'})

cedears = pd.DataFrame()

cedears['AAPL'] = (data.AAPLBA / data.AAPL) * 10
cedears['ABT'] = (data.ABTBA / data.ABT) * 2
cedears['AIG'] = (data.AIGBA / data.AIG) * 5
cedears['AMD'] = (data.AMDBA / data.AMD) / 2
cedears['AMZN'] = (data.AMZNBA / data.AMZN) * 72
cedears['BA'] = (data.BAB / data.BA) * 3
cedears['BABA'] = (data.BABABA / data.BABA) * 9
cedears['BMY'] = (data.BMYBA / data.BMY)
cedears['BBD'] = (data.BBDBA / data.BBD)
cedears['BBV'] = (data.BBVBA / data.BBVA)
cedears['C'] = (data.CBA / data.C) * 3
cedears['CVX'] = (data.CVXBA / data.CVX) * 8
cedears['DIS'] = (data.DISNBA / data.DIS) * 4
cedears['DESP'] = (data.DESPBA / data.DESP)
cedears['ERJ'] = (data.ERJBA / data.ERJ)
cedears['FB'] = (data.FBBA / data.FB) * 8
cedears['GE'] = (data.GEBA / data.GE)
cedears['GOLD'] = (data.GOLDBA / data.GOLD)
cedears['GOOGL'] = (data.GOOGLBA / data.GOOGL) * 29
cedears['GS'] = (data.GSBA / data.GS) * 13
cedears['GLOB'] = (data.GLNTBA / data.GLOB) * 2
cedears['HPQ'] = (data.HPQBA / data.HPQ)
cedears['JPM'] = (data.JPMBA / data.JPM) * 5
cedears['KO'] = (data.KOBA / data.KO) * 5
cedears['MELI'] = (data.MELIBA / data.MELI) * 2
cedears['PG'] = (data.PGBA / data.PG) * 5
cedears['MRK'] = (data.MRKBA / data.MRK) * 5
cedears['MMM'] = (data.MMMBA / data.MMM) * 5
cedears['MSFT'] = (data.MSFTBA / data.MSFT) * 5
cedears['NEM'] = (data.NEMBA / data.NEM)
cedears['NFLX'] = (data.NFLXBA / data.NFLX) * 16
cedears['PBR'] = (data.PBRBA / data.PBR)
cedears['RIO'] = (data.RIOBA / data.SAN) / 4
cedears['TSLA'] = (data.TSLABA / data.TSLA) * 15
cedears['TRIP'] = (data.TRIPBA / data.TRIP) * 2
cedears['V'] = (data.VBA / data.V) * 6
cedears['VALE'] = (data.VALEBA / data.VALE) * 2
cedears['WFC'] = (data.WFCBA / data.WFC) * 5
cedears['WMT'] = (data.WMTBA / data.WMT) * 3
cedears['X'] = (data.XBA / data.X) * 3

dataarg = yahoo.download(tickers="AAPL.BA ABT.BA AIG.BA AMD.BA "
                              "AMZN.BA BA.BA BABA.BA  BMY.BA BBD.BA  BBV.BA "
                              "C.BA CVX.BA DISN.BA ERJ.BA DESP.BA FB.BA GE.BA "
                              "GLNT.BA GOLD GOLD.BA GOOGL.BA GS.BA HPQ.BA JPM.BA "
                              "KO.BA MELI.BA MRK.BA MMM.BA MSFT.BA NEM.BA NFLX.BA "
                              "PBR.BA PG.BA RIO.BA TSLA.BA TRIP.BA V.BA "
                              "VALE.BA WFC.BA WMT.BA X.BA", period="2y")['Adj Close']
