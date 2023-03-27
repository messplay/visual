import unittest
from unittest.mock import MagicMock
import pandas as pd
from strategies.entry_strategies import detect_entry_signals
from strategies.exit_strategies import detect_exit_signals, profit_loss_percentage

class TestStrategies(unittest.TestCase):
    def test_detect_entry_signals(self):
        mock_data_with_indicators = {
            "AAPL": pd.DataFrame({
                "Open": [100, 101, 102],
                "High": [105, 106, 107],
                "Low": [99, 98, 97],
                "Close": [104, 103, 108],
                "Volume": [1000, 2000, 3000],
                # Añadir aquí más columnas de indicadores técnicos
            })
        }

        entry_signals = detect_entry_signals(mock_data_with_indicators)

        self.assertEqual(len(entry_signals), 1, "Debería haber una señal de entrada para un símbolo de acciones")
        self.assertIn("AAPL", entry_signals, "Debería haber una señal de entrada para AAPL")

    def test_detect_exit_signals(self):
        mock_data_with_indicators = {
            "AAPL": pd.DataFrame({
                "Open": [100, 101, 102],
                "High": [105, 106, 107],
                "Low": [99, 98, 97],
                "Close": [104, 103, 108],
                "Volume": [1000, 2000, 3000],
                # Añadir aquí más columnas de indicadores técnicos
            })
        }

        open_positions = {
            "AAPL": ("buy", 100)
        }

        exit_signals = detect_exit_signals(profit_loss_percentage, mock_data_with_indicators, open_positions, 5, 2)

        self.assertEqual(len(exit_signals), 1, "Debería haber una señal de salida para un símbolo de acciones")
        self.assertIn("AAPL", exit_signals, "Debería haber una señal de salida para AAPL")

if __name__ == "__main__":
    unittest.main()
