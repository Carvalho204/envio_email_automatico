import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá</p>
    <p>Como você vai?</p>
    <p>Esse é o meu envio de email automático</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "TEMA"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Seu email foi enviado')


enviar_email()

