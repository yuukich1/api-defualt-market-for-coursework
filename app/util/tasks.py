from celery import Celery
import smtplib
from email.message import EmailMessage
from app.config import SMTP_USER, SMTP_PASSWORD
from app.schemas import UserRead

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_for_verify_user(user: UserRead):
    email = EmailMessage()
    email['Subject'] = 'Verify your account'
    email['From'] = SMTP_USER
    email['To'] = user.email

    email.set_content(
    """
    !   
    !   НУЖНО НАПИСАТЬ ВЕРСТКУ ДЛЯ СООБЩЕНИЯ ПОДТВЕРЖДЕНИЯ ПОЛЬЗОВАТЕЛЯ
    !
    """
    )


@celery.task
def send_mail_to_verify_user(user: UserRead):
    email = get_email_template_for_verify_user(email)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(email)