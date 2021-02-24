



def desc_log(g,y,n):
    for i in range(1,n+1):
        if (g**i % n)==y:
            return i


if __name__ == "__main__":
    import sys
    y = int(sys.argv[1])
    g = int(sys.argv[2])
    n = int(sys.argv[3])
    print(f"descreete log of g={g}, y={y},n={n} is {desc_log(g,y,n)}")



