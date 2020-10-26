#Explaining the aim of the program to the user#
print("Please give me a word and I'll tell you if it's a Palindrome. ")

#Asking the user to input a word#
word = str(input("What is your chosen word? "))
reverse = "".join(reversed(word)) 
#reversal of the input
#check whether the input is equal to it's reverse or not
if(word == reverse): 
    print("Yes, the word " +word+ " is palindrome.")
else:
    print("No, the word " +word+ " is not a palindrome.")