## Petals 
## Brigid O'Hara 
## Jan 2025.

## FIX/ADD: choice1 = list 0:10, ask 'see more.' close file when done, return to start
##                  = Instead of list feature, have user input good feeling and return bad from list          
##          choice2 = figure out how user can add multiple entries
##                  = if not, reloop it 'add to list?'

import random 

file_a = 'a.txt'
file_b = 'b.txt'

name = input('Pluck the Daisy. What is your name: ')

print('\n~He loves me \n'
      '     or \n'
       'He loves me not~ \n')
gochoice = input(' ')


if gochoice == 'He loves me':
    print('\n~Do you want to see how little he does?~\n' )
    choice1 = input(' ')

    if choice1 == 'yes':
        print('\n~LISTEN TO YOUR PAST BELIEFS~: \n ')# add list 0:10 , then see more? )
            
        def user_rage_input():
            return input('\n Tell me how you feel:')
        
        def a_b_files(file_a, file_b, text):
            
            with open(file_b, 'a') as file: 
                file.write(text + '\n')

            with open(file_a, 'r') as file:
                lines = file.readlines()
                print(random.choice(lines).strip())
        while True: 
            text = user_rage_input()
            if text.lower() == 'I feel better.': 
                break
            a_b_files(file_a, file_b, text)
        
        
    else:
        print('Oh,' +name + '! How silly, goodbye.')

else:
    print('\n~Much Better. Would you like to add to list?~' )
    choice2 = input(' ')
    
    if choice2 == 'yes':
        add = input('\nAdd:')
        with open('a.txt', 'a') as file:
            file.write(add +'\n')

    else:
        print('goodbye')


     
    
    


      
