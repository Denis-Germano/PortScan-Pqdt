# Created By: Denis Germano[ManinhuGuitar]

import sys
import socket
import pyfiglet

banner = pyfiglet.figlet_format("Port Scan")
print(banner)

# Qtd de argumentos
if len(sys.argv) == 4:
    ip = socket.gethostbyname(sys.argv[1])
    start_port = int((sys.argv[2]))
    end_port = int((sys.argv[3]))

    print(f'\033[4;33;40mScan IP:\033[m {ip} nas portas {start_port} a {end_port} \n')

    try:
        for port in range(int(start_port), int(end_port)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((ip,port))
            if result == 0:
                print(f"\033[7;30;42m[+]\033[m Porta {port} aberta")
            #else:
                #print(f'\033[7;30;41m[+]\033[m Porta {port} fechada') # Caso queira exibir as portas fechadas descomente o Else e o print
            s.close()
        
    except KeyboardInterrupt:
            print("\nSaindo do Programa !!!!")
            sys.exit()

    except socket.error:
            print("\Host não responde !!!!")
            sys.exit()

else:
    print(f"\033[4;33;40mForma de uso:\033[m python3 {sys.argv[0]} <ip> <start port> <end port>")