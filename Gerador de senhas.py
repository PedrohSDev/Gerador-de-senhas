import PySimpleGUI as sg
import random
import smtplib
import email.message

class PassGen:
    def __init__(self):
        # Define o layout da janela:
        sg.theme('Black')
        layout = [
            [sg.Text('Olá, seja bem-vindo ao Gerador de senhas!')],
            [sg.Text('')],
            [sg.Text('Descrição:')],
            [sg.Text('Ao inserir as informações abaixo, será gerada uma senha')],
            [sg.Text('automaticamente e, além disso, poderá ser salva em um')],
            [sg.Text('arquivo de texto ou via e-mail.')],
            [sg.Text('')],
            [sg.Text('Site/Software:'), sg.Input(key='site', size=(36,1))],
            [sg.Text('')],
            [sg.Text('E-mail:'), sg.Input(key='usuario', size=(42,1))],
            [sg.Text('')],
            [sg.Text('Quantidade de caracteres:'), sg.Combo(values=list(range(1, 31)), key='total_chars', 
                                                            default_value=1, size=(3,1))],
            [sg.Button('Gerar senha')],
            [sg.Output(size=(48,3))],
            [sg.Text('')],
            [sg.Button('Salvar senha em arquivo txt'),sg.Text('    '), sg.Button('Enviar senha por E-mail')]
        ]

        # Cria a janela:
        self.janela = sg.Window('Gerador de senhas', layout)
    
    # Inicia a leitura dos comandos da janela:
    def iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WIN_CLOSED:
                break
            
            if eventos == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(f'Sua senha: {nova_senha}')
                
            if eventos == 'Salvar senha em arquivo txt':
                self.salvar_senha(nova_senha, valores)
                            
            if eventos == 'Enviar senha por E-mail':
                nova_senha = self.gerar_senha(valores)
                self.enviar_email(nova_senha, valores['usuario'], valores['site'])
                
# Envia o E-mail para o destinatário e notifica o usuário:
    def enviar_email(self, nova_senha, usuario, site):
        corpo_email = f"""
        <p>Informações:</p>
        <p>Site: ({site})   Senha gerada: {nova_senha}</p>
        """
        msg = email.message.Message()
        msg['Subject'] = "Gerador de senhas - Sua senha:"
        msg['From'] = 'pedroalves112020@gmail.com'
        msg['To'] = usuario
        password = b'ysjenifsdrlcxlnm'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password.decode('utf-8'))
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        sg.popup_notify('E-mail enviado com sucesso!', fade_in_duration=10, location=(511,70))
    
    # Gera a senha:
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    # Salva a senha em txt e notifica o usuário:
    def salvar_senha(self, nova_senha, valores):
        with open('Senhas.txt', 'a', newline='', encoding='utf8') as arquivo:
            arquivo.write(f"Site: {valores['site']}, Usuário: {valores['usuario']}, Senha: {nova_senha}\n")
        sg.popup_notify('Arquivo salvo com sucesso!', fade_in_duration=10, location=(511,70))
   
# Inicia o programa:         
gerar = PassGen()
gerar.iniciar()
