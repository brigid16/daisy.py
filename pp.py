## Petals 
## Brigid O'Hara 
## Jan 2025.

## FIX/ADD: choice1 = list 0:10, ask 'see more.' close file when done, return to start
##                  = Instead of list feature, have user input good feeling and return bad from list          
##          choice2 = figure out how user can add multiple entries
##                  = if not, reloop it 'add to list?'

name = input('Pluck the Daisy. What is your name: ')

print('\n~He loves me \n'
      '     or \n'
       'He loves me not~ \n')
gochoice = input(' ')


if gochoice == 'He loves me':
    print('\n~Do you want to see how little he does?~\n' )
    choice1 = input(' ')

    if choice1 == 'yes':
        print('\n~YOUR VERY OWN PAST BELIEFS~: \n ')# add list 0:10 , then see more? )
        with open('a.txt', 'r') as file:
            contents = file.read() 
            print(contents)  
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


     
    
    


      
