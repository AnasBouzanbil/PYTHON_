import requests
import os
import sys
import spyinsta


file_name = ""




def asking():
    global file_name
    file_name = input("Enter the file name of victim: ")
    file = open(file_name + ".txt", 'w')
    questions = [
        "Name ",
        "City ",
        "Gender ",
        "Instagram ",
        "LinkedIn ",
        "Facebook ",
        "Phone Number",
        "Age ",
        "Friends",
        "Boyfriend/Girlfriend Status",
        "Social",
        "Family",
        "Email",
        "Bad happits",
        "Godd happbits"
    ]

    print("Please provide the following information. Type 'Done' to finish.")
    
    for question in questions:
        answer = input(f"{question}: ")
        file.write(f"| {question:<25}    {answer:<25} |\n{'-'*60}\n")

    file.close()


def updatee():
    file_name = input("Enter the name of victim : ")
    key_to_update = input("Enter the key to update: ")

    with open(file_name + ".txt", 'r') as file:
        lines = file.readlines()

    found = False
    for i, line in enumerate(lines):
        if key_to_update in line:
            found = True
            new_value = input(f"Enter the new value for {key_to_update}: ")
            lines[i] = f"| {key_to_update:<25} {new_value:<25} |{'-'*30} Modifed {'-' *  30}\n"
            break

    if not found:
        print(f"Key '{key_to_update}' not found in the file.")
        return

    with open(file_name + ".txt", 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    w = input("Update ot new or instaspy [U / N/ S] ")
    if w == "U":
        updatee()
    elif w == "N":
        asking()
    elif w == "S":
        name = input("Enter the name of victim: ")
        spyinsta.start(name)

    
