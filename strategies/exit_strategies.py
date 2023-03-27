import pandas as pd
from typing import Dict
from .stop_loss import stop_loss_trailing

def detect_exit_signals(profit_loss_percentage: float, stock_data_with_indicators: Dict[str, pd.DataFrame], open_positions: Dict[str, tuple], profit_percentage: float, loss_percentage: float) -> Dict[str, str]:
    """
    Detecta señales de salida para las posiciones abiertas.

    :param profit_loss_percentage: Función que calcula el porcentaje de beneficio o pérdida actual para una posición.
    :param stock_data_with_indicators: Un diccionario que contiene DataFrames de pandas con los datos de las acciones y sus indicadores técnicos calculados.
    :param open_positions: Un diccionario que contiene las posiciones abiertas y sus detalles.
    :param profit_percentage: El porcentaje de beneficio objetivo para cerrar una posición.
    :param loss_percentage: El porcentaje de pérdida máxima tolerada para cerrar una posición.
    :return: Un diccionario que contiene las señales de salida detectadas para cada acción.
    """
    exit_signals = {}

    for symbol, position in open_positions.items():
        # Calcular el porcentaje de beneficio o pérdida actual
        current_profit_loss_percentage = profit_loss_percentage(position[1], stock_data_with_indicators[symbol].iloc[-1].close)
        
        # Calcular la señal de salida correspondiente según los porcentajes de beneficio y pérdida
        if current_profit_loss_percentage >= profit_percentage:
            exit_signals[symbol] = "Take profit"
        elif current_profit_loss_percentage <= -loss_percentage:
            exit_signals[symbol] = "Stop loss"
        else:
            # Actualizar el stop loss para que se mueva con el precio
            open_positions[symbol] = (position[0], stop_loss_trailing(position[1], stock_data_with_indicators[symbol].iloc[-1].close, loss_percentage))
    
    return exit_signals


def profit_loss_percentage(entry_price: float, current_price: float) -> float:
    """
    Calcula el porcentaje de beneficio o pérdida actual para una posición.

    :param entry_price: El precio de entrada de la posición.
    :param current_price: El precio actual de la acción.
    :return: El porcentaje de beneficio o pérdida actual para la posición.
    """
    return ((current_price - entry_price) / entry_price) * 100.0
