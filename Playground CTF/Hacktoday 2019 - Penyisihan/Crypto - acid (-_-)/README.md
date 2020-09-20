# Crypto - acid (-_-)
friska like a vampire HAHAHAHA
<br>
format flag: hacktoday{flag}
<br>
author: monhack - IPB
# Solved
Teks yang berisi dalam file acid.txt adalah sebuah Cryptography <b>DNA Code</b>https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/dna_codes.png<br>
```python
mapping = {
    'AAA':'a',
    'AAC':'b',
    'AAG':'c',
    'AAT':'d',
    'ACA':'e',
    'ACC':'f',
    'ACG':'g',
    'ACT':'h',
    'AGA':'i',
    'AGC':'j',
    'AGG':'k',
    'AGT':'l',
    'ATA':'m',
    'ATC':'n',
    'ATG':'o',
    'ATT':'p',
    'CAA':'q',
    'CAC':'r',
    'CAG':'s',
    'CAT':'t',
    'CCA':'u',
    'CCC':'v',
    'CCG':'w',
    'CCT':'x',
    'CGA':'y',
    'CGC':'z',
    'CGG':'A',
    'CGT':'B',
    'CTA':'C',
    'CTC':'D',
    'CTG':'E',
    'CTT':'F',
    'GAA':'G',
    'GAC':'H',
    'GAG':'I',
    'GAT':'J',
    'GCA':'K',
    'GCC':'L',
    'GCG':'M',
    'GCT':'N',
    'GGA':'O',
    'GGC':'P',
    'GGG':'Q',
    'GGT':'R',
    'GTA':'S',
    'GTC':'T',
    'GTG':'U',
    'GTT':'V',
    'TAA':'W',
    'TAC':'X',
    'TAG':'Y',
    'TAT':'Z',
    'TCA':'1',
    'TCC':'2',
    'TCG':'3',
    'TCT':'4',
    'TGA':'5',
    'TGC':'6',
    'TGG':'7',
    'TGT':'8',
    'TTA':'9',
    'TTC':'0',
    'TTG':' ',
    'TTT':'.'
}

f = open("acid.txt", "r").read().strip()
flag = ""

for x in range(0, len(f), 3):
    flag += mapping[f[x:x + 3]]

print "hacktoday{" + flag.split("flag is")[1].split(" ")[1] + "}"
```
Flag : <b>hacktoday{DN4ismybl00d}</b>