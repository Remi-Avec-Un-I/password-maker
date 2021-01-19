
import os
import random
from random import choice


print("This is the new version of my strong password, in this one you are able to choose your password's complexity.")
type = int(input("What kind of password whould you like:\n[1] Basic (a to z and 0 to 9)\n[2] Medium (a to z, A to Z, "
                 "and 0 to 9)\n[3] Strong (a to z, A to Z, 0 to 9, and a lot of special characters)\n"))

number = 0

listeb = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
listem = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", *listeb]
listes = ["^","£","%","µ","+","-","=",")","(","[","]","{","}","'","&","é","#","$","/","ù","^","!",".",",",".","ç",";","$", *listem]
#this is the differents liste of charactere you can get in your password.

def openpassword():
    #Wrote your password on the password.txt and open it for you
    file = open('password.txt', "a+")
    file.write("\n/-/-/-/-/-/-/ \n")
    file.close()
    print("Password save in password.txt\n")
    os.startfile("password.txt")


if type == 1:
    def main():
        global number
        number = int(input("How many charactere would you like to have in your password: "))
        boucle = 0
        if number <= 0:
            print("You have to choose a number = or > 0")
            main()
        while boucle != number:
            boucle = boucle + 1
            with open("password.txt", "a+") as file:
                file.write(choice(listeb))
                file.close()
        openpassword()


elif type == 2:
    def main():
        global number
        number = int(input("How many charactere would you like to have in your password: "))
        boucle = 0
        if number <= 0:
            print("You have to choose a number = or > 0")
            main()
        while boucle != number:
            boucle = boucle + 1
            with open("password.txt", "a+") as file:
                file.write(choice(listem))
                file.close()
        openpassword()
        

elif type == 3:
    def main():
        global number
        number = int(input("How many charactere would you like to have in your password: "))
        boucle = 0
        if number <= 0:
            print("You have to choose a number = or > 0")
            main()
        while boucle != number:
            boucle = boucle + 1
            with open("password.txt", "a+") as file:
                file.write(choice(listes))
                file.close()
        openpassword()
#this will create a random password depend of the liste choice you did in the beginning, and the amount of charactere you choose

else:
    retry = int(input("You did not choose a good number, would you like to try again?\n[1] Yes\n[2] No\n"))
    if retry == 1:
        def main():
            os.startfile("passwordmaker.py")
    elif retry == 2:
        def main():
            print("Closing...")
            #Close the programme
    elif retry != 1 or retry != 2:
        def main():
            close = input("I think you are stupid...")


main()

    
