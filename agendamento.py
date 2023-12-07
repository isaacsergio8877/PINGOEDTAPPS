import schedule
import time

def minha_tarefa():
    import os
import smtplib
from email.message import EmailMessage

# Configurar email, senha
EMAIL_ADDRESS = 'isaacsergio8877@gmail.com'
EMAIL_PASSWORD = 'invs niky qhgg rjif'

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Pagamento Do site PINGOEDSTAPP'
msg['From'] = 'isaacsergio8877@gmail.com'
msg['To'] = 'santos.developer8877@gmail.com'
msg.set_content('O pagamento do site PINGOEDSTAPP no valor de R$ 100,00 acaba de se expirar, por favor cobre o pagamento para efetuar novamente o pagamento')

# Enviar um email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



# Agendar a tarefa para ser executada a cada minuto
schedule.every(4).weeks.do(minha_tarefa)

# Loop para manter o script em execução
while True:
    schedule.run_pending()
    time.sleep(1)
