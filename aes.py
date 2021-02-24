def AES(P, K, r):
    saveKeys(P, K)
    for i in range(0, r):
        print("This is round number: " + str(i+1))
        print("The plaintext block, P, is: " + P)
        kk, kkk = getKeys()
        print(kk, kkk)
        step1, K2 = permutations(kk, kkk)
        print("Step 1: " + step1)
        step2 = substitutions(step1)
        print("Step 2: " + step2)
        step3 = posPermutation(step2)
        print("Step 3: " + step3)
        saveKeys(step3, K2)

def saveKeys(k, kk):
    global k1
    global k2
    k1 = k
    k2 = kk


def getKeys():
    return k1, k2

def permutations(P, K):
    K2 = K[1:len(K)] + K[0]
    print("The subkeys are K1 and K2, where K1 = " + str(K) + " and K2 = " + str(K2))
    return format(int(P, 2) ^ int(K, 2), '08b'),K2

def substitutions(step):
    lst = []
    for i in range(0, len(step), 2):
        lst.append(step[i] + step[i + 1])

    for i in range(0, len(lst), 1):
        lst[i] = pi_s_out[pi_s_in.index(lst[i])]
    res = ""
    for element in lst:
        res += element;
    return res


def posPermutation(step):
    lst = []
    for i in range(len(step)):
        lst.append("")

    for i in range(len(step)):
        lst[pi_p_out[pi_p_in[i]]] = step[i]

    res = ""
    for element in lst:
        res += element
    return res


K = "11000011"
P = "01010101"
pi_s_in = ["00", "01", "10", "11"]
pi_s_out = ["10", "00", "01", "11"]

pi_p_in = [0, 1, 2, 3, 4, 5, 6, 7]
pi_p_out = [3, 6, 0, 5, 2, 1, 7, 4]

AES(P, K, 4)
