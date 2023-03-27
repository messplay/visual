import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
from typing import Dict

def calculate_technical_indicators(stock_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """
    Calcula indicadores técnicos para los datos de acciones proporcionados.

    :param stock_data: Un diccionario que contiene DataFrames de pandas con los datos de las acciones.
    :return: Un diccionario que contiene DataFrames de pandas con los datos de las acciones y sus indicadores técnicos calculados.
    """
    stock_data_with_indicators = {}

    for symbol, data in stock_data.items():
        # Eliminar filas con valores NaN
        cleaned_data = dropna(data)

        # Calcular todos los indicadores técnicos disponibles
        try:
            # Asegurarse de que los datos de entrada tengan al menos 200 filas antes de calcular los indicadores técnicos
            if len(cleaned_data) >= 200:
                data_with_indicators = add_all_ta_features(cleaned_data, open="Open", high="High", low="Low", close="adj Close", volume="Volume")
                stock_data_with_indicators[symbol] = data_with_indicators
            else:
                print(f"No se pudieron calcular los indicadores técnicos para {symbol}. No hay suficientes datos.")
        except Exception as e:
            print(f"No se pudieron calcular los indicadores técnicos para {symbol}. Error: {str(e)}")

    return stock_data_with_indicators
