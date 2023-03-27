import pandas as pd

def stop_loss_trailing(data: pd.DataFrame, position: tuple, loss_percentage: float) -> tuple:
    """
    Implementa una estrategia de stop loss móvil para cerrar una posición abierta si el precio de la acción cae por debajo de un cierto porcentaje del precio de entrada.

    :param data: DataFrame de pandas que contiene los datos históricos de una acción.
    :param position: Tupla que contiene la información de una posición abierta, incluyendo el símbolo de la acción, la señal de entrada y el precio de entrada.
    :param loss_percentage: Porcentaje de pérdida máxima tolerada para cerrar la posición.
    :return: Una tupla con el símbolo de la acción y una señal de salida si se ha alcanzado el stop loss, o None si no se ha alcanzado.
    """
    symbol, entry_signal, entry_price = position
    stop_loss_price = entry_price * (1 - loss_percentage / 100)

    for i in range(len(data)):
        current_price = data.iloc[i].close

        if current_price <= stop_loss_price:
            return symbol, "Stop loss"

        if current_price > entry_price:
            stop_loss_price = current_price * (1 - loss_percentage / 100)

    return None