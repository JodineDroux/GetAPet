

def GetAPet() :   
    num = input('Pick a number between 1 and 4\n')
    if num == int(1):
        color = input('Red or Blue\n')
        if color == 'Red':
            print('Unicorn')
        else:
            print('Gryphon')
        
    if num == '2':
        color = input('Pink or Purple\n')
        if color == 'Pink':
            print('Phoenix')
        else:
            print('Dragon')

    if num == '3':
        color = input('Green or Yellow\n')
        if color == 'Green':
            print('Harpy')
        else:
            print('Chymera')    
    
    if num == '4':
        color = input('Magenta or Orange\n')
        if color == 'Magenta':
            print('Pegasus')
        else:
            print('Hippogryph')

    again = input('Do you want to try again?\n Y or N\n')
    
    if again == 'Y':
        GetAPet()
    else:
        print('Thanks for playing')
        
GetAPet()


    