#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# WDang, 2020-Mar-15, modified code
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        add_inventory(cd_id, cd_title, cd_artist, table): -> modified list of CD objects 
        show_inventory(table): -> none
        textList_to_CDlist: -> convert list of CD attributes to list of CD objects
    """
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist


    @staticmethod
    def add_inventory(cd_id, cd_title, cd_artist):
        """create a new CD object based on user inputs

        Args:
            each of the three cd attributes
            
        Returns:    
            the new CD object
        """

        new_cd = CD(cd_id, cd_title, cd_artist)
        return new_cd


    @staticmethod
    def del_inventory(IDDel, table):
        """delete a CD object based on user inputs CD ID

        Args:
            IDDel: user input CD ID for the CD to be deleted
            table: current list of CD objects in memory
            
        Returns:    
            the new list of CD objects
        """

        intRowNr = -1
        blnCDRemoved = False
        for cd in table:
            intRowNr += 1
            if int(cd.cd_id) == IDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

        return table




# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def load_inventory(file_name):
        """Read data from file identified by file_name into a list.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            a list of CD attributes of each CD.
        """
        
        try:
            with open(file_name, 'r') as objFile:
                table = []
                for line in objFile:
                    cd = line.strip().split(',')
                    table.append(cd)
                return table
        # try-except to prevent program crash if specified file can't be found due to such as
        # filename error, file not created, file removed
        except FileNotFoundError:
            print("\n\nFile {} was not found and was not able to be loaded\n".format(file_name))
            # below is necessary otherwise table = None when except is invoked
            # this function won't crash but the future code will crash
            table = [] 
            return table


    @staticmethod
    def save_inventory(lst_Inventory, file_name):

        """Function to manage data ingestion from a list to a file

        Args:
            table: list of CD objects in memory
            file_name: name of file used to save the data to

        Returns:
            None. Create a txt file containing list of CD attributes.
        """        
        
        with open(file_name, 'w') as objFile:
            for cd in lst_Inventory:
                objFile.write("{},{},{}'\n".format(cd.cd_id, cd.cd_title, cd.cd_artist))
                


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Data inputs and outputs

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> None
        user_input_to_add_inventory(table): -> three CD attritutes for user create CD
        get_new_cd_id(table): -> new unused CD ID
        get_typed_input(input_message, error_message): -> correct numerical formatted CD ID input

    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

 
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            print("'{} is not a valid operation".format(choice))
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra line for layout
        return choice


    @staticmethod
    def user_input_to_add_inventory(table):
        """Collect user inputs to add new CDs to inventory

        Args:
            None.

        Returns:
            cd_id (int): ID for the new CD
            cd_title (string): Title for the new CD
            cd_artist (string): Artist of the new CD

        """
        
        cd_id = IO.get_new_cd_id(table)
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, cd_artist

    @staticmethod
    def get_new_cd_id(table):
        """ Gets a new, unused CD ID from the user

        Args:
            table (list of dict): CDInventory

        Returns:
            cd_id (int): New unused CD ID specified by the user
        
        """
        used_ids = []
        for cd in table:
            used_ids.append(cd.cd_id)
        
        while True:
            cd_id = IO.get_typed_input('Enter a numerical ID: ', 'The entered ID is not an integer. Please enter a number')
            if cd_id in used_ids:
                print("CD ID '{}' already exsits, use a different ID\n".format(cd_id))
            else:
                return cd_id


    @staticmethod
    def get_typed_input(input_message, error_message):
        """Prompts the user for input and checks for the correct type.

        Prompts the user for input value of the int type displaying input_message.
        Checks for correct input type, looping until a proper type is entered
        and displays the passed error_message if bad input is passed.

        Args:
            input_message (string): Message displayed to the user prompting for input
            error_message (string): Error message displayed to the user if an incorrect type is entered

        Returns:
            typed_value (int): Int value entered by the user
        
        """

        while True:
            try:
                typed_value = int(input(input_message).strip())
                return typed_value
            except ValueError:
                print(error_message)


    @staticmethod
    def show_inventory(table):
        """Displays CD objects in memory, only shows the attributes  

        Args:
            table: list of CD objects in memory.

        Returns:
            None.
        """

        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')

        for cd in table:
            print('{}\t{}\t (by:{})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))

    @staticmethod
    def textlist_to_CDlist(table):
        """Convert list of CD attributes strings read from saved file to list of CD objects

        Args:
            table: list of CD attributes read from saved file.

        Returns:
            table: list of CD objects.
        """

        cd =[]
        for line in table:
            cd_id, cd_title, cd_artist = line
            cd.append(CD(cd_id, cd_title, cd_artist))
        return cd


# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
    # let user delete data from the inventory (added by WDang)

def main():

    # 1. When program starts, read in the currently saved Inventory, convert CD attributes to CD objects
    lstOfCDObjects = FileIO.load_inventory(strFileName)
    # print(lstOfCDObjects) # print list of strings of attributes of CDs in inventory
    lstOfCDObjects = IO.textlist_to_CDlist(lstOfCDObjects)
    # print(lstOfCDObjects) # print list of CD object after the conversion on line 303
    
    # 2. start main loop
    while True:
        # 2.1 Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
    
        # 3. Process menu selection
        # 3.1 process exit first
        if strChoice == 'x':
            print('Goodbye!')
            break

        # 3.2 process load inventory
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                lstOfCDObjects = FileIO.load_inventory(strFileName)
                lstOfCDObjects = IO.textlist_to_CDlist(lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)

            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        # 3.3 process add a CD
        elif strChoice == 'a':
            # 3.3.1 Ask user for new ID, CD Title and Artist and add to CD inventory table
            cd_id, cd_title, cd_artist = IO.user_input_to_add_inventory(lstOfCDObjects)
            lstOfCDObjects.append(CD.add_inventory(cd_id, cd_title, cd_artist))
            # 3.3.2 Display the updated inventory list
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        # 3.4 process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        # 3.5 process delete a CD, note not in the scope of this assignment
        elif strChoice == 'd':
            IO.show_inventory(lstOfCDObjects)
        # 3.5.2.1 get user input for which CD to delete
        # 3.5.2 2 search thru table and delete CD if found
            intIDdel = IO.get_typed_input('Which ID would you like to delete? ', "ID is not valid, please enter an interger value.")
            CD.del_inventory(intIDdel, lstOfCDObjects)
        # 3.5.3 display updated Inventory to user
            IO.show_inventory(lstOfCDObjects)

            continue  # start loop back at top.
        # 3.6 process save inventory to file
        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save CD objects attriutes as strings
                FileIO.save_inventory(lstOfCDObjects, strFileName)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.
        # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
        else:
            print('General Error')


# start main program

main ()



