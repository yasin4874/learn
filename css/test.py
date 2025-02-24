# import random
# '''
# random game of numbers: (3) num 7 win 

# '''
# PRICE = '2'
# def generate_num():
#     weight = (1,1,1,1,1,1,1,1,1,1) 
#     num = random.choices([1,2,3,4,5,6,7,8,9,0] ,weights=weight ,k=3)
#     slot_num = num
#     return slot_num

# user = input("How many of money do you have? ").rstrip()
# while True:
#     if user.isdigit():
#         if user >= PRICE:
#             try:
#                 print("which game do you wanna play:\n1-slot game 's'. price: $2.\n2-gambling 'g'. price: $1000")
#                 game = input ("Enter your game: ").lower()                
#             except Exception:
#                 print("Please choose a game in our list.")
#                 continue
#             input('Enter to start gambling.....')
#             slot_game = generate_num()
#             print(slot_game)
#             if slot_game[0] and slot_game[1] and slot_game[2] == '7':
#                 print("congratulations! you win")
#         else:
#             print("Sorry! you dont have enough money.")
#             break
#     else:
#         continue
#         print("Enter a digit number")

import numpy as np

my_list = [12,21,12]
oh = [1,2,3]
array_1 = np.array(my_list)
array_2 = np.array(oh)
print(np.dot(array_1 , array_2))