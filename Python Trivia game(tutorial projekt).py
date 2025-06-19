# collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string  #gibt acces zur einer list of all of the characters welches lowercase, uppercase, zahlen oder special characters wie ! sind.

def generate_password():
    length = int(input("Enter the desired password length: ").strip()) #strip um spaces zu löschen, und macht es zu einem int, weil ich ja eine zahl als input haben möchte und nicht string
    include_uppercase = input("Include uppercase letter? (yes/no): ").strip().lower() #lower ist fals er Yes ausversehen groß schreibt oder no
    include_special = input("Include special characters ? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at elast 4 characters.")
        return    #bei return gehst du zum exit der funktion also zu generate_passwort(), also unter return wird geskipped
    
    lower = string.ascii_lowercase #gibves all of the lowercase letters
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""   #das ist ein inline if statement, string.ascii_uppercase ist der value vpn der variable upper wenn die condition true ist also yes sonst empty string
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits #dass ist eine string concatenation, es squished die strings zusammen

    required_characters = []  #da kommen characters die wird brauchen dass wir bei max 3 sind
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))   #random.choice damit random ein uppercase genommen wird
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)  #die länge von passwort - dass wie viel wird gepicked haben
    password = required_characters

    for _ in range(remaining_length):   #es lässt die for loop so lange laufen, however many characters left there are to pick, _ ist wenn du etwas nicht definen möchtest, mir ist ja egal welcher index da ich random möchte
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)  #es schaut sich die liste an password und randomly mixed all die items die drinnen sind
    
    str_password = "".join(password) #.join nimmt eine liste, hier password * required_characters und combined all die elemente in dieser liste zusammen mithelfe wasauchimmer vor join dieser string ist als seperator, hier wäre es ""
    return str_password

    
password = generate_password()
print(password)


