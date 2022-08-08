import time, requests, json, os, random, ctypes, subprocess
from colorama import Fore


"""
by nextrix#8446

███▄▄▄▄      ▄████████ ▀████    ▐████▀ ▀█████████▄   ▄██████▄      ███     
███▀▀▀██▄   ███    ███   ███▌   ████▀    ███    ███ ███    ███ ▀█████████▄ 
███   ███   ███    █▀     ███  ▐███      ███    ███ ███    ███    ▀███▀▀██ 
███   ███  ▄███▄▄▄        ▀███▄███▀     ▄███▄▄▄██▀  ███    ███     ███   ▀ 
███   ███ ▀▀███▀▀▀        ████▀██▄     ▀▀███▀▀▀██▄  ███    ███     ███     
███   ███   ███    █▄    ▐███  ▀███      ███    ██▄ ███    ███     ███     
███   ███   ███    ███  ▄███     ███▄    ███    ███ ███    ███     ███     
 ▀█   █▀    ██████████ ████       ███▄ ▄█████████▀   ▀██████▀     ▄████▀    


""" 
                                                                           

#select='null'


ctypes.windll.kernel32.SetConsoleTitleW("Welcome to Nexbot!")

with open('src/config/config.json') as f:
    config = json.load(f)

os.system("cls")


# Speed Var []-! DONT CHANGE !-[]
speed_var = config.get("SPEED")

# Customize RPC Vars []-! DONT CHANGE !-[]
token = config.get("TOKEN")




print(
    f"{Fore.CYAN}███▄▄▄▄      ▄████████ ▀████    ▐████▀ ▀█████████▄   ▄██████▄      ███    \n",
    f"███▀▀▀██▄   ███    ███   ███▌   ████▀    ███    ███ ███    ███ ▀█████████▄\n",
    f"███   ███   ███    █▀     ███  ▐███      ███    ███ ███    ███    ▀███▀▀██\n",
    f"███   ███  ▄███▄▄▄        ▀███▄███▀     ▄███▄▄▄██▀  ███    ███     ███   ▀\n",
    f"███   ███ ▀▀███▀▀▀        ████▀██▄     ▀▀███▀▀▀██▄  ███    ███     ███    \n",
    f"███   ███   ███    █▄    ▐███  ▀███      ███    ██▄ ███    ███     ███    \n",
    f"███   ███   ███    ███  ▄███     ███▄    ███    ███ ███    ███     ███    \n",
    f"▀█   █▀    ██████████ ████       ███▄ ▄█████████▀   ▀██████▀     ▄████▀   \n",
    f"\t\t {Fore.BLUE}by {Fore.MAGENTA}nextrix#8446"
    )

print("\n")
print(f"{Fore.LIGHTGREEN_EX}  This has a customizable RPC and Status within config.json\n")
input(f"{Fore.YELLOW}  Press enter to continue {Fore.BLACK}>> \t")
py = 'python src/discordrpc.py'
cmd = "rpc1.bat"
p = subprocess.Popen(py, creationflags=subprocess.CREATE_NEW_CONSOLE)
#, creationflags=subprocess.CREATE_NEW_CONSOLE
def start():
    os.system("cls")
    
    ctypes.windll.kernel32.SetConsoleTitleW("Connected Token with Nexbot!")
    print(f"{Fore.RED}Custom Status Started!\n")
    print("\n")
    
    while True:
        
        #print("cycling motd")
        # Debug Motd Changer     |::| ! Dont touch unless you know what your doing ! |::|
        """content = {
                    "custom_status": {"text": "nextrix.ml"},
                    "status": "dnd"
                }

        r = requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':token}, json=content)
        print(r.content)

        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':token}, json=content)
        time.sleep(float(speed_var))"""
        
        

        # Normal Motd Changer
        content = {
                "custom_status": {"text": "nextrix.ml"}, # Change nextrix.ml to whatever you want.
                "status": "dnd" # dnd = do not disturb :: Change it to: online, idle, offline, or dnd.
            }

        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':token}, json=content)
        time.sleep(float(speed_var))

        content = {
                "custom_status": {"text": "ExtortedVRC"}, # Change ExtortedVRC to whatever you want.
                "status": "online" # Change it to: online, idle, offline, or dnd.
                
            }

        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':token}, json=content)
        time.sleep(float(speed_var))

        content = {
                "custom_status": {"text": "Python Dev"}, # Change Python Dev to whatever you want.
                "status": "idle" # Change it to: online, idle, offline, or dnd.
            }

        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':token}, json=content)
        time.sleep(float(speed_var))

start()