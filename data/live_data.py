import yfinance as yf
import pandas as pd
from typing import List, Dict
from config import STOCKS_TO_MONITOR


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
            live_data[symbol] = stock_data
        else:
            print(f"No se pudo obtener datos en tiempo real para {symbol}.")

    return live_data
