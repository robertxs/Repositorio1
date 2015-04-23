# -*- coding: utf-8 -*-. 
'''
Created on 13/4/2015

@author: Roberto
'''
import uuid
import hashlib
import re
 
class clsAccessControl(object):
    def __init__(self):
        ohast=''
        
    def encript(self, value):
        # Verificar la longitud del password
        oHash=""
        olength_password=self.length_password(value)
        if olength_password>=8 and olength_password<=16:
            if (re.search(r'[a-z]', value) or re.search(r'[A-Z]', value)) and (re.search(r'[!-/]', value) 
                or re.search(r'[:-@]', value) or re.search(r'[[-`]', value) or re.search(r'[{-~]', value)) and re.search(r'\d', value):
                # uuid es usado para generar numeros random
                    salt = uuid.uuid4().hex
                # hash
                    oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
            else:
                print('El Password debe contener números, símbolos y caracteres')
                return False
        else:
            print('El Password debe contener entre 8 y 16 caracteres')
        return oHash   
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        # Verificar la longitud del password
        olength_password=self.length_password(oCheckPassword)
        if olength_password>=8 and olength_password<=16: 
            if (re.search(r'[a-z]', oCheckPassword) or re.search(r'[A-Z]', oCheckPassword)) and (re.search(r'[!-/]', oCheckPassword) 
                or re.search(r'[:-@]', oCheckPassword) or re.search(r'[[-`]', oCheckPassword) or re.search(r'[{-~]', oCheckPassword)) and re.search(r'\d', oCheckPassword):
                 # uuid es usado para generar numeros random
                 oPassworkEncript, salt = oPassworkEncript.split(':')
                 return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
            else:
                print('El Password debe contener números, símbolos y caracteres')
                return False
        else:
            print('El Password no posee la cantidad de caracteres requerida')
            return False
    
    def length_password(self, user_password):
        # uuid es usado para generar numeros random
        return len(user_password)

#Para encriptar un passwork  
oPassword = input('Por favor ingrese su password: ')
#Se crea un objeto tipo clsAccessControl
oAccessControl=clsAccessControl()
oPassworkEncript = oAccessControl.encript(oPassword)
print('El Password almacenado en la memoria es: ' + oPassworkEncript)
if oPassworkEncript:
    #Para validar el passwork introducido
    oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
    if oAccessControl.check_password(oPassworkEncript, oCheckPassword):
        print('Ha introducido el password correcto')
    else:
        print('El password es diferente')