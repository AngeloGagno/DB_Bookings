import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def email_credenciais():
    load_dotenv(override=True)
    from_email = os.getenv('email') 
    to_email = "angelogagno@gmail.com"
    password = os.getenv('email_password') 
    return from_email,to_email,password


def email(credenciais,erro):

    from_email,to_email,password = credenciais
    subject = "Erro na inserção de dados no Banco"
    body = f"""<p>{erro}</p>
    """

    # Criação do objeto de mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))


    # Conectando ao servidor SMTP do Gmail e enviando o e-mail
    try:
        # Conexão com o servidor SMTP do Gmail (usando TLS)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Inicia a segurança TLS
        server.login(from_email, password)  # Faz o login na conta do Gmail

        # Enviando o e-mail
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

    finally:
        server.quit()
