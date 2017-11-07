import hashlib

 
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash1= sha1obj.hexdigest()       
        return hash1
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash2 = md5obj.hexdigest()
        return hash2
         
path1 = "C:/Users/Administrator/Desktop/C9064-information security/Assignment 1/assignment1-files/assignment1-evil"
path2 = "C:/Users/Administrator/Desktop/C9064-information security/Assignment 1/assignment1-files/assignment1-good"

print("evil MD5 value="+CalcMD5(path1))
print("good MD5 value="+CalcMD5(path2))

print("evil Sha1 value="+CalcSha1(path1))
print("good Sha1 value="+CalcSha1(path2))