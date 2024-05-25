from datetime import datetime
from Read import read
from Write import *
def welcome():
    '''
        Prints a welcome message for the Kitta for Bitta system.

        Displays the program name, contact information, and a welcome message.

        Returns:
            None
    '''

    #Welcome Message
    print("*" * 250 + "\n")
    print(" " * 160 + "Kitta for Bitta" + " " * 125 + "\n")
    print("*" * 250)
    print(" " * 90 + "Budhanilkantha, Kathmandu" + " " * 60 + "9861595991")
    print("*" * 250 + "\n")
    print(" " * 150 + "Welcome to Kitta for Bitta" + " " * 125 + "\n")
    print("*" * 250 + "\n")

def items():
    '''
        Displays the available land items for rent.

        Reads land information from a file and prints details of available lands.

        Returns:
            None
    '''

    landList = read('info.txt') #Uses read() from Read.py
    print("*" * 250 + "\n")
    print('Kitta' + '\t' * 3 + 'City' + '\t' * 3 + 'Direction' + '\t' * 3 + 'Area' + '\t' * 3 + 'Price'  + '\t' *3 + 'Status' + '\n')
    for land in landList:
        if 'Available' in land[5]:
            print(land[0] + '\t' * 3 + land[1] + '\t' * 3 + land[2] + '\t' * 3 + land[3] + '\t' * 3 + land[4] + 'NPR' + '\t' *2 + land[5] + '\t' + '\n')
    print("*" * 250 + "\n")

def rent(name, number):
    '''
        Allows a user to rent a land item.

        Prompts the user to select a land item by its kitta number and rent duration.
        Updates the file to mark the selected land item as 'Not Available' (rented).
        Generates an invoice for the rent transaction.

        Args:
            name (str): The name of the person renting the land.
            number (int): The contact number of the person renting the land.

        Returns:
            None
    '''
    filename = 'info.txt'
    landList = read(filename)   #Uses read() from Read.py
    now = int(datetime.now().timestamp())
    id = number + now
    rentedLands = []
    items()
    while True:
        exists = False
        kitta = input('Enter the kitta number of the land you want to rent: ')
        if int(kitta) < 0:            #For Negative values             
            print('Negative Kitta numbers do not exist')
        else:
            duration = int(input('Enter the duration you want to rent it for (in months): '))
            for lands in landList:
                if kitta == lands[0]:
                    exists = True
                    if lands[5] == ' Available':
                        lands[5] = ' Not Available'     #Updating the status
                        availability = ' Not Available'
                        rentedLands.append(lands)
                        updateFile(filename,availability, kitta)
                        print('Rented Successfully')
                    else:
                        print('This land is already on rent')
            if exists == False:             # For kittas that are not in the file 
                print('Kitta doesnt exist')
        choice = input('Do you want to continue? (y/n): ')
        try:
            if choice.lower() != 'y':
                invoiceRent(rentedLands, id, duration, name)
                break
        except:
            raise ValueError

                

def returns(name, number):
    '''
        Allows a user to return a rented land item.

        Prompts the user to select a rented land item by its kitta number.
        Updates the file to mark the selected land item as 'Available' (returned).
        Calculates any fines incurred based on the return duration.
        Generates an invoice for the return transaction.

        Args:
            name (str): The name of the person returning the land.
            number (int): The contact number of the person returning the land.

        Returns:
            None
    '''
    filename = 'info.txt'
    landList = read(filename)
    now = int(datetime.now().timestamp())
    id = number + now 
    returnedLands = []
    rentDuration = []
    returnDuration = []
    items()
    while True:
        exists = False
        kitta = input('Enter the kitta of the land you want to return: ')
        if int(kitta) < 0:      # For negative kitta
            print('Negative Kitta numbers do not exist')
        else:
            rentD = int(input('Enter the amount of months you originally rented it for: '))
            returnD = int(input('Enter the amout of months you actually rented it for: '))
            rentDuration.append(rentD)
            returnDuration.append(returnD)
            for lands in landList:
                if kitta == lands[0]:
                    exists = True
                    if lands[5] == ' Not Available':
                        lands[5] = ' Available'             #Updating the status
                        availability = ' Available'
                        returnedLands.append(lands)
                        updateFile(filename,availability,kitta)
                        print('Returned Successfully.....')
                    else:
                        print('The land is already in the system')
            if exists == False:     # For Kittas not in the file 
                print('Kitta does not exist')
        choice = input('Do you want to continue? (y/n): ')
        try:
            if choice.lower() != 'y':
                invoiceReturn(returnedLands, id, name, rentDuration, returnDuration)
                break
        except:
            raise ValueError