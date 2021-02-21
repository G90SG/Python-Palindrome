#Explaining the aim of the program to the user
print("Please give me a word and I'll tell you if it's a Palindrome. ")
#Asking the user to input a  assigning it to the Variable Word and categorising as a string
word = str(input("What is your chosen word? "))
# Reversal of the input
reverse = "".join(reversed(word)) 
# Check whether the input is equal to it's reverse or not and this determines whether it is a Palindrome
if(word == reverse): 
    print("Yes, the word " +word+ " is palindrome.")
else:
    print("No, the word " +word+ " is not a palindrome.")
