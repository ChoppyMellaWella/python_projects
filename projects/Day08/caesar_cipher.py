alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

phrase = input("What is the phrase to encode/decode: ")

sn = int(input("What is the shift number?: "))

np = ""

for char in phrase:
    if char in alphabet:
        print(alphabet[alphabet.index(char)+sn],end="")