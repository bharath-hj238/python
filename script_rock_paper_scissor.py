import random

decision = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
'----(___)
'''
]

decision_list = [0, 1, 2]
print("\nWelcome to Rock-Paper-Scissor\n")

user_choice = int(input("\nChoose an option: Rock[1] Paper[2] Scissor[3]: ")) - 1

print(decision[user_choice])

computer_choice = int(random.choice(decision_list))

print("\n Computer Chose: ")
print(decision[computer_choice])
print("\n")

if user_choice > 3:
    print("You Lose")
elif user_choice == computer_choice:
    print("Its a draw")
elif user_choice == computer_choice:
    print("Its a draw")
elif user_choice > computer_choice:
    print("You Win")
elif user_choice < computer_choice:
    print("You Lose")
else:
    print("You Lose")


