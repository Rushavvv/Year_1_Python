from datetime import datetime
from Read import read

def updateFile(fname, availablity, kitta):
    '''
        Updates the availability status of a land record in the specified file.

        Args:
            fname (str): File name or path to the CSV file containing land records.
            availability (str): Updated availability status for the land (e.g., "Available", "Rented").
            kitta (str): Unique identifier (kitta) of the land record to be updated.

        Returns:
            None
    '''

    file = open(fname, 'r')
    lines = file.readlines()    #Reads each line of the file
    file.close

    with open(fname, 'w') as file:  #Open file in 'w' mode
        for line in lines:
            line_data = line.strip().split(',')
            if line_data[0] == kitta:   
                line_data[5] = availablity
                line = ','.join(line_data) + '\n'
            file.write(line)        # Writes in the file


def invoiceRent(rentedLands, id,  duration, name):
    '''
        Generates an invoice for renting land and saves it to a text file.

        Args:
            rentedLands (list): A list of lists containing information about the rented lands.
                                Each inner list contains the following elements:
                                [kitta, city, direction, area, price]
            id (int): The unique identifier (ID) for the transaction.
            duration (int): The duration for which the land is rented.
            name (str): The name of the person renting the land.

        Returns:
            None
    '''
    total = 0 
    #Thank you message
    print("*" * 250 + "\n")
    print(" " * 100 + "Thank you for choosing Kitta for Bitta                         ID: " + str(id) + " " * 100 + 'To: ' + name + "\n")
    print("*" * 250 + "\n")

    with open(name + str(id) + '.txt', 'a') as invoice:  # Open the file in 'a' mode
        invoice.write("*" * 200 + "\n\n")
        invoice.write(" " * 50 + "Thank you for choosing Kitta for Bitta           ID: " + str(id) + " " * 20 + '\t' + 'To: ' + name + '\n\n' )
        invoice.write("*" * 200 + "\n\n")
        
        invoice.write('Kitta' + '\t' * 3 + 'City' + '\t' * 4 + 'Direction' + '\t' * 2 + 'Area' + '\t' * 3 + 'Price' + '\n')

        print('Kitta' + '\t' * 3 + 'City' + '\t' * 3 + 'Direction' + '\t' * 3 + 'Area' + '\t' * 3 + 'Price' + '\n')
        for rentedLand in rentedLands:
            invoice.write(rentedLand[0] + '\t' * 3 + rentedLand[1] + '\t' * 3 + rentedLand[2] + '\t' * 3 + rentedLand[3] + '\t' * 3 + rentedLand[4] + 'NPR' + '\n\n')
            print(rentedLand[0] + '\t' * 3 + rentedLand[1] + '\t' * 3 + rentedLand[2] + '\t' * 3 + rentedLand[3] + '\t' * 3 + rentedLand[4] + 'NPR' + '\n')
            price = int(rentedLand[4])
            total += int(price * duration)

        invoice.write("*" * 200 + "\n")
        invoice.write('\t' * 5 + 'Your total is: ' + str(total) + 'npr \n')
        invoice.write("*" * 200 + "\n")

        print("*" * 250 + "\n\n")
        print('\t' * 5 + 'Your total is: ' + str(total) + 'npr \n\n')
        print("*" * 250 + "\n\n")



def invoiceReturn(rentedLands, id, name , rentDuration, returnDuration):
    '''
        Generates an invoice for returning rented land and saves it to a text file.

        Args:
            rentedLands (list): A list of lists containing information about the rented lands.
                                Each inner list should contain the following elements:
                                [kitta, city, direction, area, price]
            id (int): The unique identifier (ID) for the transaction.
            name (str): The name of the person returning the rented land.
            rentDuration (list): A list containing the duration for which each land was rented.
            returnDuration (list): A list containing the duration for which each land is returned.

        Returns:
            None
    '''
    
    print("*" * 250 + "\n")
    print(" " * 100 + "Thank you for choosing Kitta for Bitta           ID: " + str(id) + " " * 100 + 'To: ' + name + "\n")
    print("*" * 250 + "\n")

    with open(name + str(id) + '.txt', 'a') as invoice:  # Open the file in 'a' mode
        invoice.write("*" * 200 + "\n\n")
        invoice.write(" " * 50 + "Thank you for choosing Kitta for Bitta           ID: " + str(id) + " " * 20 + '\t' + 'To: ' + name + '\n\n' )
        invoice.write("*" * 200 + "\n\n")
        invoice.write('Kitta' + '\t' * 3 + 'City' + '\t' * 3 + 'Direction' + '\t' * 3 + 'Area' + '\t' * 3 + 'Price' + '\t' * 3 + 'Fine' + '\n\n')
        print('Kitta' + '\t' * 3 + 'City' + '\t' * 3 + 'Direction' + '\t' * 3 + 'Area' + '\t' * 3 + 'Price' + '\t' * 3 + 'Fine' + '\n')
        total = 0
        for i in range(len(rentedLands)):

            rentedLand = rentedLands[i]
            rentDue = rentDuration[i]
            returnDue = returnDuration[i]
            extra = returnDue - rentDue 
            fine = 0

            if extra > 0:
                fine = int((int(rentedLand[4]) * int(extra)) * 0.10)
            total += int(rentedLand[4]) * int(returnDue) + fine
            
            invoice.write(rentedLand[0] + '\t' * 3 + rentedLand[1] + '\t' * 3 + rentedLand[2] + '\t' * 3 + rentedLand[3] + '\t' * 3 + rentedLand[4] + 'NPR' + '\t' * 2 + str(fine) + '\n')
            print(rentedLand[0] + '\t' * 3 + rentedLand[1] + '\t' * 3 + rentedLand[2] + '\t' * 3 + rentedLand[3] + '\t' * 3 + rentedLand[4] + 'NPR' + '\t' * 2 + str(fine) + '\n')

        invoice.write("*" * 200 + "\n\n")
        invoice.write('\t' * 5 + 'Your total is: ' + str(total) + 'npr \n\n')
        invoice.write("*" * 200 + "\n\n")

        print("*" * 250 + "\n")
        print('\t' * 5 + 'Your total is: ' + str(total) + 'npr \n')
        print("*" * 250 + "\n")
