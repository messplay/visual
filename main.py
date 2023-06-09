import time
from data.live_data import fetch_live_data
from indicators.technical_indicators import calculate_technical_indicators
from strategies.entry_strategies import detect_entry_signals
from strategies.exit_strategies import detect_exit_signals, profit_loss_percentage
from alerts.email_alerts import send_email_alert
from logs.logger import logger
from config.config import STOCKS_TO_MONITOR, INTERVAL, PROFIT_PERCENTAGE, LOSS_PERCENTAGE
import pandas as pd

if __name__ == "__main__":
    open_positions = {}

    while True:
        try:
            # Obtener datos en vivo
            live_data = fetch_live_data(STOCKS_TO_MONITOR)

            # Calcular los indicadores técnicos
            data_with_indicators = calculate_technical_indicators(live_data)

            # Detectar señales de entrada
            entry_signals = detect_entry_signals(data_with_indicators)

            for stock, signal in entry_signals.items():
                if signal:
                    open_positions[stock] = (signal, live_data[stock].iloc[-1].Close)
                    message = f"Señal de entrada detectada para {stock}: {signal} a ${live_data[stock].iloc[-1].Close}"
                    send_email_alert(f"Señal de entrada {stock}", message)
                    logger.info(message)

            # Detectar señales de salida
            exit_signals = detect_exit_signals(profit_loss_percentage, data_with_indicators, open_positions, PROFIT_PERCENTAGE, LOSS_PERCENTAGE)

            for stock, signal in exit_signals.items():
                if signal:
                    del open_positions[stock]
                    message = f"Señal de salida detectada para {stock}: {signal} a ${live_data[stock].iloc[-1].Close}"
                    send_email_alert(f"Señal de salida {stock}", message)
                    logger.info(message)

            # Esperar hasta el próximo intervalo
            time.sleep(INTERVAL)

        except Exception as e:
            logger.error(f"Error en la ejecución del script: {str(e)}")
