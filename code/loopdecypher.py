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

    text='nbyly qum uh ifx qiguh qbi fcpyx ch u mbiy.  mby bux mi guhs wbcfxlyh '

    for i in range(1,4):
        print 'Cipher Shift Attempt ' ,i, ':',
        print decrypt(text,i)
        command = raw_input('press Enter to contine OR q to quit when code is cracked :')
        if command == 'q':
            print '\n'
            print 'It took ',i,'tries to crack this code.'
            break
