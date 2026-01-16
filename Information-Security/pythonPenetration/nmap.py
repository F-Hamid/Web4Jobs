import socket

def banner(ip,port):
    s=socket.socket()
    s.connect((ip,int(port)))
    s.settimeout(5)
    print(s.recv(1024))


def portScanner(ip,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host=input("Please enter the Ip adress: ")
    # port=int(input("Please enter the port you want to scan: "))
    if s.connect_ex((ip,port)):
        print(f"The port {port} is closed")
        return False
    else:
        print(f"The port {port} is open")
        return True





def main():
    ip=input("please enter an Ip adress: ")
    port=int(input("please enter a port: "))
    portOpened= portScanner(ip, port)
    if portOpened:
       banner(ip,port)
    else:
        print("Sorry! port closed")


main()
# 192.168.100.190

