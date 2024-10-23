import csv
from cryptography.fernet import Fernet
import ast
key = b'Z1MPWdmwabH551KvAu6LAodnA5u3G6KJNFgiJeQQvMI='

def add_password(key):
    account = input('account: ')
    name = input('name: ')
    password = input('password: ')
    fernet = Fernet(key)
    encoded_password = fernet.encrypt(password.encode())
    data = {'account': account, 'name': name, 'password': encoded_password}

    with open('passwords.csv', 'a', newline='') as passwords:
        feildnames = ['account', 'name', 'password']
        writer = csv.DictWriter(passwords, fieldnames=feildnames)
        writer.writerow(data)

def list_passwords(key):
    with open('passwords.csv', mode='r') as passwords:
        passwords_file = csv.reader(passwords)
        decrypted_passwords = []
        for lines in passwords_file:
            decrypted_passwords.append(lines)
        decrypted_passwords.pop(0)
        fernet = Fernet(key)
        
        for i in range(len(decrypted_passwords)):
            password = ast.literal_eval(decrypted_passwords[i][2])
            decrypted_passwords[i][2] = fernet.decrypt(password).decode()
        print(decrypted_passwords)


choice = int(input('add password (0), list passwords (1): '))
if choice:
    list_passwords(key)
else:
    add_password(key)