import hashlib
import binascii
from venv import create

from pip import main
from database import user_db

# Example 1
sha3_256hash = hashlib.sha3_256(b'Cobanov').digest()
# print("SHA3-256('Cobanov') = ", binascii.hexlify(sha3_256hash))

# Example 2
text = 'Cobanov'
text_b = b'Cobanov'  # same as text.encode
data = text.encode('utf8')

# print(text)
# print(text_b)
# print(data)

# Saving passwords into SQLite database as hash


def _convertSHA256(password):
    sha3_256hash = hashlib.sha3_256(password).digest()
    hex_password = binascii.hexlify(sha3_256hash)
    return hex_password


def _takeInfo():
    username = input('Please provide a User name: ')
    password = input('Please provide a password: ').encode('utf8')
    encrypted_password = _convertSHA256(password)
    return username, encrypted_password


def createUser():
    username, password = _takeInfo()
    user_db.addUserDB(username, password)


def login():
    username = input('Please provide a User name: ')
    __dbPassword = user_db.fetchUserDB(username)
    password = _convertSHA256(
        input('Please provide a password: ').encode('utf8'))

    print(password, __dbPassword)

    if __dbPassword == password:
        print('Succesfully login!')
    else:
        print('Password wrong!')


def resetPassword():
    # TODO
    pass


def changePassword():
    # TODO
    pass


if __name__ == '__main__':

    print('Signup or Login: ')
    choice = input('s or l: ')

    if choice == 's':
        createUser()

    elif choice == 'l':
        login()

    else:
        print('Something went wrong!')
