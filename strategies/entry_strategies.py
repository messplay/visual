# strategies/entry_strategies.py

import ta
import numpy as np
import pandas as pd
from typing import List
from config.config import EMA_SHORT_PERIOD, EMA_LONG_PERIOD, RSI_PERIOD, MACD_FAST_PERIOD, MACD_SLOW_PERIOD, MACD_SIGNAL_PERIOD


def detect_entry_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detecta señales de entrada para una acción utilizando indicadores técnicos.

    :param df: Un DataFrame de pandas que contiene los precios históricos de una acción.
    :return: Un DataFrame de pandas que contiene las señales de entrada detectadas.
    """
    df = df.copy()

    # Calcula los indicadores técnicos necesarios
    df["ema_short"] = ta.trend.ema_indicator(df["Close"], window=EMA_SHORT_PERIOD)
    df["ema_long"] = ta.trend.ema_indicator(df["Close"], window=EMA_LONG_PERIOD)
    df["rsi"] = ta.momentum.rsi(df["Close"], window=RSI_PERIOD)
    macd = ta.trend.macd_diff(df["Close"], window_fast=MACD_FAST_PERIOD, window_slow=MACD_SLOW_PERIOD, window_sign=MACD_SIGNAL_PERIOD)
    df["macd"] = macd

    # Detecta las señales de entrada
    df["ema_signal"] = np.where(df["ema_short"] > df["ema_long"], 1, 0)
    df["rsi_signal"] = np.where(df["rsi"] < 30, 1, 0)
    df["macd_signal"] = np.where(macd > 0, 1, 0)

    # Calcula la señal final de entrada
    df["entry_signal"] = np.where((df["ema_signal"] == 1) & (df["rsi_signal"] == 1) & (df["macd_signal"] == 1), 1, 0)

    return df
