import socket

#IP = "10.190.33.32"
PORTS = [135, 139]

#conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try:
#    conn.connect((IP, PORT))
#except socket.error:
#    print("Не доступен")
#else:
#    print("Доступен")
#finally:
#    conn.close()
print('Start')
with open('C:/Users/s.egorov/Downloads/1.txt') as f:
    for ip_without_last in f:
        for last in range(1,255):
            last = str(last)
            ip = ip_without_last.strip() + last
            IP = ip
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for PORT in PORTS:
                try:
                    conn.settimeout(0.1)
                    conn.connect((IP, PORT))
                except socket.error:
                    #print(ip,':', PORT, '-- >', "Не доступен")
                    pass
                else:
                    with open('C:/Users/s.egorov/Downloads/file4.txt', '+a') as file2:
                            file2.write(ip + '\n')
                            print(ip,':', PORT, '-- >', "Доступен")
                finally:
                    conn.close()