from MTRecover import MT19937Recover
from robo_numbers import numbers

def decodeSecret(s, random_state):
    key = [random_state.getrandbits(8) for i in range(len(s))]
    return bytes([a^b for a,b in zip(key,s)])

def main():
    mtr = MT19937Recover()
    r_gen = mtr.go(numbers)

    with open("secret.enc", 'rb') as f:
        s = f.read()
    
    flag = decodeSecret(s, r_gen)
    print(str(flag, 'UTF-8'))

if __name__ == "__main__":
    main()