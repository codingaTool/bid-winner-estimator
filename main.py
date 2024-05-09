from art import logo
import random
import os

print(logo)
print("Welcome to the highest bidder program")

bidder_dictionary={}
highest_bid_list=[]
highest_bid=0

def collect_bid(bidder_names, bidder_amount):
    bidder_dictionary[bidder_names] = bidder_amount    
    print (bidder_dictionary)
    highest_bid_list.append(bidder_amount)
    
   
def bid_result(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            print(f"The highest bidder is {key} with ${value}")
        
    # If value not found, return None
    return None

# Call the function to clear the screen
def clear_screen():
    os.system('clear')


#To keep the program running until user enters 'restart' options
end_program = False
while not end_program:
    bidder_names = input("Enter bidder name: ")
    bidder_amount = int(input("Enter bidder amount: $"))

    collect_bid(bidder_names, bidder_amount)

    restart = input("Continue program 'Yes' or 'No'").lower()

    
    if restart == 'yes':
        clear_screen()
        continue

    elif restart =='no':
         end_program = True
         print(bidder_dictionary)
         highest_bid= max(highest_bid_list)
         bid_result(dictionary=bidder_dictionary, value=highest_bid)
         print("Goodbye")
        

    else:
        print("Entered wrong action")
        break


        
        
    

    
