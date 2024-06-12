import pyautogui as auto
import time
#instalar o cx_Freeze

# Gerar o arquivo 'requirements.txt':
# O comando 'pip freeze' lista todas as bibliotecas Python instaladas no ambiente atual.
# O operador '>' redireciona a saída do comando para o arquivo 'requirements.txt'.
# no terminal: pip freeze > requirements.txt
# listar todas as dependências do Python que seu projeto precisa para funcionar corretamente. 
# pode-se usar o comando pip install -r requirements.txt para instalar todas as dependências do seu projeto de uma só vez, em vez de instalá-las uma por uma.

#no terminal use o comando:  cxfreeze main.py --target-dir (nome da pasta onde vai baixar) ese comando baixa o executável junto com quaisquer bibliotecas Python que seu script dependa.
# os “arquivos baixados” seriam o executável criado a partir do seu script Python e quaisquer bibliotecas dependentes. 
# Isso permite que você distribua seu programa Python para pessoas que não têm o Python instalado em seus computadores.

#é uma variável que define um atraso global entre cada chamada de função
auto.PAUSE = 0.5

#abre o menu iniciar
auto.press('win')

#abre o edge
auto.write('edge')
#pressionar enter
auto.press('enter')

#abre o github
auto.write('github.com')
auto.press('enter')

# #aumenta a tela aberta
# auto.hotkey('alt', 'space')
# auto.press('x')

#abre um site em uma nova guia
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')

#abre um site em uma nova guia
auto.hotkey('ctrl','t')
auto.write('palmeiras.com')
auto.press('enter')

#abre um site em uma nova guia
time.sleep(3)
auto.hotkey('ctrl','t')
auto.write('moodle.df.senac.br')
auto.press('enter')