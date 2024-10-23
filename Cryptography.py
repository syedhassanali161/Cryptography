#* ***********************************************************************
# Hassan Ali
# Assignment 1: Cryptography
# Computer Science 20 Block 3
# April 21, 2021

# This program is my own work - H.A.


alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Please enter the message that you would like to cypher: ")


#This counts how many words the message has by counting how many spaces are in the message
counter = 0
for i in message:
    if i == " ":
        counter += 1

#This is a while loop that runs when there are more than 5 words
while counter > 5:
    counter = 0
    message = input("Please enter only a maximum of five words: ")
    for i in message:
        if i == " ":
            counter += 1

#This part of the program takes in the key and uses if statements and a while loop to make sure that the key is a postitive integer number
key = input("Please enter a number for the letter shift: ")
if key.isnumeric() == True:
    key = int(key)
elif key.isnumeric() == False:
    while key.isnumeric() == False:
        key = input("please enter a positive integer number for the key: ")
        if key.isnumeric() == True:
            key = int(key)
            break

#These are the strings that are going to be added to based on what the user enters
encrypted_string = ""
decrypted_string = ""



for i in message:
    #if the letter is a letter and it is lower case
    if i.isalpha() == True and i.islower() == True:
        num = alphabet.find(i) #find the letter in the lowercase alphabet list
        real_num = num + key #shift the number of the key
        real_real_num = real_num % 26 #the number is then modulared to make sure that it does not exceed the length of the alphabet string
        encrypted_string += alphabet[real_real_num] #add the letter to the encrypted string
    elif i.isupper() == True:
        #the same code as above is ran except the letter is searched for in the capitalized list
        num = cap_alphabet.find(i)
        real_num = num + key
        real_real_num = real_num % 26
        encrypted_string += alphabet[real_real_num]
    elif i.isalpha() == False:
        #if the index of the string is not a letter, then it is just added as so to the encrypted string
        encrypted_string += i

#printing the encrypted string
print("The encrypted message is: " + encrypted_string)


#checking with the user if they want to decrypt the message
yesorno = input("Would you like to decrypt this message(y/n): ")


#this while loop runs when the user does not enter one of the two options available
while yesorno != "y" and yesorno != "n":
    yesorno = input("Please type 'y' for yes and 'n' for no: ")


#decrypting the message
if yesorno == "y":
    for i in encrypted_string:
        if i.isalpha() == True and i.islower() == True:
            #the same code as previously shown is ran, except the key is subtracted instead of added
            num = alphabet.find(i)
            real_num = num - key
            real_real_num = real_num % 26
            decrypted_string += alphabet[real_real_num]
        elif i.isupper() == True:
            num = cap_alphabet.find(i)
            real_num = num - key
            real_real_num = real_num % 26
            decrypted_string += cap_alphabet[real_real_num]
        elif i.isalpha() == False:
            decrypted_string += i

    #printing the decrypted string
    print("The decrypted message is: " + decrypted_string)


# adding a random comment