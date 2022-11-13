import requests
import random
import string
from colorama import Fore
import time
from pystyle import Colors, Colorate

print(Colorate.Horizontal(Colors.cyan_to_blue,"""GEN NITRO.\n"""))
time.sleep(0.7)
num = int(input(f'{Fore.LIGHTBLUE_EX}NITRO GENERATED NUMBER : \n'))
time.sleep(1)


with open("Nitro Link.txt", "w", encoding='utf-8') as file:
    print(Colorate.Horizontal(Colors.cyan_to_blue,"""GENERATED NITRO!"""))
    time.sleep(0.7)

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.com/billing/promotions/{code}\n")

    print(f"{Fore.LIGHTCYAN_EX}GENERATED {num} LINK !\n")

with open("Nitro Link.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n VALID | {nitro}\n\n")
        else:
            print(f"{Fore.LIGHTCYAN_EX}[+] , ", end = "")

print(Colorate.Horizontal(Colors.rainbow, ('''SUCCESFULLY GENERATED''')))
