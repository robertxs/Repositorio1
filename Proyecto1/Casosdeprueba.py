'''as
Created on 20/4/2015

@author: samuel , roberto
'''
import unittest
from clsAccessControl import *

class clsAccessControlTester(unittest.TestCase):
    
    def setUp(self):
        self.tac = clsAccessControl()
    #Caso para encript
    def testencript(self):  
        self.assertEqual(False, self.tac.encript('Hola123,./')=='')
        
    #Casos para check_password
    #Caso Valido
    def testnormal(self):
        self.assertEqual(True, self.tac.check_password(self.tac.encript('1A*1a*2a*'),'1A*1a*2a*') )
                         
    #Casos Validos Frontera
                        
    def testnormall8(self):
        self.assertEqual(True, self.tac.check_password(self.tac.encript('Prueba-1'),'Prueba-1') )
    
    def testnormal16(self):
        self.assertEqual(True, self.tac.check_password(self.tac.encript('@prUeba_version2'), '@prUeba_version2'))
        
    #Casos Invalidos Frontera
    def testonly7(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('Pru3ba?'), 'Pru3ba?'))
        
    def testonly17(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('@Prueba/version17'), '@Prueba/version17'))
            
    def testonlyletras(self):
        self.assertEqual(False,self.tac.check_password(self.tac.encript('ProbandoEsto'), 'ProbandoEsto'))
        
    def testonlynumeros(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('1234567890'), '1234567890'))
        
    def testonlycaracter(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('-@$%&/()=!/'), '-@$%&/()=!/'))
        
    def testletynum(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('Prueba12'), 'Prueba12'))
        
    def testletycara(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('¡Prueba!'), '¡Prueba!'))
    
    def testnumycara(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('(1234-5678)'), '(1234-5678)'))   
    
    #Casos Esquina 
    
    def testlet17(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('unaclavemuylargas'), 'unaclavemuylargas'))
    
    def testnum7(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('1234567'), '1234567'))
        
    def testchar8(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('$%&/()=@'), '$%&/()=@'))
        
    def testletnum8(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('clave123'), 'clave123'))
        
    def testletchar16(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('c!avesc()nch@rs%'), 'c!avesc()nch@rs%'))
        
    def testnumchar7(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('!$345&/'), '!$345&/'))
      
    #Casos Malicia
    def testemoji(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript(''), ''))
        
    def testespacio(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('prue ba2'), 'prue ba2'))
        
    if __name__ == "__main__":
        unittest.main()
        