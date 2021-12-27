#!/usr/bin/python3

# Encipherr-cli v1.0.0

# Cli version of the open source web app encipherr.Visit https://encipherr.pythonanywhere.com/.
# Made by Oussama Ben Sassi https://github.com/Oussama1403

# Contribute to the development of Encipherr-cli https://github.com/Oussama1403/Encipherr-CLI.
# Star the repo of Encipherr-cli if you like it :).

import argparse
from cryptography.fernet import Fernet
import os
import sys

def GenKey(args):
    key = Fernet.generate_key()
    print("your random generated key :\n",key.decode())

def is_valid_file(path):
    if not os.path.isfile(path):
        return False
    else:
        return True

def Encrypt(args):
    key = args.key
    if args.mode in ['file','FILE']:
        try:
            path = " ".join(args.input)
            print("specified path:",path)
            fernet = Fernet(key)
            
            if is_valid_file(path):
                with open(path,'rb') as f:
                    data = f.read()
            else:
                print("Error in provided path !") 
                sys.exit(1)       
            
            encryptedfile = fernet.encrypt(data)
            with open(path,'wb') as f:
                f.write(encryptedfile)
            print("the file at ",path," is encrypted")    
        except:
            print("Error in Encryption!, Possible problems : Invalid Key or Invalid input")    

    else:
        try:
            #text encryption mode
            value = " ".join(args.input)
            print("value",value)
            fernet = Fernet(key)
            plaintext = value.encode()
            encryptedtext = fernet.encrypt(plaintext)
            print()
            print('-'*5,"Encrypted text",'-'*5)
            print()
            print(encryptedtext.decode())
        except:
            print("Error in Encryption!, Possible problems : Invalid Key or Invalid input")    

def Decrypt(args):
    key = args.key
    if args.mode in ['file',"FILE"]:
        try:
            path = " ".join(args.input)
            print("specified path:",path)
            fernet = Fernet(key)
            
            if is_valid_file(path):
                with open(path,'rb') as f:
                    data = f.read()
            else:
                print("Error in provided path !") 
                sys.exit(1)
            
            decryptedfile = fernet.decrypt(data)
            with open(path,'wb') as f:
                f.write(decryptedfile)
            print("the file at ",path," is decrypted") 
        except:
            print("Error in Decryption!, Possible problems : Invalid Key or Invalid input")      
   
    
    else:
        try:
            #text decryption mode
            value = " ".join(args.input)
            fernet = Fernet(key)
            plaintext = value.encode()
            decryptedtext = fernet.decrypt(plaintext)
            print()
            print('-'*5,"decrypted text",'-'*5)
            print()
            print(decryptedtext.decode())
        except:
            print("Error in Decryption!, Possible problems : Invalid Key or Invalid input")      


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description="Encipherr-CLI 1.0.0 (https://github.com/Oussama1403/Encipherr-CLI)",
epilog='Exemple:\n\n python3 encipherr.py encrypt ueVEtmfzr8d... TEXT encipherr is awesome!\n ---or---\n python3 encipherr.py decrypt ueVEtmfzr8d... FILE path/to/file\n\n *if you don\'t have a key:\n python3 encipherr.py genkey\n\nan issue or a feature request ? contribute to the development of Encipherr-cli https://github.com/Oussama1403/Encipherr-CLI:)')
subparsers = parser.add_subparsers()

GenKey_parser = subparsers.add_parser('genkey',help="Generate a random key for encrypting/decrypting.")
GenKey_parser.set_defaults(func=GenKey)
 
Encrypt_parser = subparsers.add_parser('encrypt',help="encrypt key mode input")
Encrypt_parser.add_argument('key',type=str,help="your key for encrypting/decrypting.")
Encrypt_parser.add_argument('mode',type=str,choices=['text','TEXT','file','FILE'],help="TEXT or FILE")
Encrypt_parser.add_argument('input',type=str,nargs="+",help="A text if in text mode or path/to/file if in file mode")
Encrypt_parser.set_defaults(func=Encrypt)


Decrypt_parser = subparsers.add_parser('decrypt',help="decrypt key mode input")
Decrypt_parser.add_argument('key',type=str,help="your key for encrypting/decrypting.")
Decrypt_parser.add_argument('mode',type=str,choices=['text','TEXT','file','FILE'],help="TEXT or FILE")
Decrypt_parser.add_argument('input',type=str,nargs="+",help="A text if in text mode or path/to/file if in file mode")
Decrypt_parser.set_defaults(func=Decrypt)

if __name__ == '__main__':
    args = parser.parse_args()
    #if no args,show help and exit.
    if len(sys.argv)==1:
       parser.print_help(sys.stderr)
       sys.exit(1)
    
    args.func(args)