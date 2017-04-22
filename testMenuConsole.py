import unittest
import menuConsole as mc


class TestMenuCreation (unittest.TestCase):
    """Test the menu display with 
    different informations and
    parameters"""
  
    def testCreateWithAnyParameters(self):       
        """#UT01
        create simple menu without 
        name, informations and properties
        catch the exception
        """
        monMenu = mc.menuConsole(None,None,None,None)
        monMenu.create()           
        self.assertRaises(ValueError,monMenu.display,None)

    def testCreateWithoutInformation(self):       
        """#UT02
        create simple menu without 
        informations and properties
        display an empty menu ''
        """
        monMenu = mc.menuConsole('myMenu',None,None,None)
        monMenu.create()  
        self.assertEqual(monMenu.display('myMenu'),'')      
        #self.assertRaises(ValueError,monMenu.display,None)


    def testCreateWithExistingName (self):        
        """ #UT03
        create 2 menus with the same name
        catch the exception
        """
        monMenu = mc.menuConsole('theName',None,None,None)
        monMenu.create()
        monMenu = self.assertRaises(ValueError,mc.menuConsole,'theName',None,None,None)
        self.assertTrue(monMenu == None)

    def testCreateWithBadFormatOptionsList (self):        
        """ #UT04
        create a menu with wrong option list
        catch the exception
        """
        myMenu = mc.menuConsole('theName','menu','option','?')
        self.assertRaises(ValueError,myMenu.create)
    
    def testCreateWithBadFormatOptionsTuple (self):        
        """ #UT04
        create a menu with wrong option list
        catch the exception
        """
        myMenu = mc.menuConsole('theName','menu',['opt','bad'],'?')
        self.assertRaises(IndexError,myMenu.create)

    def testSimpleMenuWithoutProperties(self):
        """UT03
        create a menu with simple informations :
        name, title, options and message
        test the screen result
        """
        # reference result
        screen  = ""
        screen += "The Title menu\n"
        screen += "1 option n°1\n"
        screen += "2 option n°2\n"
        screen += "input message : "
        
        # create the menu
        monMenu = mc.menuConsole('menu0',None,None,None)
        monMenu.create()
        monMenu = mc.menuConsole('menu1',
    	            'The Title menu',
    	            [
    	             ('option n°1', 1,'opt1'),
                  ('option n°2', 2,'opt2')
                 ],
                 'input message : ')
        monMenu.create()
        
        # test result 
        self.assertEqual(monMenu.display('menu1'), screen)
        
        
if __name__ == '__main__':
    unittest.main()