# importing the module 
import sys 
  
# this function will be the first to run as soon as the main function executes 
def initial_phonebook(): 
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
      
    # We are collecting the initial number of contacts the user wants to have in the 
    # phonebook already. User may also enter 0 if he doesn't wish to enter any. 
    phone_book = [] 
    print(phone_book) 
    for i in range(rows): 
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1)) 
        print("NOTE: * indicates mandatory fields") 
        print("....................................................................") 
        temp = [] 
        for j in range(cols): 
                      
        # We have taken the conditions for values of j only for the personalized fields 
        # such as name, number, e-mail id, dob, category etc 
            if j == 0: 
                temp.append(str(input("Enter name*: "))) 
                  
                # We need to check if the user has left the name empty as its mentioned that 
                # name & number are mandatory fields. 
                # So implement a condition to check as below. 
                if temp[j] == '' or temp[j] == ' ': 
                    sys.exit( 
                        "Name is a mandatory field. Process exiting due to blank field...") 
                    # This will exit the process if a blank field is encountered. 
                      
            if j == 1: 
                temp.append(int(input("Enter number*: "))) 
                # We do not need to check if user has entered the number because int automatically 
                # takes care of it. Int value cannot accept a blank as that counts as a string. 
                # So process automatically exits without us using the sys package. 
                  
            if j == 2: 
                temp.append(str(input("Enter e-mail address: "))) 
                # Even if this field is left as blank, None will take the blank's place 
                if temp[j] == '' or temp[j] == ' ': 
                    temp[j] = None
                      
            if j == 3: 
                temp.append(str(input("Enter date of birth(dd/mm/yy): "))) 
                # Whatever format the user enters dob in, it won't make a difference to the compiler 
                # Only while searching the user will have to enter query exactly the same way as 
                # he entered during the input so as to ensure accurate searches 
                if temp[j] == '' or temp[j] == ' ': 
                                      
                # Even if this field is left as blank, None will take the blank's place 
                    temp[j] = None
            if j == 4: 
                temp.append( 
                    str(input("Enter category(Family/Friends/Work/Others): "))) 
                # Even if this field is left as blank, None will take the blank's place 
                if temp[j] == "" or temp[j] == ' ': 
                    temp[j] = None
                      
        phone_book.append(temp) 
        # By this step we are appending a list temp into a list phone_book 
        # That means phone_book is a 2-D array and temp is a 1-D array 
      
    print(phone_book) 
    return phone_book 
  
def menu(): 
    # We created this simple menu function for 
    # code reusability & also for an interactive console 
    # Menu func will only execute when called 
    print("********************************************************************") 
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False) 
    print("********************************************************************") 
    print("\tYou can now perform the following operations on this phonebook\n") 
    print("1. Add a new contact") 
    print("2. Remove an existing contact") 
    print("3. Delete all contacts") 
    print("4. Search for a contact") 
    print("5. Display all contacts") 
    print("6. Exit phonebook") 
  
    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6 
    # We return the entered choice to the calling function wiz main in our case 
    choice = int(input("Please enter your choice: ")) 
      
    return choice 
  
def add_contact(pb): 
    # Adding a contact is the easiest because all you need to do is: 
    # append another list of details into the already existing list 
    dip = [] 
    for i in range(len(pb[0])): 
        if i == 0: 
            dip.append(str(input("Enter name: "))) 
        if i == 1: 
            dip.append(int(input("Enter number: "))) 
        if i == 2: 
            dip.append(str(input("Enter e-mail address: "))) 
        if i == 3: 
            dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 
        if i == 4: 
            dip.append( 
                str(input("Enter category(Family/Friends/Work/Others): "))) 
    pb.append(dip) 
    # And once you modify the list, you return it to the calling function wiz main, here. 
    return pb 
  
def remove_existing(pb): 
    # This function is to remove a contact's details from existing phonebook 
    query = str( 
        input("Please enter the name of the contact you wish to remove: ")) 
    # We'll collect name of the contact and search if it exists in our phonebook 
      
    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp. 
      
    for i in range(len(pb)): 
        if query == pb[i][0]: 
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope 
              
            print(pb.pop(i)) 
            # The pop function removes entry at index i 
              
            print("This query has now been removed") 
            # printing a confirmation message after removal. 
            # This ensures that removal was successful. 
            # After removal we will return the modified phonebook to the calling function 
            # which is main in our program 
              
            return pb 
    if temp == 0: 
        # Now if at all any case matches temp shoul've incremented but if otherwise, 
        # temp will remain 0 and that means the query does not exist in this phonebook 
        print("Sorry, you have entered an invalid query.\Please recheck and try again later.") 
          
        return pb 
  
def delete_all(pb): 
    # This function will simply delete all the entries in the phonebook pb 
    # It will return an empty phonebook after clearing 
    return pb.clear() 
  
def search_existing(pb): 
    # This function searches for an existing contact and displays the result 
    choice = int(input("Enter search criteria\n\n\1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\ \nPlease enter: ")) 
    # We're doing so just to ensure that the user experiences a customized search result 
      
    temp = [] 
    check = -1
      
    if choice == 1: 
    # This will execute for searches based on contact name 
        query = str( 
            input("Please enter the name of the contact you wish to search: ")) 
        for i in range(len(pb)): 
            if query == pb[i][0]: 
                check = i 
                temp.append(pb[i]) 
                  
    elif choice == 2: 
    # This will execute for searches based on contact number 
        query = int( 
            input("Please enter the number of the contact you wish to search: ")) 
        for i in range(len(pb)): 
            if query == pb[i][1]: 
                check = i 
                temp.append(pb[i]) 
                  
    elif choice == 3: 
    # This will execute for searches based on contact's e-mail address 
        query = str(input("Please enter the e-mail ID\of the contact you wish to search: ")) 
        for i in range(len(pb)): 
            if query == pb[i][2]: 
                check = i 
                temp.append(pb[i]) 
                  
    elif choice == 4: 
    # This will execute for searches based on contact''s date of birth 
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\of the contact you wish to search: ")) 
        for i in range(len(pb)): 
            if query == pb[i][3]: 
                check = i 
                temp.append(pb[i]) 
                  
    elif choice == 5: 
    # This will execute for searches based on contact category 
        query = str( 
            input("Please enter the category of the contact you wish to search: ")) 
        for i in range(len(pb)): 
            if query == pb[i][4]: 
                check = i 
                temp.append(pb[i]) 
        # All contacts under query category will be shown using this feature 
          
    else: 
    # If the user enters any other choice then the search will be unsuccessful 
        print("Invalid search criteria") 
        return -1
    # returning -1 indicates that the search was unsuccessful 
      
    # all the searches are stored in temp and all the results will be displayed with 
    # the help of display function 
      
    if check == -1: 
        return -1
        # returning -1 indicates that the query did not exist in the directory 
    else: 
        display_all(temp) 
        return check 
        # we're just returning a index value wiz not -1 to calling function just to notify 
        # that the search worked successfully 
  
# this function displays all content of phonebook pb 
def display_all(pb): 
    if not pb: 
    # if display function is called after deleting all contacts then the len will be 0 
    # And then without this condition it will throw an error 
        print("List is empty: []") 
    else: 
        for i in range(len(pb)): 
            print(pb[i]) 
  
def thanks(): 
# A simple gesture of courtesy towards the user to enhance user experience 
    print("********************************************************************") 
    print("Thank you for using our Smartphone directory system.") 
    print("Please visit again!") 
    print("********************************************************************") 
    sys.exit("Goodbye, have a nice day ahead!") 
  
# Main function code 
print("....................................................................") 
print("Hello dear user, welcome to our smartphone directory system") 
print("You may now proceed to explore this directory") 
print("....................................................................") 
# This is solely meant for decoration purpose only. 
# You're free to modify your interface as per your will to make it look interactive 
  
ch = 1
pb = initial_phonebook() 
while ch in (1, 2, 3, 4, 5): 
    ch = menu() 
    if ch == 1: 
        pb = add_contact(pb) 
    elif ch == 2: 
        pb = remove_existing(pb) 
    elif ch == 3: 
        pb = delete_all(pb) 
    elif ch == 4: 
        d = search_existing(pb) 
        if d == -1: 
            print("The contact does not exist. Please try again") 
    elif ch == 5: 
        display_all(pb) 
    else: 
        thanks() 