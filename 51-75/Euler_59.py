# 101, 120, 112

import time

def decrypt(key: list, filename: str):

    if not len(key): # Making sure the length of the key is non-zero
        return
    
    # print("New key", key)
    keylen = len(key)
    char_list = [int(x) for x in open(filename, "r").read().split(',')]

    for c in range(len(char_list)):
        
        decrypted_letter = char_list[c] ^ key[c % keylen]

        if not ((decrypted_letter >= ord('a') and decrypted_letter <= ord('z'))\
            or (decrypted_letter >= ord('A') and decrypted_letter <= ord('Z'))\
            #or (decrypted_letter >= ord('0') and decrypted_letter <= ord('9'))\
            or decrypted_letter == ord(' ') or decrypted_letter == ord('-')\
            # or decrypted_letter == ord(',') or decrypted_letter == ord('.')\
            # or decrypted_letter == ord('\n')):
            ):
            # print()
            # print("Letters decrypted", c)
            # print()
            # print("-----------------------------")
            # print()

            if c > 2:
                char_list[c] = decrypted_letter
                continue

            return None

        # print(decrypted_letter >= ord('a') and decrypted_letter <= ord('z'))
        # print(decrypted_letter >= ord('A') and decrypted_letter <= ord('Z'))
        # print(decrypted_letter == ord(' ') or decrypted_letter == ord('-'))
        # print(decrypted_letter == ord(',') or decrypted_letter == ord('.'))
        # print()

        # print("Letter to decrypt", chr(char_list[c]), bin(char_list[c]), char_list[c])
        # print("Key              ", chr(key[c % keylen]), bin(key[c % keylen]), key[c % keylen])
        # print("Decrypted letter ", chr(decrypted_letter), bin(decrypted_letter), decrypted_letter)
        # print()
        # time.sleep(2)

        char_list[c] = decrypted_letter

    return [sum(char_list), ''.join([chr(ascii_val) for ascii_val in char_list])]


def main(filename: str):
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):
                string = decrypt([i, j, k], filename)

                if string is None:
                    continue

                print(string[0])
                # print(string[1])
                print([i, j, k])
                print()

def tests():
    # print(3 ^ 0) # 11 ^ 00 = 11
    # print(3 ^ 3)
    # print(3 ^ 1)

    # if None == True: # Comparing None to anything will always return False except None itself
    #     print("None is True")
    # elif None == False:
    #     print("None is False")
    # else:
    #     print("None is neither True nor False")

    # print(None is None) # True
    # print(None == None) # True

    # a = 1
    # b = 2
    # if a == 0\
    #     or b == 2:
    #     print("True")

    # print(ord('A'), ord('Z'), ord('a'), ord('z'), ord(' '), ord('-'), ord(','), ord('.'))
    pass


'''
KEY_LEN = 3

def decrypt(filename: str):
    char_list = [int(x) for x in open(filename, "r").read().split(',')]

    for i in range(ord('a'), ord('z') + 1):
        for c in range(0, len(char_list), KEY_LEN):

    return
'''

if __name__ == "__main__":
    # tests()
    # main("Euler_59-cipher.txt")
    string = decrypt([101, 120, 112], "Euler_59-cipher.txt")
    print("Sum:", string[0])
    print(string[1])
    # print(chr(101), chr(120), chr(112))
    

'''
loop through all possible keys used to encrypt
    loop through all the letters in the message this key would decrypt
        if letter ^ key is a letter
            continue

'''