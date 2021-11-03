# File:		Gather-Stock-Data
# %% Imports
from dotenv.main import dotenv_values
from dotenv import load_dotenv
import requests
import orjson

load_dotenv()
config = dotenv_values(".env")

# %% URLs
Short_Quote_URL = f"https://financialmodelingprep.com/api/v3/quote-short/"


# %% Get all possible tickers with financial statements available on FMP
def Get_All_Tickers():
    all_tickers_url = f"https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey={config['API_KEY']}"
    response = requests.get(all_tickers_url)
    # get all ticker symbols!
    # get from the response text the JSON data in list form
    return orjson.loads(response.text)

# %% Function to Get the current stock price
def Get_Current_Price(stock: str):
    """Returns the current price of a stock

    Args:
        stock (str): The stock's ticker symbol

    Returns:
        float: The stock's current market price
    """
    response = requests.get(Short_Quote_URL + f"{stock}?apikey={config['API_KEY']}")
    response_list = orjson.loads(response.text)
    if (response_list == []):
        raise ValueError(f"Failed to retrieve {stock}")
    # response_list is of the form [ { ... } ]
    # get the first dictionary and get the value for the price key
    return float(response_list[0]['price'])


# %% Get MTTR stock data
Get_Current_Price('AAAAAA')
# %%
