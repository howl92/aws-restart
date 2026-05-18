#Working with conditionals
userReply = input("Do you need to ship a package? (Enter yes or no)")

if userReply.lower() == "yes":
    print("we can help you ship the package!")
else:
    print("Please come back when you need to ship a package. Thank you")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope or copy)")
if userReply.lower() == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply.lower() == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply.lower() == "copy":
    copies = input("How many copies would you like? (Enter a number)")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again")
    
# def question():
# userReply = input("Please enter yes or no: ")
# if userReply.lower() == "yes":
# print("User says yes")
# elif userReply.lower() == "no":
# print("User says no")
# else:
# print("Invalid input. Try again!")
# question() #Recursive function

# question()