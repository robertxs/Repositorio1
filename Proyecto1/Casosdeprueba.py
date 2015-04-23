'''as
Created on 20/4/2015

@author: samuel , roberto
'''
import unittest
from clsAccessControl import *

class clsAccessControlTester(unittest.TestCase):
    
    def setUp(self):
        self.tac = clsAccessControl()
    #Casos Validos Frontera
    def testnormal8(self):
        self.assertEqual(True, self.tac.check_password(self.tac.encript('prueba-1'),'prueba-1') )
    
    def testnormal16(self):
        self.assertEqual(True, self.tac.check_password(self.tac.encript('@prueba_version2'), '@prueba_version2'))
        
    #Casos Invalidos Frontera
    def testonly7(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('pru3ba?'), 'pru3ba?'))
        
    def testonly17(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('@prueba/version17'), '@prueba/version17'))
        
    def testbadpass(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('una.prueba?'),'un.aprueba?'))
            
    def testonlyletras(self):
        self.assertEqual(False,self.tac.check_password(self.tac.encript('ProbandoEsto'), 'ProbandoEsto'))
        
    def testonlynumeros(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('1234567890'), '1234567890'))
        
    def testonlycaracter(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('-@$%&/()=!/'), '-@$%&/()=!/'))
        
    def testletynum(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('prueba12'), 'prueba12'))
        
    def testletycara(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('¡prueba!'), '¡prueba!'))
    
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
        self.assertEqual(False, self.tac.check_password(self.tac.encript('☺mira_un_3moji'), '☺mira_un_emoji'))
        
    def testespacio(self):
        self.assertEqual(False, self.tac.check_password(self.tac.encript('(prue ba2)'), '(prue ba2)'))
    
    if __name__ == "__main__":
        unittest.main()
        