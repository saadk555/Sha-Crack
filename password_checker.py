import hashlib

def rw_array(file, passwords):
  with open(file,"rb") as f:
    line = f.readline().strip() 
    while line:
      passwords.append(line)
      line = f.readline().strip()

global T_file
T_file = ""

def crack_sha1_hash(hash):
  passwords = []
  rw_array (T_file,passwords)
      
  pass_dic = {}
  for i in passwords:
    hash_line = hashlib.sha1(i).hexdigest()
    pass_dic[hash_line] = i.decode()

  if hash in pass_dic:
    return pass_dic[hash]
  return False

def percent(p, w):
  r = float(p)* 100/float(w)
  return round(r,1) 




  
    