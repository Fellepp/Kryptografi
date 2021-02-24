

def get_letter(A):
  return ord(A) -65

if __name__ == "__main__":
  import sys
  letter = sys.argv[1]
  print(get_letter(letter))
