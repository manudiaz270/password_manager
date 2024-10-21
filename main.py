#guardar contraseñas encriptadas con el usuario y la cuenta
#poder agregar contraseñas o pedirlas, utilizando una contraseña maestra
#mantenerse entre sesiones
import csv

data = [
    {'account': 'instagram', 'name': 'manu', 'password': 'aflewybfalye'},
    {'account': 'youtube', 'name': 'manucho', 'password': 'kajsbdlfhaadf'}
]

with open('passwords.csv', 'w', newline='') as passwords:
    fieldnames = ['account', 'name', 'password']
    writer = csv.DictWriter(passwords, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data) 