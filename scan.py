# Created By: Denis Germano[ManinhuGuitar]
# Version 1.1 - PortScan-Pqdt - python with MultiThreading
# https://github.com/Denis-Germano
# https://www.linkedin.com/in/dgermano/

import threading
import socket
import sys
import pyfiglet

banner = pyfiglet.figlet_format("PortScan pqdt")
print(banner)

# Verificando a qtd de argumentos
if len(sys.argv) == 4:
    ip = socket.gethostbyname(sys.argv[1])
    start_port = int((sys.argv[2]))
    end_port = int((sys.argv[3]))
    print(f'\033[4;33;40mEscaneando IP:\033[m {ip} nas portas {start_port} a {end_port} \n')

    # Port Scan
    def portscan(port=1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        try:
            con = s.connect((ip,port))
            print(f"\033[7;30;42m[+]\033[m Porta {port} aberta")
            con.close()
        
        except:
            pass

    # Thread
    def thread():
        r = 1
        for x in range(int(start_port), int(end_port)):
            t = threading.Thread(target=portscan, kwargs={'port':r})
            r += 1
            t.start()

    # Chamar a função        
    thread()

else:
    print(f"\033[4;33;40mForma de uso:\033[m python3 {sys.argv[0]} <ip or dns> <start port> <end port>")