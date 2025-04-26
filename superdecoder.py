import random
from colorama import Fore

Num = [1,2,3,4,5,6,7]
Answer = []

for i in range(4):
    PickRandom = random.randrange(len(Num))
    Answer.append(Num[PickRandom])
    Num.pop(PickRandom)
# print(f"Answer: {Answer}\n")

for i in range(7):
    UserInput = str(input("Num [x x x x]: "))
    ListInputStr = UserInput.split(" ")
    ListInputInt = []

    for i in range(len(ListInputStr)):
        ListInputInt.append(int(ListInputStr[i])) # convert to int
    # print(f"Input: {ListInputInt}\n")

    ShowOutput = ""
    for i in range(len(ListInputInt)):
        if ListInputInt[i] == Answer[i]:
            ShowOutput += f"{Fore.GREEN} {str(ListInputInt[i])}{Fore.RESET}"
        elif ListInputInt[i] in Answer:
            ShowOutput += f"{Fore.WHITE} {str(ListInputInt[i])}{Fore.RESET}"
        else:
            ShowOutput += f"{Fore.RED} {str(ListInputInt[i])}{Fore.RESET}"

    print(ShowOutput)
    if ListInputInt == Answer:
        print("Congrat!! you win!!")
        break