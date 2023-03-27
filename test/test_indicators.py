import unittest
from unittest.mock import MagicMock
import pandas as pd
from indicators.technical_indicators import calculate_technical_indicators

class TestTechnicalIndicators(unittest.TestCase):
    def test_calculate_technical_indicators(self):
        mock_stock_data = {
            "AAPL": pd.DataFrame({
                "Open": [100, 101, 102],
                "High": [105, 106, 107],
                "Low": [99, 98, 97],
                "Close": [104, 103, 108],
                "Volume": [1000, 2000, 3000]
            })
        }

        stock_data_with_indicators = calculate_technical_indicators(mock_stock_data)

        self.assertEqual(len(stock_data_with_indicators), 1, "Debería haber datos para un símbolo de acciones")
        self.assertIn("AAPL", stock_data_with_indicators, "Debería haber datos para AAPL")

        aapl_data = stock_data_with_indicators["AAPL"]
        self.assertTrue(aapl_data.shape[1] > 5, "Debería haber más columnas que las originales (Open, High, Low, Close, Volume)")

        for column in ["Open", "High", "Low", "Close", "Volume"]:
            self.assertIn(column, aapl_data.columns, f"La columna {column} debería estar presente en los datos de AAPL")

if __name__ == "__main__":
    unittest.main()
