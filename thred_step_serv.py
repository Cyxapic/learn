import socket, threading                                                        
                                                                                
class talkToClient(threading.Thread):                                           
    def __init__(self, clientSock, addr):                                       
        self.clientSock = clientSock                                             
        self.addr = addr                                                        
        threading.Thread.__init__(self)                                         
    def run(self):                                                              
        while True:                                                             
            data = self.clientSock.recv(1024)                                    
            if not data:                                                        
                self.clientSock.send('bye')                                     
                break                                                           
            self.clientSock.send(data)                                          
            if data == 'close':                                                 
                break                                                           
        self.clientSock.close()                                                 
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        
conn.bind(('0.0.0.0', 2222))
conn.listen(10)                                                                 
while True:                                                                     
    channel, details = conn.accept()                                            
    talkToClient(channel, details).start()                                      
conn.close()
