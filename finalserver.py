import socket
import pickle
import _thread
import os
import pymysql
from datetime import datetime

def find(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return os.path.join(root, name)


def communication(c):
	service=c.recv(30)
	service=pickle.loads(service)
	if service=="verify":
            c.send(pickle.dumps("ok"))
            data=c.recv(1024)
            data=pickle.loads(data)
            try:
                    db=pymysql.connect(host="127.0.0.1",user="root",passwd="",db="PRACTICE")
            except:
                    print("Connection to db refused")
                    return
            cur=db.cursor()
            sql="SELECT userid,password FROM user WHERE userid=%s"
            cur.execute(sql,(data['user'],))
            res=cur.fetchall()
            cur.close()
            db.commit()
            db.close()
            print(res)
            if len(res)==0:
                c.send(pickle.dumps("2"))
            elif data['user']==res[0][0] and data['pass'] ==res[0][1]:
                c.send(pickle.dumps("1"))
            else:
                c.send(pickle.dumps("0"))
            return
	if service=="myfiles":
		c.send(pickle.dumps("ok"))
		user=c.recv(30)
		user=pickle.loads(user)
		db=pymysql.connect(host="127.0.0.1",user="root",passwd="",db="PRACTICE")
		cur=db.cursor()
		sql="SELECT sender,file,remark,status,sign,new,date,size FROM file WHERE receiver=%s"
		cur.execute(sql,(user,))
		data=cur.fetchall()
		cur.close()
		db.commit()
		db.close()
		myfile=[]
		file={}
		for item in data:
			file={}
			file['sender']=item[0]
			file['fname']=item[1]
			file['msg']=item[2]
			file['mode']=item[3]
			file['sign']=item[4]
			file['new']=item[5]
			file['date']=item[6]
			file['size']=item[7]
			myfile.append(file)
		print(myfile)
		c.send(pickle.dumps(myfile))
		print("sent")
		print(pickle.dumps(myfile))
		return

	if service=="upload":
		c.send(pickle.dumps("ok"))
		info=c.recv(2048)
		info=pickle.loads(info)
		if info['fname']!="":
			f= open(info['fname'],"w")
			f.close()
		c.send(pickle.dumps("send"))
		
		while True:
			data=c.recv(1024)
			f= open(info['fname'],"a+b")
			f.write(data)
			f.close()
			if (len(data)<=0):
				print ("recieved")
				break
		print(info)
		db=pymysql.connect(host="127.0.0.1",user="root",passwd="",db="PRACTICE")
		cur=db.cursor()
		now = datetime.now()
		formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
		sql = "INSERT INTO file (sender,file,receiver,remark,size,date,status,sign,new) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s)"
		val = (info['sender'],info['fname'], info['reciever'],info['msg'],info['size'],formatted_date,info['mode'],"signature",1)
		cur.execute(sql,val)
		cur.close()
		db.commit()
		db.close()
						
	if service=="download":
		print ("coming")
		c.send(pickle.dumps("ok"))
		name=c.recv(100)
		name=pickle.loads(name)
		print ("request for:")
		print (name)
		path=find(name,"./")
		filesize=os.path.getsize(path)
		
		if path!=None:
			#c.send(name)
			file=open(path,"r+b")
			read=file.read(1024)
			while True:
				#print "sending length:"+str(len(read))
				c.send(read)
				if (len(read)<=0):
					break
				read=file.read(1024)
			print ("sent")
		else:
			c.send("0")
		
		


s=socket.socket()
s.bind(('192.168.43.19',4001))
print ('Server started!')
print ('Waiting for clients...')
print(socket.gethostname())
s.listen(1)

while True:
	c,addr=s.accept()
	print ("connected with")
	_thread.start_new_thread(communication,(c,))
s.close()	
