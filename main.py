import hashlib
import os

def md5_for_file(f):
    #md5 =  hashlib.md5() 
    f = open(file_path, encoding='utf8')
    while True:
        data = f.readline()
        if not data:
            break
        hash_object = hashlib.md5(data.encode())
        print(data)
        print(hash_object)
        print(hash_object.digest())
        
        #md5.update(hash_object)
    f.close()    
    #return md5.hexdigest()

if __name__=='__main__':
  file_path = 'read.txt'
  md5_for_file(file_path)