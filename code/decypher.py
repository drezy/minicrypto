def decrypt(text, shift):
    cyphertext=''
    for char in text.lower():
        #don't bother with spaces or punctuation 
        if 'a' <= char <= 'z':
            cyphertext += chr((ord(char) -ord('a') - shift) % 26 + ord('a'))
        else:
            #don't bother with spaces or punctuation 
            cyphertext += char
    return cyphertext



if __name__ == "__main__":

    text='cffg'

    print decrypt(text,1)
