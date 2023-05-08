### Gerador-de-senhas 🔐

O código em Python apresentado é um gerador de senhas que utiliza a biblioteca PySimpleGUI para criar uma interface gráfica para o usuário interagir com o programa.

A classe PassGen contém métodos para gerar a senha, salvar a senha em um arquivo de texto e enviar a senha gerada por e-mail. A janela criada contém campos para o usuário inserir informações como o site ou software que precisa da senha, o e-mail do usuário e a quantidade de caracteres que a senha deve ter. Além disso, há botões para gerar a senha, salvar a senha em um arquivo de texto e enviar a senha por e-mail.

Ao clicar no botão "Gerar senha", é chamado o método gerar_senha, que utiliza a biblioteca random para criar uma senha aleatória com a quantidade de caracteres especificada pelo usuário. A senha gerada é exibida na saída da janela.

📩 Ao clicar no botão "Salvar senha em arquivo txt", é chamado o método salvar_senha, que salva a senha gerada em um arquivo de texto com o nome "Senhas.txt", junto com as informações inseridas pelo usuário (site e e-mail). Uma notificação é exibida para o usuário informando que o arquivo foi salvo com sucesso.

🗒 Ao clicar no botão "Enviar senha por E-mail", é chamado o método enviar_email, utilizando a biblioteca smtplib, que envia a senha gerada por e-mail para o endereço de e-mail especificado pelo usuário. O corpo do e-mail contém informações como o site ou software que precisa da senha e a senha gerada. Uma notificação é exibida para o usuário informando que o e-mail foi enviado com sucesso.

### Sinta-se à vontade para entrar em contato em:

<a href = "mailto:contatopedrohsdev@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>  <a href="https://www.linkedin.com/in/pedro-silva-1032a7243/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 

### ✅ Sinta-se à vontade para entrar em contato, estou totalmente aberto à sugestões de melhorias e críticas construtivas!
