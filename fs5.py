
# working good with threading 

import socket,threading,os,tqdm




class sof1ane_serveur(object):
    
    
    def __init__(self,host,port):
        
        
        self._host,self._port = host,port
        
        self.address = (host,port)
        
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.fas = False
        
    def start(self):
        
        
        self.sock.bind(self.address)
        
        self.sock.listen(10)
        
        print ("servar is sur done ",self._port)
        
        self.gerer_con()
        
        
    def gerer_con(self):
        
        
        
        while True:
            clientsock,addr = self.sock.accept()
            print ("\033[1;36m conntion is found",addr)
            clientsock.sendall(str("1 2 3 /sdcard/hi /sdcard/photo /sdcard/photo").encode())
            self.th1 = threading.Thread(target=self.thread1,args=[clientsock])
            self.FILES = threading.Thread(target=self.files,args=[clientsock])
            self.th1.start()
            self.FILES.start()
                
        
      
            
    def thread1(self,clientsock):
        
        
      
        while True:
            x = " \033[0;31m [\033[0;36m->\033[0;31m] \033[42m\033[1;30m from ssss "+"\033[0;31m "+":  \033[0;33m"
            mesg = str(input(" \033[0;31m [\033[0;36m->\033[0;31m] \033[42m\033[1;30m me"+"\033[0;31m "+":  \033[0;33m "))
            if not mesg:
                break
                
                
                
            clientsock.send(mesg.encode())
                
            if self.fas == True :
                print(" \033[0;31m [\033[0;36m->\033[0;31m] \033[42m\033[1;30m me"+"\033[0;31m "+":  \033[0;33m  ")
                self.fas = False
                
                
                
        self.sock.close()
            
    
    def files(self,clientsock):
        CHUNKSIZE = 1048576
        os.makedirs('TOTstorage',exist_ok=True)
        with clientsock,clientsock.makefile('rb') as clientfile:
            while True:
                raw = clientfile.readline()
                if not raw: break # no more files, server closed connection.

                filename = raw.strip().decode()
                length = int(clientfile.readline())
       # print(f'Downloading {filename}...\n  Expecting {length:,} bytes...',end='',flush=True)

                path = os.path.join('TOTstorage',filename)
                os.makedirs(os.path.dirname(path),exist_ok=True)
        
                progress = tqdm.tqdm(range(length), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
                with open(path,'wb') as f:
                    while length:
                        chunk = min(length,CHUNKSIZE)
                        data = clientfile.read(chunk)
                        if not data: break
                        f.write(data)
                        length -= len(data)
                        progress.update(len(data))
                    else: # only runs if while doesn't break and length==0
                        print('Complete')
                        continue

                print('Incomplete')
                break
            
if __name__=="__main__":
    
    host = "102.164.96.97"
    # str(input("\n \033[42m\033[1;30m put Host\033[0;31m :\033[0;33m "))
    port = 5000
    try:
        serveur = sof1ane_serveur(host,port)
        serveur.start()
    except:
        exit()
        
