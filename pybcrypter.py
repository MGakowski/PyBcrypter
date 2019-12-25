import bcrypt
import time
print ("""                                              
 _____         _____                 _           
|  _  |_ _ ___| __  |___ ___ _ _ ___| |_ ___ ___ 
|   __| | |___| __ -|  _|  _| | | . |  _| -_|  _|
|__|  |_  |   |_____|___|_| |_  |  _|_| |___|_|  
      |___|                 |___|_|              
v1.0 - 2019 MGakowski
""")
hash_file = raw_input("Name of .txt hash file in this directory? \n")
hf = hash_file + ".txt"
dict_file = raw_input("Name of .txt dictionary file in this directory? \n")
df = dict_file + ".txt"
hash_lines = 0
with open(hf, 'r') as g:
    for line in g:
        hash_lines += 1
hashes = int(hash_lines)
print(str(hashes) + " Hashes loaded.")
up_to = int(0)
start_time = time.time()
for y in range(0, hash_lines):
    g = open(hf)
    lines = [line.rstrip() for line in g]
    dict_lines = 0
    with open(df, 'r') as f:
        for line in f:
            dict_lines += 1
    loop_for = int(dict_lines)
    with open(df, 'r') as f:
        for x in range(0, loop_for):
            cipher = str(lines[up_to])
            salt = cipher[:29]  # Extract salt
            a = f.readline()
            passwd = str(a.rstrip('\n'))
            hashed = bcrypt.hashpw(passwd, salt)
            if str(cipher) == str(hashed):
                print(" - Hash match: " + hashed + " : " + passwd)
        print("Dictionary exhausted, processing next hash in hashfile.")
        up_to += 1
elapsed_time = time.time() - start_time
total_hashes = int(hash_lines*dict_lines)
rate = int(total_hashes/elapsed_time)
print("Completed " + str(total_hashes) + " in " + str(elapsed_time) + " seconds. @ " + str(rate) + "/sec.")
end = raw_input()
