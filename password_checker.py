import hashlib

# Opens the file of vulnerable passwords and adds every line from it, to the password's lists
def rw_array(file, passwords):
  with open(file,"rb") as f:
    line = f.readline().strip() 
    while line:
      passwords.append(line)
      line = f.readline().strip()

# global variable outside of the function to avoid unwanted loop 
global T_file
T_file = ""


# Main algorithm for hashing every line of the password's file to compare it with the given hash file

def crack_sha1_hash(hash):
  passwords = []
  rw_array (T_file,passwords)
      
  pass_dic = {}
  for i in passwords:
    hash_line = hashlib.sha256(i).hexdigest()
    pass_dic[hash_line] = i.decode()

  if hash in pass_dic:
    return pass_dic[hash]
  return False


# simple function with formula for percentage

def percent(p, w):
  r = float(p)* 100/float(w)
  return round(r,1) 




  
    