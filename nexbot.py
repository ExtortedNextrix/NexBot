import time, requests, json, os, random, ctypes
from colorama import Fore
from pypresence import Presence

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
                                                                           

ctypes.windll.kernel32.SetConsoleTitleW("Welcome to Nexbot!")

with open('config.json') as f:
    config = json.load(f)

os.system("cls")

# Speed Var []-! DONT CHANGE !-[]
speed_var = config.get("SPEED")

# Customize RPC Vars []-! DONT CHANGE !-[]
token = config.get("TOKEN")
large_image_var = config.get("LARGE_IMAGE")
small_image_var =config.get("SMALL_IMAGE")
large_text_var =config.get("LARGE_TEXT")
small_text_var =config.get("SMALL_TEXT")
state_var = config.get("STATE")

# Change Party size
party_size_var=[int(69),int(420)]
# Change what you want the button to be: syntax = Change "My Website" to whatever you want the name of the button to be :: Change the url to the directory of a website... |]-! Only works for others to click on !-[|
buttons_var=[{"label":"My Website", "url":"https://nextrix.ml/"}]



detailstext = [ # Change these placeholders to whatever you want.
    "1987",
    "nextrix#8446",
    "ExtortedVRC",
    "Python Dev",
    "Programmer",
    "Checkout my Website",
    "1337",
    "1983",
    "HTML Dev",
    "CSS Dev",
    "Ur bad",
    "fvck off skid",
    "Unity Animator",
    "GFX",
    "Unity VFX Animator",
    "Computer Engineer"
    ]



# RPC Load
client_id = "1002489968217821184"
RPC = Presence(client_id)
RPC.connect()

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

def start():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Connected Token with Nexbot!")
    print(f"{Fore.RED}Started!\n")
    print("\n")
    while True:
        # RPC Updater
        RPC.update(
            large_image=large_image_var,
            small_image=small_image_var,
            large_text=large_text_var,
            small_text=small_text_var,
            details=str(random.choice(detailstext)),
            state=state_var,
            party_size=party_size_var,
            buttons=buttons_var,
            
            # Dont Change Time because it can break the RPC! (it wont show for other people)
            start=int(time.time()),
            end=int(time.time()),
            )
        
        
        
        
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