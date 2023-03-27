import pandas as pd
import yfinance as yf
from typing import List, Dict


def fetch_historical_data(stock_symbols: List[str], start_date: str, end_date: str) -> Dict[str, pd.DataFrame]:
    """
    Obtiene datos históricos de acciones utilizando la API de Yahoo Finance.

    :param stock_symbols: Una lista de símbolos de acciones.
    :param start_date: Fecha de inicio en formato "YYYY-MM-DD".
    :param end_date: Fecha de finalización en formato "YYYY-MM-DD".
    :return: Un diccionario que contiene DataFrames de pandas con los datos históricos de cada acción.
    """
    historical_data = {}

    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        stock_history = stock.history(start=start_date, end=end_date)
        if not stock_history.empty:
            historical_data[symbol] = stock_history
        else:
            print(f"No se pudo obtener datos históricos para {symbol}.")

    return historical_data
