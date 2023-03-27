import unittest
from unittest.mock import patch
from alerts.email_alerts import send_email_alert


class TestEmailAlerts(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_send_email_alert(self, mock_smtp):
        subject = "Prueba de alerta"
        message = "Este es el contenido de la prueba de alerta."

        send_email_alert(subject, message)

        # Verificar que se estableció conexión con el servidor SMTP
        mock_smtp.assert_called_once_with("smtp.example.com", 587)

        # Verificar que se llamó al método starttls()
        mock_smtp.return_value.starttls.assert_called_once()

        # Verificar que se llamó al método login()
        mock_smtp.return_value.login.assert_called_once_with("you@example.com", "your-password")

        # Verificar que se llamó al método sendmail()
        expected_email_body = f"Subject: {subject}\n\n{message}"
        mock_smtp.return_value.sendmail.assert_called_once_with("you@example.com", "recipient@example.com", expected_email_body)

        # Verificar que se llamó al método quit()
        mock_smtp.return_value.quit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
