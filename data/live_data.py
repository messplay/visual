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
            stock_history = stock.history(period='30d', interval='1d')
            if not stock_history.empty:
                # Agregar datos en tiempo real al final del DataFrame
                stock_history.loc[pd.Timestamp.now().tz_localize('UTC')] = [
                    stock_info['regularMarketOpen'],
                    stock_info['regularMarketDayHigh'],
                    stock_info['regularMarketDayLow'],
                    stock_info['regularMarketPrice'],
                    stock_info['regularMarketVolume'],
                    0,
                    0
                ]
                live_data[symbol] = stock_history
            else:
                print(f"No se pudo obtener datos históricos para {symbol}.")
        else:
            print(f"No se pudo obtener datos en tiempo real para {symbol}.")

    return live_data
