Purpose
This file request data from argentinian adrs stocks,
their parallel quote in Argentina plus the official 
argentinian's peso exchange rate
Due to capital controls started in August 2019, the 
quantity to exchange capital had been constrained 
and prices are not relatable to official entities
We can get the market price for the real value of Peso
following the process of grabing local stock quote, divide
it by it adr in New York and multiply the result by the 
convertion ratio 

This file only needs pandas, pandas_datareader and datetime
modules.
You retrieve information from April 2019 to today 