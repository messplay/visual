# config/config.py

# Lista de símbolos de acciones a monitorear
STOCKS_TO_MONITOR = ["AAPL", "AMZN"]

# Intervalo de tiempo en segundos entre cada comprobación de las condiciones de entrada y salida
INTERVAL = 180

# Porcentaje de beneficio objetivo para cerrar una posición
PROFIT_PERCENTAGE = 2

# Porcentaje de pérdida máxima tolerada para cerrar una posición
LOSS_PERCENTAGE = 1

# Periodo para el cálculo de la media móvil exponencial corta
EMA_SHORT_PERIOD = 10

# Periodo para el cálculo de la media móvil exponencial larga
EMA_LONG_PERIOD = 30

# Periodo para el cálculo del indicador RSI
RSI_PERIOD = 14

# Periodo para el cálculo del MACD rápido
MACD_FAST_PERIOD = 12

# Periodo para el cálculo del MACD lento
MACD_SLOW_PERIOD = 26

# Periodo para el cálculo de la señal del MACD
MACD_SIGNAL_PERIOD = 9

# Configuración del correo electrónico para las alertas
EMAIL_CONFIG = {
    "email_sender": "*****@gmail.com",
    "email_password": "*****",
    "email_receiver": "******@gmail.com",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
}

# Configuración del registro
LOG_CONFIG = {
    "log_directory": "logs",
    "log_filename": "stock_monitor.log",
    "log_format": "%(asctime)s %(levelname)s [%(name)s] %(message)s",
    "log_level": "INFO",
}

LOG_DIRECTORY = LOG_CONFIG["log_directory"]
LOG_LEVEL = LOG_CONFIG["log_level"]
