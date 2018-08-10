#!/usr/bin/python
import socket , time
a = []  # a adinda bir liste tanimliyoruz.
t0 = time.time() # su anki zamani getirdik

with open("wordlistimiz" ,"r") as f: #wordlistin icine girdik
    for line in f:      
        a.append(line.rstrip('\n')) #sag tarafindan alt satiri kirparak listeye ekliyoruz
f.close()       #isimiz bitti

n = len(a) # n'e a'nin uzunlugunu atiyoruz.

for i in range(0,n,100):
    s=socket.socket # soketimizi belirledik
    s.connect(("cnn.com",80))#site ve portumuz belli baska bir site yada portta belirleyebilirsiniz.
    for j in range(0,100):
        k = i + j
        if k < n :
            req = "HEAD / " + a[k] + "HTTP/1.1\nHost: hackazon.samsclass.info\n\n"
            r= s.recv(8192)[9:12]
            if r !="404":
                print (a[k]+ ' ' + r)
        s.shutdown(socket.SHUT_WR) # yazma kismini shutdown ettik.
        s.close() # soketimizi kapadik artik kullanilamaz.

print("Tahminler:" + n + "Gecen sure:" + (time.time()-t0)+ "saniye.")