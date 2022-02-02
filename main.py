import os
import socket
import time
from platform import system
a = system()
b = socket.gethostbyaddr(socket.gethostname())[0]
print('''

 ██▀███  ▓█████   ██████  ██▓  ██████ ▄▄▄█████▓
▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓██▒▒██    ▒ ▓  ██▒ ▓▒
▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒░██░  ▒   ██▒░ ▓██▓ ░ 
░██▓ ▒██▒░▒████▒▒██████▒▒░██░▒██████▒▒  ▒██▒ ░ 
░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░    ░    
  ░░   ░    ░   ░  ░  ░   ▒ ░░  ░  ░    ░      
   ░        ░  ░      ░   ░        ░           
                                               
''')
print(f'information:   {b}       {a}')
po = input('''[1]login
[2]sign up\n>''')
if po == '1':
    c = input('Password\n>')
    with open('user') as n:
        m = n.readline()
        if m == c:
            os.startfile('server.py')
            os.startfile('client.py')
        else:
            for i in range(100):
                print('wrong password')
if po == '2':
    email = input('email\n>')
    a = '@'
    if a in email:
        with open('emails', 'w') as em:
            em.writelines(email)
            singup = input('new Password\n>')
            singup2 = input('check Password\n>')
            if singup == singup2:
                print('adding to database')
                time.sleep(5)
                with open('user', 'w') as re:
                    re.writelines(singup)
                os.startfile('client.py')
    else:
        print('wrong')
