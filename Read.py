
def read(fname):
    '''
        Reads data from a CSV (comma separated values) file containing land details.
        
        Arguments:
            fname (str): Name of the file to be read.
            Returns:  
            list: A list of lists that has land information. Each inner list has information about lands,
              with the following elements:
              - kitta (str): Unique id for a land.
              - city (str): City where the land is located.
              - direction (str): Direction of the land (e.g., north, south).
              - area (str): Area of the land.
              - price (str): Price of the land.
              - status (str): Availability of the land. 

        Raises:
            FileNotFoundError: If the specified file cannot be found.

    '''
    land = []
    try:
        with open(fname,'r') as file: #Opens given file as 'file
            for value in file: 
                data = value.strip().split(',')
                kitta, city, direction, area, price, status = data
                information = [kitta, city, direction, area, price, status]
                land.append(information)
        return land
    except FileNotFoundError:
        print("The file " + fname + " cannot be found")
        return []
