from Read import read
from Operations import *

def main():
    '''
        Executes the main functionality of the program.

        The program starts by displaying the welcome message to the user and prompting for their name and phone number.
        Then, it gives the user choices to choose from:
            - Rent land
            - Return land
            - Exit the program
        The user is prompted to input the operation they want to perform, and the program executes
        the corresponding operation. If the user inputs an invalid operation, they are prompted again.
        The program continues in a loop until the user chooses to exit (3).

        If the user's phone number is not 10 digits long, they are prompted to input a valid number.
        If the user inputs any character other than digits in the phone number, an error message is displayed.

        Returns:
            None
    '''
    welcome()

    try:

        name = input('Enter your name: ')   #Prompts User's name
        number = int(input('Enter your number: '))  #Prompts User's phone number

        if len(str(number)) == 10:

            looping = True
            while looping:
                try:
                    print("*" * 250 + "\n")
                    print("Below are the operations you can perform" + "\n") 
                    print("Press 1 to Rent land")
                    print("Press 2 to Return Land")
                    print("Press 3 to Exit" + "\n")
                    print("*" * 250 + "\n")

                    userIn = input("Enter the operation you want to perform: ")
                    if userIn > '3' or userIn < '1':    #For values that are not in the options
                        raise ValueError
                    else: 
                        if userIn == '1':
                            rent(name,number)
                        elif userIn == '2': 
                            returns(name,number)
                        else: 
                            print('Thank you for choosing Kitta for Bitta')
                            break
                except ValueError:
                    print('\n Please enter a valid input \n')
        else:
            print('Input a valid number')
            

    except:
        print('Number should not contain any other characters')
main()