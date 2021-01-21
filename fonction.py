#All fonction of password maker

import os
import random
from random import choice


listeb = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
listem = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", *listeb]
listes = ["^","£","%","µ","+","-","=",")","(","[","]","{","}","'","&","é","#","$","/","ù","^","!",".",",",".","ç",";","$", *listem]
#this is the differents liste of charactere you can get in your password.



def main():
    type = int(input("What kind of password whould you like:\n[1] Basic (a to z and 0 to 9)\n[2] Medium (a to z, A to Z, "
                 "and 0 to 9)\n[3] Strong (a to z, A to Z, 0 to 9, and a lot of special characters)\n"))


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
    number = int(input("How many charactere would you like to have in your password: "))
    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        b()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listeb))
            file.close()

def m():
    global number
    number = int(input("How many charactere would you like to have in your password: "))
    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        m()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listem))
            file.close()

def s():
    global number
    number = int(input("How many charactere would you like to have in your password: "))
    boucle = 0
    if number <= 0:
        print("You have to choose a number = or > 0")
        s()
    while boucle != number:
        boucle = boucle + 1
        with open("password.txt", "a+") as file:
            file.write(choice(listes))
            file.close()





def retry():
    retry = int(input("You did not choose a good number, would you like to try again?\n[1] Yes\n[2] No\n"))

    if retry == 1:
        os.system('cls')
        main()

    elif retry == 2:
        print("Closing...")
        #Close the programme

    elif retry != 1 or retry != 2:
        input("I think you are stupid...")

