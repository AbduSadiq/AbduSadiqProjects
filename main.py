print("Hello There, I'm Abdurrafay's virtual assistant.")

name = input("What may your name be?")

print("Woah, "  + name +  ", that's a new one!")
input("Press enter to continue...")

age = int(input("How old may you happen to be?"))
if 0 <= age < 18:
    print ( "You've got some years ahead of you!")
    input("Press enter to continue...")
elif 18 <= age < 60:
    print ("You're almost an adult, act mature!")
    input("Press enter to continue...")
elif age > 60:
    print ("Don't forget to use your senior discounts!")
    input("Press enter to continue...")
else:
    print ("Be a role model!")
    input("Press enter to continue...")


while True:
    print("Choose an option!")
    print("1)Option 1")
    print("2)Option 2")
    print("3)Option 3")
    print("4)Exit chat")

    choice = input("Make a choice please.")

    if choice == '1':
        print("You chose option 1, this is just a placeholder.")
        break
    elif choice == '2':
        print("You chose option 2, this is just a placeholder.")
        break
    elif choice == '3':
        print("You chose option 3, this is just a placeholder.")
        break
    elif choice == '4':
        print("Have a great day, Goodbye")
        break
    else:
        print("Choice not valid, please try again later.")



