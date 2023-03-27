# alerts/email_alerts.py

import smtplib
from email.message import EmailMessage
from config.config import EMAIL_CONFIG


def send_email_alert(subject: str, message: str) -> None:
    """
    Envía una alerta por correo electrónico.

    :param subject: El asunto del correo electrónico.
    :param message: El contenido del correo electrónico.
    """
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_CONFIG["email_sender"]
    msg["To"] = EMAIL_CONFIG["email_receiver"]

    try:
        with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"]) as server:
            server.starttls()
            server.login(EMAIL_CONFIG["email_sender"], EMAIL_CONFIG["email_password"])
            server.send_message(msg)
            print(f"Correo electrónico enviado: {subject}")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {str(e)}")


if __name__ == "__main__":
    # Ejemplo de uso
    send_email_alert("Prueba", "Este es un correo electrónico de prueba.")
