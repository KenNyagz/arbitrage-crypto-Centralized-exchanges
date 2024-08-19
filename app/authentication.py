import bcrypt
import mysql.connector
from mysql.connector import IntegrityError


class user:
    '''User management class'''
    @classmethod
    def add_user(cls, user, password):
        '''Function to add a user'''
        if not user or not password:
            print("Please provide user and password")
            return

        salt = bcrypt.gensalt()
        encrypted_pwd = bcrypt.hashpw(password.encode('UTF-8'), salt)

        db = mysql.connector.connect(
            host='localhost',
            user='kennyagz',
            password='root',
            database='arbi_cove'
        )
        cursor = db.cursor()
        try:
            query = "INSERT INTO users (user, hashpwd) VALUES (%s, %s)"
            cursor.execute(query, (user, encrypted_pwd.decode('utf-8')))
            db.commit()
            print("User created")
        except IntegrityError:
            print('User exists.')
            raise ValueError

        cursor.close()
        db.close()
        return True


    @classmethod
    def user_auth(cls, user, password):
        '''Function to authenticate a user'''
        db = mysql.connector.connect(
            host='localhost',
            user='kennyagz',
            password='root',
            database='arbi_cove'
        )
        cursor = db.cursor()
        cursor.execute('SELECT user, hashpwd FROM users WHERE user=%s', (user,))
        result_user_pwd = cursor.fetchone()

        if result_user_pwd:
            _, hashpwd = result_user_pwd
            if bcrypt.checkpw(password.encode(), hashpwd.encode()):
                print('Successful Authentication')
                return True
            else:
                print('Incorrect password')
                return False