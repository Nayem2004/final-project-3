#The purpose of the import os is to import
#necessary modules into the program.
#os is used to clear the console screen for system 
#dependent functionality.
import os 
#the datetime tool is to work with the date and time
from datetime import datetime
#this function Clears the console screen for a cleaner display.
def clear_screen():
    #uses the os module to exectute platform specific commands
    #the "cls" is for Windows and "clear" for Linux
    os.system('cls' if os.name == 'nt' else 'clear')
#This function gets customer name and 
#address as input from the user.
def get_customer_information():
    #prompts the user for input and returns the entered values.
     print("Enter Customer Information:")
     customer_name = input("Customer Name: ")
     customer_address = input("Customer Address: ")
     date = input("What is today's date? MM/DD/YY")
     return customer_name, customer_address, date
#This function displays the customer information on the console.
def display_customer_information(name, address, date):
    #Takes "name" and "address" as parameters and prints them.
     print("\nCustomer Information:")
     print("Name:", name)
     print("Address:", address)
     print("Date:", date)
#This function gets the user's preference 
# for receiving notifications.
def get_notification_preference():
    preference = input("Do you want to receive notifications? (yes/no): ").lower()
    return preference == 'yes'
    #Asks the user whether they want notifications 
    #and returns a boolean value.

#This function Allows the user to choose the output format 
# (simple or detailed).
def get_output_format():
    print("Choose Output Format:")
    print("1. Simple")
    print("2. Detailed")
    choice = input("Enter your choice (1/2): ")
    return 'Detailed' if choice == '2' else 'Simple'
    #Presents options to the user and returns the selected format.

#This fuction is used to calculate 
# the electric bill based on the number of 
# kWh used and the electric rate.
def calculate_electric_bill(kwh_used, electric_rate):
    return kwh_used * electric_rate
    #Multiplies 'kwh_used' by 'electric_rate' 
    # and returns the result.

#This function is used to calculate the gas bill 
# based on the number of therms used and the gas rate.
def calculate_gas_bill(therms_used, gas_rate):
    return therms_used * gas_rate
    #Multiplies 'therms_used' by 'gas_rate' 
    # and returns the result.

#This function is used to append data 
# to the specified file (filename) and saves it.
def save_to_file(filename, data):
     with open(filename, 'a') as file:
          file.write(data)
     #Opens the file in append mode and writes the data.

#This function is used to displays the month-to-month  
#history from the specified file. To read the file 
# in Visual Studio
def  display_history(filename):
    #Opens the file in read mode and prints its content.
    with open(filename, 'r') as file:
        history = file.read()
        print("\nMonth-to-Month Usage History:")
        print(history)


#This is the main function orchestrating the program flow 
# and where most of the information is returning from
def main():
    print("Utility Company Bill Calculator")
    #Prints a title to identify the program.


    # Set up file for month-to-month comparison
    filename = "utility_bills.txt" #Checks if the file 
    #"utility_bills.txt" exists.
    if not os.path.exists(filename):
        with open(filename, 'w'):
            #forces the program to skip, if there already is a file named utility_bills.txt
             pass #(is a no operation)
    #If not, it creates the file in write mode 
    #pass 

    # Get and display customer information
    customer_name, customer_address, date = get_customer_information()
    #Calls the 'get_customer_information()' function to 
    # get customer name and address
    display_customer_information(customer_name, customer_address, date)
    #Calls the 'display_customer_information()' 
    # function to print the customer information.


    # Additional features
    #Calls functions to get additional user 
    # preferences:
    #get_notification_preference() 
    #Asks the user whether they want to 
    # receive notifications.
    receive_notifications = get_customer_information()
    #get_output_format() 
    # Asks the user to choose the output format 
    # (simple or detailed).
    output_format = get_output_format()
    receive_notifications, output_format
    
    #This while loop is responsible for continuously 
    #presenting the main menu to the user.
    while True:
        clear_screen()
        print("1. Calculate Bill")
        print("2. View Month-to-Month History")
        print("3. View Settings")
        print("4. Exit")

        #This input is responsible for allowing the user 
        # to chose the option they want for the menu choice
        choice = input("Enter your choice (1/2/3/4): ")

        #If statements below is a consequence for the user input
        #above
        if choice == '1':
            clear_screen()
            print("Calculate Bill")
        #If the user chooses option 1, 
        # it clears the screen and displays a message.

        elif choice == '2':
            clear_screen()
        #If the user chooses option 2, it clears the screen, 
        #displays the month-to-month history, 
        # and will ask the user to press Enter to continue.

        elif choice == '3':
            # Display extended settings menu
            clear_screen()
            print("Settings Menu")
            print("1. Change Notification Preferences")
            print("2. Change Default Rates")
            print("3. Choose Output Format")
            print("4. Back to Main Menu")
        #If the user chooses option 3, it clears the screen and 
        #displays an extended settings menu.
             
            #settings menu
            #The user will enter an option to explore
            #This line takes user input for the settings menu.
            setting_choice = input("Enter your choice (1/2/3/4): ")
            #If the user chooses option 1, 
            #it calls get_notification_preference() 
            # to change the notification preferences.
            if setting_choice == '1':
                receive_notifications = get_notification_preference()
             #If the user chooses option 2, 
            # it is a placeholder for changing the default rates.
            elif setting_choice == '2':
                # Add functionality to change default rates
                #forces the program to skip, if option 2 wasn't selected
                pass #(allows you to)
            #If the user chooses option 3, 
            #it calls get_output_format() 
            #to change the output format.
            elif setting_choice == '3':
                output_format = get_output_format()

            
            #If the user chooses option 4, it continues to 
            #the main menu and handles invalid choices 
            #with an appropriate error message.
            
            #Return to the main menu
            elif setting_choice == '4':
                #forces the program to continue to the next line of code
                 continue
            #incase the user typed in an option not stated
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                input("Press Enter to continue...")
        
        #meant to end the service by the user
        #If the user chooses option 4, clears the screen, 
        # prints a goodbye message, and exits the program
        elif choice == '4':
            clear_screen()
            print("Goodbye!")
            #break is used to end the loop instead of it continuing
            break
        #incase the user typed in an option not stated
        #it will give an error and will ask you to press enter
        #to continue
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue...")



         # Electric service input 
         #Uses a try-except block to handle potential errors 
         #during user input. It attempts to get user input 
         # for electric service rates and usage. If the conversion 
         #To the float fails, it catches a ValueError 
         # and provides an error message.
        try:
            electric_rate = float(input("Enter electric rate per kWh: $"))
            kwh_used = float(input("Enter the number of kWh used: "))
            
        #Incase the user enters an invalid electrical rate or kwh
        except ValueError:
            print("Invalid input. Please enter numeric values for electric service.")
            input("Press Enter to continue...")
            #forces the program to continue to the next line of code
            continue


         # Gas service input
         #Similar to the electric service input, The gas service 
         #input uses a try-except block to handle potential errors 
         #during user input for gas service rates and therms usage.
        try:
            gas_rate = float(input("Enter gas rate per therm: $"))
            therms_used = float(input("Enter the number of therms used: "))
            
        #incase the user enters an ivalid gas rate or therm
        except ValueError:
            print("Invalid input. Please enter numeric values for gas service.")
            input("Press Enter to continue...")
            #forces the program to continue to the next line of code
            continue


        # Calculate total bill
        #Uses the calculate_electric_bill() and 
        # calculate_gas_bill() functions to calculate 
        # the electric and gas bills
        #Sums the electric and gas bills to get the total bill.
        electric_bill = calculate_electric_bill(kwh_used, electric_rate)
        gas_bill = calculate_gas_bill(therms_used, gas_rate)
        total_bill = electric_bill + gas_bill


        # Display and save to file
        #Prints the calculated bills on the screen.
        #Saves the data (timestamp, customer 
        #information, usage, and total bill) 
        #to a text file for month-to-month comparison.
        print("\nElectric Bill: ${:.2f}".format(electric_bill))
        print("Gas Bill: ${:.2f}".format(gas_bill))
        print("Total Bill: ${:.2f}".format(total_bill))


        # Save data to a text file for month-to-month comparison
        #The now variable is meant to show the current bill and how that'll look compared to others
        now = datetime.now()
        #formatted date variable is meant for the user to compare previous bills to the current one
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") 
        #data to save variable is meant to store all bills both current and old
        data_to_save = f"{formatted_date} - {customer_name}, {customer_address}, {date}, {kwh_used} kWh, {therms_used} therms, ${total_bill:.2f}\n"
        #sends the filename and data to save variables to the save to files function
        save_to_file(filename, data_to_save)

        
        input("\nPress Enter to continue...")
#Makes transfering into the text file easier, '__name__' being the file
if __name__ == "__main__":
    main()
    
        

    



  





 

     
   