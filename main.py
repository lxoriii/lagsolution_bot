import discord  ,  json  ,  os
from discord.ext import bridge
from colorama import Fore
import ezcord

def get_config(name):
    with open("config.json", "r") as f:
        json_file = json.load(f)
        return json_file[name]

client = ezcord.Bot(
    command_prefix=get_config('prefix'),
    intents=discord.Intents.all(),
    help_command=None,
    error_webhook_url='https://discord.com/api/webhooks/1101598247534997595/66jlf1YhlQs4X8ooKuBrZUwI4hFp5g3vncc6B8hhUpVOOi8yxcXJ337E-f4xoj4v6gHF'
)


def load():
    os.system("cls")
    print(Fore.RED + " ____________________________________")
    print(Fore.RED + "/                                    \ ")
    print(Fore.RED + "|      _ _         _____             |")
    print(Fore.RED + "|     | | |       |  __ \            |")
    print(Fore.RED + "|   __| | |____  _| |  | | _____   __|")
    print(Fore.RED + "|  / _` | '_ \ \/ / |  | |/ _ \ \ / /|")
    print(Fore.RED + "| | (_| | |_) >  <| |__| |  __/\ V / |")
    print(Fore.RED + "|  \__,_|_.__/_/\_\_____/ \___| \_/  |")
    print(Fore.RED + "|                                    |")
    print(Fore.RED + f"|             " + Fore.BLUE + f"Lag Solution" + Fore.RED + "           |")
    print(Fore.RED + "\____________________________________/\n" + Fore.GREEN + "|")

    folders = [
        "Events", "Commands"
        ]
    for folder in folders:
        for file in os.listdir(f"./{folder}"):
            if file.endswith(".py"):
                client.load_extension(f"{folder.replace('/', '.')}.{file[:-3]}")
                print(Fore.GREEN + f'| {file} was loaded')
    print(Fore.GREEN + f'\_______________________________')


if __name__ == '__main__':
    load()
    client.run(get_config('token'))