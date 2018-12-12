import socket
import time
import threading
class process1:
    
    def __init__(self, serverport):
        self.event = [0,0,0]
        self.event1 = [1,0,0]
        self.event2 = [2,0,0]
        self.serverport = int(serverport)
        self.sock = self.makeserversocket(self.serverport)
        
    def makeserversocket( self, port ):
        s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        s.bind(('localhost', port ))
        return s
    
    def listen(self):
        while True:
            try:
                if self.sock is not None:
                    data, clientaddr = self.sock.recvfrom(1024)
                    if clientaddr[1] == 7001:
                        self.event2[1] = self.event2[1]+1
                    elif clientaddr[1] == 7002:
                        self.event2[2] = self.event2[2]+1
            except KeyboardInterrupt:
                self.sock.close()
                
    def send_updates(self):
            self.sock.sendto(str(self.event1).encode('utf-8'),('localhost',7001))
            self.sock.sendto(str(self.event2).encode('utf-8'),('localhost',7001))
            self.sock.sendto(str(self.event1).encode('utf-8'),('localhost',7002))
            self.sock.sendto(str(self.event2).encode('utf-8'),('localhost',7002))
                    
    def print_vector(self):
        print('The vector at p1 is :',self.event2)
        
if __name__ == "__main__":
    server = process1(6000)
    time.sleep(0.5)
    threading.Thread(target = server.listen).start()
    threading.Thread(target = server.send_updates).start()
    # wait for all the threads to finish.
    time.sleep(3)
    server.print_vector()
    print('--------process 1----------ENDS')    
    