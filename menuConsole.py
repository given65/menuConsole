

class menuConsole():
    flagBDD = False # for validate bdd
    screen = {}
    def __init__(self, name,
    	            title,
    	            option,
    	            message,
    	            flagBDD = None,
    	            **dicParam
    	            ):
    	   # Manage the mode BDD to test
    	   # Force flag if the value is sent
        if flagBDD != None :
            self.flagBDD = flagBDD
        # else it's the default value
        # message to indicate the test mode
        if self.flagBDD : 
            print("\nBDD MODE\ninstanciate menuConsole")
        
        # Analyse and formate init parameters
        
        # if not named set default name
        if name == None or name == '' :
            name = 'default'
        # if already exist raise an error
        if self.screen.get(name) != None:
            msgError ='Error object menuConsole there is already a menu named {0}'
            msgError = msgError.format(name)
            raise ValueError(msgError)
            # if not title set it to empty string
        
        # if no title it is an empty string 
        if title == None : #not title empty string
            title = ''
            
        # if option is empty there is no option
        if option == '':
            option = None
            
        #if no message it is an empty string
        if message == None :
            message = ''
         
        # set the menu informations 
        self.name    = name
        self.title   = title        
        self.option  = option
        self.message = message 
        
        # read the menu properties
        # if there is an offset for the left menu margin
        self.margin = 0
        if  dicParam.get('leftMargin') != None :
            self.margin = int (dicParam['leftMargin'])
        # if there is an options offset   
        self.offsetCode = 0
        if  dicParam.get('offsetCode') != None :
            self.offsetCode= int (dicParam['offsetCode'])

        # if there is an options label offset   
        self.offsetLabel = 0
        if  dicParam.get('offsetLabel') != None :
            self.offsetLabel = int (dicParam['offsetLabel'])
        
        # in mode BDD view the properties
        if self.flagBDD :
            print("MENU : ",self.name)
            print("setup înformations :\n-",self.title)
            print("- options")
            if self.option != None:
                for opt in self.option:
                    try:                 
                        print ("  . (",opt[0], ",",opt[1],",",opt[2],")")
                    except:
                        raise ValueError("not valid option !")
            #except:
            #   raise ValueError(" bad option list")

            print ("-", self.message)
            print("setup properties :")
            print("left margin  :",dicParam.get('leftMargin'))
            print("offset code  :",dicParam.get('offsetCode'))
            print("offset label :",dicParam.get('offsetCode'))

    def create(self):
        """ build the screen display and
            store the result in a dictionnary

        """
        scr  =  ""
        mrg = self.margin * " "
        strOC = self.offsetCode  * " "
        strOL = (self.offsetLabel+1) * " "
        if self.title != '' :
            scr += mrg + self.title + "\n"
        if self.option != None :
            # try:
            for opt in self.option:
                try :                
                    ln = mrg + strOC + str(opt[1]) + strOL + opt[0] + "\n"
                except IndexError :
                    scr += "\n"
                    print("option {0} not a valid option in list {1} !".format(opt,self.option))
                    #raise IndexError
                else :
                    scr += ln
                  
           # except:
           #     raise ValueError("error list {0} not valid !".forrmat(self.option))
        scr += mrg  + self.message       
        self.screen[self.name] = scr
        
    def display(self, menuName = 'default'):
        """ return the string created
            in the screen dictionnary 
            to display the menu named
            menuName"""
        if self.screen.get(menuName) != None:
            return  self.screen[menuName] 
        else:
            raise ValueError("error menu name '{0}' not exist!".format(menuName))
            #return None
            
    def show(self, menuName):
        print(self.screen[menuName],end='') 
       
if __name__ == '__main__' :
    print ("\nmenuConsole : init")
    monMenu = menuConsole('menu1',
    	            'The Title menu',
    	            #[
    	             'bad',
    	             #('option n°1', 1,'opt1'),
                  #('option n°2', 2,'opt2')
                 #],
                 'input message : ',
                 leftMargin = 3,
                 offsetCode = 2,
                 offsetLabel =3,
                 flagBDD = False)
    
    print ("\nmenuConsole : create")  
    monMenu.create()
    
    print ("\nmenuConsole : print display")
    print (monMenu.display ('menu1'))
    
    print ("\nmenuConsole : show")
    monMenu.show('menu1')    