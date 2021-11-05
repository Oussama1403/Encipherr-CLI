# Encipherr-cli v0.1.0-alpha

# Cli version of the open source web app encipherr.Visit https://encipherr.pythonanywhere.com/.
# Made by Oussama Ben Sassi https://github.com/Oussama1403

# Contribute to the development of Encipherr-cli https://github.com/Oussama1403/Encipherr-CLI.
# Star the repo of Encipherr-cli if you like it :).


from cryptography.fernet import Fernet
import argparse
import sys

parser = argparse.ArgumentParser(description="Encipherr-CLI",usage='\n\npython3 %(prog)s -k yourkey -a E|D -t yourtext OR -f path/to/file\npython3 %(prog)s -genkey to generate a random key.',
epilog='an issue or a feature request ? contribute to the development of Encipherr-cli https://github.com/Oussama1403/Encipherr-CLI:)')

def ParseArgs():
    
    parser.add_argument('-genkey','--generate-key',dest="genkey",action="store_true",help="Generate a random key for encrypting/decrypting.")

    parser.add_argument('-k','-key',dest="key",type=str,help="your key for encrypting/decrypting.")
    parser.add_argument('-a','-action',dest="action",type=str,help="specify the action [E for encrypt | D for decrypt].")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t','-text',dest="text",type=str,help="type your a text after -t arg.") 
    group.add_argument('-f','-file',dest="filepath",type=str,help="specify the file path after -f arg.") 
    

    return parser.parse_args()


def GenKey():
    key = Fernet.generate_key()
    return key.decode()

def Encrypt(key,args):
    if args.text == None:
        print("File encryption is not implemented for the moment.")
        print("look for updates at https://github.com/Oussama1403/Encipherr-CLI.")
    else:
        try:
            #text encryption mode
            value = args.text
            fernet = Fernet(key)
            plaintext = value.encode()
            encryptedtext = fernet.encrypt(plaintext)
            print()
            print('-'*5,"Encrypted text",'-'*5)
            print()
            print(encryptedtext.decode())
        except:
            print("Error in Encryption!, Possible problems : Key Not Found or Invalid Key")    

def Decrypt(key,args):
    if args.text == None:
        print("File decryption is not implemented for the moment.")
        print("look for updates at https://github.com/Oussama1403/Encipherr-CLI.")
    else:
        try:
            #text decryption mode
            value = args.text
            fernet = Fernet(key)
            plaintext = value.encode()
            decryptedtext = fernet.decrypt(plaintext)
            print()
            print('-'*5,"decrypted text",'-'*5)
            print()
            print(decryptedtext.decode())
        except:
            print("Error in Decryption!, Possible problems : Key Not Found or Invalid Key")      

def main():
    args = ParseArgs()
    #if no args,show help and exit.
    if len(sys.argv)==1:
       parser.print_help(sys.stderr)
       sys.exit(1)
    #generate a key
    if args.genkey == True:
        key = GenKey()
        print(key)
    #call encrypt/decrypt functions
    if args.action == "E":
        key = args.key
        Encrypt(key,args)  
    elif args.action == "D":
        key = args.key
        Decrypt(key,args)
    else:
        pass     

#start program      
main()


