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
auto.write('read -p "Digite o nome do arquivo: " arquivo')
auto.press('enter')

time.sleep(10)
auto.write('touch "$arquivo"')
auto.press('enter')

auto.write('git add .')
auto.press('enter')

auto.write('read -p "Digite o nome do usuario: "usuario')
auto.press('enter')

time.sleep(10)
auto.write('git config --local user.name "$usuario"')
auto.press('enter')
