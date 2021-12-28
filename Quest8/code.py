import struct
import base64

def main():
    f = open('hideandseek.png', 'rb').read()[8:]
    i = 0
    flag = b''
    while True:
        length = struct.unpack(">I", f[i:i+4])[0]
        types = f[i+4:i+8]
        chunk_data = f[i+8:i+8+length]
        i += 12 + length

        if types == b'IEND':
            break

        if types == b'eDIH':
            print(types, length, chunk_data)
            flag += chunk_data
    
    flag = base64.b64decode(flag)
    print("FLAG: ", flag)

if __name__ == '__main__':
    main()