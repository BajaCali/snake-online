from Communication.tcp import Server

server = Server(port = 11111, timeout = 0, decoding = 'utf8')




clients = []

while(1):
    new_client = server.accept()
    if (new_client != None):
        clients.append(new_client)
        clients[-1].write("ahoj")
        print("New Client! addr: {}".format(str(clients[-1].address)))
    for client in clients:
        out = ""
        client.write("{:4}".format(len(out)))
        client.write(out)
    for client in clients:
        if not client.readable:
            closed.append(client)
        else:
            read = client.read()
            if read:
                print('from {} read {}'.format(id(client), read))
                client.write(read)
        for client in closed:
            print('Client disconected! addr: {}'.format(client.addr))
            clients.remove(client)

        

server.close()
for client in clients:
    client.close()
print('\n\nclosed')
