alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Please enter the message that you would like to cypher: ")

counter = 0
for i in message:
    if i == " ":
        counter += 1

while counter >= 5:
    counter = 0
    message = input("Please enter only a maximum of five words: ")
    for i in message:
        if i == " ":
            counter += 1


key = input("Please enter a number for the letter shift: ")
if key.isnumeric() == True:
    key = int(key)
elif key.isnumeric() == False:
    while key.isnumeric() == False:
        key = input("please enter a positive integer number for the key: ")
        if key.isnumeric() == True:
            key = int(key)
            break

encrypted_string = ""
decrypted_string = ""



for i in message:
    if i.isalpha() == True and i.islower() == True:
        num = alphabet.find(i)
        real_num = num + key
        real_real_num = real_num % 26
        encrypted_string += alphabet[real_real_num]
    elif i.isupper() == True:
        num = cap_alphabet.find(i)
        real_num = num + key
        real_real_num = real_num % 26
        encrypted_string += cap_alphabet[real_real_num]
    elif i.isalpha() == False:
        encrypted_string += i

print("The encrypted message is: " + encrypted_string)





yesorno = input("Would you like to decrypt this message(y/n): ")

while yesorno != "y" and yesorno != "n":
    yesorno = input("Please type 'y' for yes and 'n' for no: ")


if yesorno == "y":
    for i in encrypted_string:
        if i.isalpha() == True and i.islower() == True:
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

    print("The decrypted message is: " + decrypted_string)
