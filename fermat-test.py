import sys
import random



def test(ran,num):
    for i in range(ran):
        r = random.randint(1,num)
        r = 4

        if (r**(num-1)%num != 1):
            return True
    return False


if __name__ == "__main__":
    num = int(sys.argv[1])
    try:
        rounds = int(sys.argv[2])
    except:
        ran = 1
    print("composite?",test(rounds,num))


