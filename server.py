from Communication.tcp import Server

server = Server(port = 11111, timeout = 0, decoding = 'utf8')




clients = []
while(1):
    new_client = server.accept()
    if (new_client != None):
        clients.append(new_client)
        clients[-1].write("ahoj")
        print("New Client! addr: " + str(clients[-1].address))
    for client in clients:
        client.write("{:4}".format(len()))
