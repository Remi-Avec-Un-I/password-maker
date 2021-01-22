#All fonction of password maker

import os
import random
from random import choice


listeb = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
listem = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", *listeb]
listes = ["^","£","%","µ","+","-","=",")","(","[","]","{","}","'","&","é","#","$","/","ù","^","!",".",",",".","ç",";","$", *listem]
#this is the differents liste of charactere you can get in your password.



def main():
    try:
        type = int(input("What kind of password whould you like:\n[1] Basic (a to z and 0 to 9)\n[2] Medium (a to z, A to Z, "
                    "and 0 to 9)\n[3] Strong (a to z, A to Z, 0 to 9, and a lot of special characters)\n"))
    except ValueError :
        os.system("cls")
        print("Please, enter a number, not a letter !")
        main()


    if type == 1:
        b()


    elif type == 2:
            m()
        

    elif type == 3:
        s()
    #this will create a random password depend of the liste choice you did in the beginning, and the amount of charactere you choose

    else:
        retry()







def openpassword():
    #Wrote your password on the password.txt and open it for you
    file = open('password.txt', "a+")
    file.write("\n/-/-/-/-/-/-/ \n")
    file.close()
    print("Password save in password.txt\n")
    os.startfile("password.txt")







def b():
    global number


    try:
        number = int(input("How many charactere would you like to have in your password: "))
    except ValueError :
        os.system("cls")
        print("You have to choose with a number !")
        b()


    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        b()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listeb))
            file.close()
    openpassword()

def m():
    global number


    try :
        number = int(input("How many charactere would you like to have in your password: "))
    except ValueError :
        os.system("cls")
        print(f"You have to choose with a number !")
        m()

    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        m()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listem))
            file.close()
    openpassword()

def s():
    global number


    try: 
        number = int(input("How many charactere would you like to have in your password: "))
    except ValueError :
        os.system("cls")
        print(f"You have to choose with a number !")
        s()


    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        s()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listes))
            file.close()
    openpassword()





def retry():
    retry = input("You did not choose a good number, would you like to try again?\n[yes] Yes\n[no] No\n")

    if retry == "yes":
        os.system("cls")
        main()

    elif retry == "no":
        print("Closing...")
        #Close the programme

    elif retry != "yes" or retry != "no":
        input("I think you are stupid...")

