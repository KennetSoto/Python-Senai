import pyautogui as auto
import os
import time

auto.PAUSE = 0.5

# abrir gitbash
auto.press('win')
auto.write('git bash')
auto.press('enter')

auto.write('cd ~/Desktop')
auto.press('enter')

auto.write('mkdir NovaPastaGit')
auto.press('enter')

auto.write('cd NovaPastaGit')
auto.press('enter')

auto.write('git init')
auto.press('enter')

#usuário insira o nome do arquivo
auto.write('read -p "Digite o nome do arquivo e aperte enter: " arquivo')
auto.press('enter')

time.sleep(14)
auto.write('touch "$arquivo"')
auto.press('enter')

auto.write('git add .')
auto.press('enter')

#pede nome do usuario para configuração
auto.write('read -p "Digite o nome do usuario e aperte enter: " usuario')
auto.press('enter')

time.sleep(14)
auto.write('git config --local user.name "$usuario"')
auto.press('enter')

#pede email do usuario para configuração
auto.write('read -p "Digite o email e aperte enter: " email')
auto.press('enter')

time.sleep(20)
auto.write('git config --local user.email "$email"')
auto.press('enter')

#pede nome comit para configuração
auto.write('read -p "Digite o nome do comit e aperte enter: " comit')
auto.press('enter')

time.sleep(14)
auto.write('git commit -m "$comit"')
auto.press('enter')

#pede o comando completo para adicionar o repositorio remoto
auto.write('read -p "Cole o comando completo para adicionar o repositorio remoto e aperte enter: " repo')
auto.press('enter')

time.sleep(14)
auto.write('$repo')
auto.press('enter')

#envia para o repositorio remoto
auto.write('git push -u origin main')
auto.press('enter')
