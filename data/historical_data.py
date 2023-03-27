import pandas as pd
import yfinance as yf
from typing import List, Dict


def fetch_historical_data(symbols: List[str], start_date: str, end_date: str) -> Dict[str, pd.DataFrame]:
    """
    Obtiene los datos históricos de los símbolos de las acciones especificados para un rango de fechas.

    :param symbols: Una lista de símbolos de acciones.
    :param start_date: La fecha de inicio en formato "yyyy-mm-dd".
    :param end_date: La fecha de finalización en formato "yyyy-mm-dd".
    :return: Un diccionario que contiene DataFrames de pandas con los datos históricos de cada acción.
    """
    historical_data = {}

    for symbol in symbols:
        stock = yf.Ticker(symbol)
        stock_history = stock.history(start=start_date, end=end_date)

        if len(stock_history) > 0:
            historical_data[symbol] = stock_history
        else:
            print(f"No se pudo obtener datos históricos para {symbol}.")

    return historical_data

