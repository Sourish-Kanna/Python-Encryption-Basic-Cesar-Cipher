Cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Num = ' 0123456789_-=+/*'
LETTERS = Cap+Num+Cap.lower()
end = len(LETTERS)

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>end-1:
                num-=end
                encrypted +=  '?'
            encrypted +=  LETTERS[num]
    return encrypted

def decrypt(message, key):
    decrypted = ''
    cc=0
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            if chars=="?":
                cc=1
                pass
            if cc==1:
                num=end-num
                cc=0
            decrypted +=  LETTERS[num]
    return decrypted

def encrypt_new(message):
    encrypted = []
    for chars in message:
        txt=ord(chars)
        encrypted.append(txt)
    return encrypted

def decrypt_new(message):
    decrypted = ''
    cc=0
    for chars in message:
        txt=chr(chars)
        decrypted += txt
    return decrypted

if __name__ == '__main__':
    a = input("Enter Type:\n1] Text Output\n2] List Output\nYour Choice: ")

    if a == '1':
        message = str(input('Enter your message: '))
        key = int(input('Enter you key [1 - 26]: '))
        choice = input('Encrypt or Decrypt? [E/D]: ')

        if choice.lower().startswith('e'):
            print('Your code',encrypt(message, key))
        else:
            print('Your message ',decrypt(message, key))

    elif a == '2':
        message = str(input('Enter your message: '))
        choice = input('Encrypt or Decrypt? [E/D]: ')

        if choice.lower()=="e":
            print('Your code',encrypt_new(message))
        else:
            print('Your message ',decrypt_new(eval(message)))
