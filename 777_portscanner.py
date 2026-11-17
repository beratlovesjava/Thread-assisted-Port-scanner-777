import concurrent.futures
import socket

RESET = "\033[0m"
CYAN = "\033[38;2;0;255;255m"
BEYAZ = "\033[1;37m"
GRI = "\033[38;2;120;120;120m"



def portscan():
    ascii_art = """
         _____  _____  _____ 
        |___  ||___  ||___  |
           / /    / /    / / 
          / /    / /    / /  
         /_/    /_/    /_/   
        """
    print(CYAN + ascii_art + RESET)
    try:
        ip = input(GRI + "[?] Please enter target IP : " + RESET)
        ports = input(GRI + "[?] Please enter your ports (EX: 80,443,22) : " + RESET)
        ports = [int(port.strip()) for port in ports.split(",")]

        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)

                result = s.connect_ex((ip, port))

                if result == 0:
                    service = s.recv(4087).decode(errors='ignore').strip()
                    print(GRI + f"7777777777777777\n"
                          f"|Status Port Service:\n"
                          f"|[OPEN] {port} {service}\n"
                          f"7777777777777777" + RESET)
                else:
                    print(GRI + f"7777777777777777\n"
                          f"|Status Port Service:\n"
                          f"|[CLOSED] {port} \n"
                          f"7777777777777777" + RESET)

    except ValueError:
        print("[!] Invalid port number.")

    except socket.gaierror:
        print("[!] Invalid IP address or hostname.")

    except TimeoutError:
        print("[!] Connection timed out.")

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted.")

def threadedportscan1():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(portscan)

threadedportscan1()

