import yfinance as yf
import pandas as pd
from typing import List, Dict
from config import STOCKS_TO_MONITOR
import datetime

def fetch_live_data(stock_symbols: List[str]) -> Dict[str, pd.DataFrame]:
    """
    Obtiene datos en tiempo real de acciones utilizando la API de Yahoo Finance.

    :param stock_symbols: Una lista de símbolos de acciones.
    :return: Un diccionario que contiene DataFrames de pandas con los datos en tiempo real de cada acción.
    """
    live_data = {}

    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        stock_info = stock.info

        if stock_info:
            stock_data = pd.DataFrame([stock_info])
            end_date = datetime.datetime.today().strftime('%Y-%m-%d')
            start_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
            stock_history = stock.history(start='2023-03-20', end='2023-03-24', interval='1m')
            if not stock_history.empty:
                stock_data = stock_data.reindex(stock_history.index)
                stock_data['Close'] = stock_history['Close'].values
                live_data[symbol] = stock_data
            else:
                print(f"No se pudo obtener datos históricos para {symbol}.")
        else:
            print(f"No se pudo obtener datos en tiempo real para {symbol}.")

    return live_data
