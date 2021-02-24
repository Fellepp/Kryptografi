c = "TLNJG"
def decrypt(letter):
    lettord = ord(letter)-65
    lettord = (4*lettord + 64) %27
    return chr(lettord + 65)

p = ""

for i in c:
    p+= decrypt(i)
print(p)
def encrypt(letter):
    let = ord(letter)-65
    let2 = (7*let +11) %27
    return chr(let2 + 65)

asdf=""
for k in p:
    asdf += encrypt(k)
print(asdf)


