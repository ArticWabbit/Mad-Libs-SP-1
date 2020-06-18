import os
os.system("cls")

# Home Text
print("\u001b[32mA Mad Libs Game~\n")
print("Enter the following-\n")

# User Input Section
verb = input("Verb: ")
verb1 = input("Another verb: ")
verb2 = input("Verb: ")
verb3 = input("Another verb: ")
verb4 = input("Verb: ")

adjective = input("Adjective: ")
adjective1 = input("Another adjective: ")
adjective2 = input("Yup, need another one: ")
adjective3 = input("Keep em comin': ")
adjective4 = input("Last one: ")

noun = input("Noun: ")
noun1 = input("Noun: ")

# Next Line and Color
print("\n\u001b[35m")

# Mad Libs Generator
print("Another hour passes as I " + verb + " and " + verb1 + " my post.")
print("Do my " + adjective + " eyes deceive me? Is that an upvote?")
print("After refreshing the page " + adjective1 + " times, this was a " + adjective2 + "\nsight")
print("\"Wow!\" I say.\" " + adjective3 + " Steem Dollars (SBD)! " + verb2 + " you\n whales!\"")
print("I close my browser tab as I " + verb3 + " about Steemit")
print("\"I might not be an anarchist, but at least I've got my " + noun + " posts!\"")
print("Feeling " + adjective4 + ", I decide to take a break from Steemit, and head \ninto the kitchen to make a cup of "
      + noun1)
print("\"I can't believe it happened again! After all the " + verb4 + " I did when writing my post...\"\n")

# Exit Method
input('Press ENTER to exit')
