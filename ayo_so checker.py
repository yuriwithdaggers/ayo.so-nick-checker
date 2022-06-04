import requests
from colorama import Fore, Back, Style, init
init(convert=True)

def nicks():
    try:
        with open('nicks.txt', 'r', encoding='utf-8') as f:
            f = f.read().replace('\n', '-')
            return f
    except (AttributeError, FileNotFoundError):
        print('Make sure there is a nicks.txt in the folder')
    
def check():
    nick = nicks()
    nick = nick.strip(' ').split('-')
    for i in nick:
        r = requests.get(f'https://ayo.so/{i}')
        if r.status_code == 404:
            print(Fore.BLACK + Back.GREEN + f"[ ! ] Nick '{i}' -> Available" + Style.RESET_ALL)
        else:
            print(Fore.BLACK + Back.RED + f"[ ! ] Nick '{i}' -> Not Available" + Style.RESET_ALL)
    print(Fore.BLACK + Back.WHITE + f"[ & ] Done. Press any key to exit." + Style.RESET_ALL)


def main():
    print(Fore.MAGENTA + """
 ▄▄▄·  ▄· ▄▌         .▄▄ ·         
▐█ ▀█ ▐█▪██▌▪        ▐█ ▀. ▪       
▄█▀▀█ ▐█▌▐█▪ ▄█▀▄    ▄▀▀▀█▄ ▄█▀▄   
▐█ ▪▐▌ ▐█▀·.▐█▌.▐▌   ▐█▄▪▐█▐█▌.▐▌  
 ▀  ▀   ▀ •  ▀█▄▀▪ ▀  ▀▀▀▀  ▀█▄▀▪  
 ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀

    """ + Style.RESET_ALL)
    check()
    input()

if __name__ == "__main__":
    main()