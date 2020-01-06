# 復号アルゴリズム
def Dec(cipher, key, table):
    plain = ""
    text_l = "abcdefghijklmnopqrstuvwxyz"
    text_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i,c in enumerate(cipher):
        plain += text_l[table[text_u.index(key[i % len(key)])].index(c)]

    return plain

def TableGen():
    table = []

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        table.append(text)
        text = text[1:] + text[0]

    return table

def Attack(cipher):
    cipher = cipher
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#DVZIYPZKGBWMINUVZEKMQBHRBQTIRVZRI
    for letter_1 in alphabet_upper:
        for letter_2 in alphabet_upper:
            for letter_3 in alphabet_upper:
                for letter_4 in alphabet_upper:

                            tmp_key = letter_1 + letter_2 + letter_3 + letter_4
                            tmp_plain = Dec(cipher, tmp_key, TableGen())
                            if ("i" in tmp_plain[0]) and ("n" in tmp_plain[1]) and ("t" in tmp_plain[2]) and ("e" in tmp_plain[3]):
                                print("Key might be {}".format(tmp_key))
                                print("Plaintext might be {}".format(tmp_plain[:40] + "..."))
                                print(tmp_plain[0:])
                                return tmp_plain
def Attack2(cipher):
    cipher = cipher
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#DVZIYPZKGBWMINUVZEKMQBHRBQTIRVZRI
    for letter_1 in alphabet_upper:
        for letter_2 in alphabet_upper:
            for letter_3 in alphabet_upper:
                for letter_4 in alphabet_upper:

                            tmp_key = "VIGENERE"+letter_1 + letter_2 + letter_3 + letter_4
                            tmp_plain = Dec(cipher, tmp_key, TableGen())
                            #if ("l" in tmp_plain[4]) and ("l" in tmp_plain[5]) and ("i" in tmp_plain[6]) and ("g" in tmp_plain[7]):
                            if ("e" in tmp_plain[8]) and ("n" in tmp_plain[9]) and ("t" in tmp_plain[10]) :#and ("i" in tmp_plain[11]):
                                print("Key might be {}".format(tmp_key))
                                print("Plaintext might be {}".format(tmp_plain[:40] + "..."))
                                print(tmp_plain[0:])
                                print()

def Attack3(cipher):
    cipher = cipher
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#DVZIYPZKGBWMINUVZEKMQBHRBQTIRVZRI
    for letter_1 in alphabet_upper:
        for letter_2 in alphabet_upper:
            for letter_3 in alphabet_upper:

                            tmp_key = letter_1 + letter_2 + letter_3
                            tmp_plain = Dec(cipher, tmp_key, TableGen())
                            if ("e" in tmp_plain[0]) :
                                print("Key might be {}".format(tmp_key))
                                print("Plaintext might be {}".format(tmp_plain[:40] + "..."))
                                print(tmp_plain[0:])



if __name__=="__main__":
    cipher = "DVZIYPZKGBWMINUVZEKMQBHRBQTIRVZRI"
    cipher2="dhtgltqinforeweivtbnginewntnn"
    cipher3="txfivjdrmatidxqnomceerinv"
    #cipher = Attack(cipher)
    #cipher_2=Attack2(cipher2.upper())
    cipher3 = Attack2(cipher)

"""
Key might be VIGENERECODE
Plaintext might be intelligentinformationengineering...
intelligentinformationengineering
"""
