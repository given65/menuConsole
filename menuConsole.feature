feature :

In order To :    
      quickly write a menu in a console program

I want to 
     use an object menu that manage 
         the display of options menu
     and
         the choice input of the user
     and
         with a simple setup
     and 
         without write a module management

As a :
     software developper

Scenario :  I created a menu in my code 
As given :
      I'm writing a module
When
      I need a new menu
Then
      I code the instanciation of an object menu
   and
       set up its display with the following informations  :
          -  Title
          -  List of option labels with their
                 -  input code 
                 -  return code
          - Input message
        and  the presentation parameters
           - underline titre
           - marging menu
           - return lines before options
           - offset options
           - input code type (nteger or letters)
           - input code alignment (left or right)
           - return lines after options 
           - underline options
           - return lines after message

exemple 1 : instanciate a menu without parameters 
            var = menuObject(
                    'the Title Menu',
                    (
                     ('option n°1', 1, 'opt1'),
                     ('option n°2', 2, 'opt2')
                    ),
                    'input Message :')
            
exemple 2 : instanciate a menu with parameters


Scenario : display a menu
As given :
     I created a menu in my code
When
     the code is running
  and
    the show instruction of menu is executed 
then
    the menu is displaying with
    title
    options code and label
    input message

exemple 1 : instanciate without parameters
            with value "exemple 1"
            of scenario "create a menu"
     """
     |the Title menu
     |1 option n°1
     |2 option n°2
     |input Message :