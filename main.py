# File:		Gather-Stock-Data
# %% Imports
from dotenv.main import dotenv_values
from dotenv import load_dotenv
import requests
import orjson

load_dotenv()
config = dotenv_values(".env")

# %% Get all possible tickers with financial statements available on FMP
All_Tickers_URL = f"https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey={config['API_KEY']}"
response = requests.get(All_Tickers_URL)
# get all ticker symbols!
# get from the response text the JSON data in list form
All_Tickers = orjson.loads(response.text)

# %% 
