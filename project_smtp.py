#SMTP: simple mail transfer protocol
from Pessoas import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Funcao(email):
    #objeto
    # ativar o acesso no myacount.google do emissor (from_adress)
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465

    user = 'usuário email'
    password = 'senha'

    from_addr = 'quem vai receber'
    to_addrs = email


    email_content_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Botão</title>
            <!-- CSS -->
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
            <style>
                main{
                    text-align: center;
                    font-size: 2rem;
                    font-family: 'Roboto', sans-serif;
                }
                .button{
                    display: inline-block;
                    margin: 1rem;
                    padding: 0.5rem 1rem;
                    text-decoration: none;
                    text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
                    background: #15C3D6;
                    color: white;
                    border: 0;
                    border-radius: 0.5rem;
                    box-shadow: 5px 3px 3px #81dbe6 ;

                    transition: box-shadow  0.3s ease ,transform 0.3s ease;
                
                }
                .button:active {
                    box-shadow: 0 0 0 0 #15C3D6, inset 4px 3px 3px #2d95a3;
                    transform: translate(3px, 3px);
                }
            </style>
        </head>
        <body>
            <main>
                <a class = "button" href="https://www.google.com">Google</a>
            </main>
            
        </body>
        </html>
        """
    message1 = MIMEText('Funcionando com sucesso')
    message2 = MIMEText(email_content_html,'html')

    configurations = MIMEMultipart('alternative')
    configurations['subject'] = 'TESTE'
    configurations['from'] = from_addr
    configurations['to'] = to_addrs
    configurations.attach(message1)
    configurations.attach(message2)


    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(user, password)
    server.sendmail(from_addr, to_addrs, configurations.as_string() )
    server.quit()
    print(f'Mensagem mandada com sucesso para {to_addrs}')


while True:
    file_search(arquivo)
    
    escolha2 = str(input('Você quer acrescentar pessoas para mandar o email (s/n): ')).lower().strip()[0]
    if escolha2 in 's':
        nome = str(input('Digite o email: '))
        writting(arquivo, nome)
    
    print(' ')
    print('Lista: ')
    p = print(people(arquivo))
    escolha3 = str(input('Posso mandar o email paras as pessoas dessa lista ? (s/n) ')).lower().strip()[0]
    if escolha3 == 's':
        Funcao(p)

    escolha4 = str(input('Deseja sair (s/n): ')).lower().strip()[0]
    if escolha4 == 's':
        sleep(1)
        print('Saindo !!!')
        break







