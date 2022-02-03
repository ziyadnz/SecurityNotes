import string
import base64


def xor(data,key):
    l=len(key)

    decoded = ""
    for i in range (0,len(data)):
        decoded+=chr(ord(data[i]) ^ ord(key[i %l ]))
    return decoded

f= open('flag.txt' , 'r')
flag=f.read()
f.close()
flag=base64.b64decode(flag)
for k in range(1,1000):
    if "STMCTF" in flag:
        break
    splitted=flag.split(':',1)
    print str(k) + ': ' + splitted[0]
    if splitted[0] =='base64':
        flag = base64.b64decode(splitted[1])
    elif splitted[0] == 'base32':
        flag= base64.b32decode(splitted[1])
    elif splitted[0] == 'base16':
        flag= base64.b16decode(splitted[1])
    elif splitted[0] == 'rot_13':
        flag= splitted[1].decode(encoding='rot_13', errors='strict')
    elif splitted[0] == 'bz2_codec':
        flag= splitted[1].decode(encoding='bz2_codec', errors='strict')
    elif splitted[0] == 'zlib_codec':
        flag= splitted[1].decode(encoding='zlib_codec', errors='strict')
    elif splitted[0][:4] == 'xor':
        letter= splitted[0][4]
        flag=xor(splitted[1],letter)
    else:
        continue
print flag
