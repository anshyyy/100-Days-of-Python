def encrypt(text,shift):
    msg=""
    for i in range(len(text)):
        x=ord(text[i])
        x+=shift
        msg+=chr(x)
    return msg

def decrypt(text,shift):
    msg=""
    for i in range(len(text)):
        x=ord(text[i])
        x-=shift
        msg+=chr(x)
    return msg 

    
while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if direction=="encode":
        print("Here's the encoded result:",encrypt(text,shift))

    if direction=="decode":
        print("Here's the decoded result: ",decrypt(text,shift))

    ans=input("Type 'yes' if you want to go again, otherwise 'no'\n")
    if ans=="no":
        break