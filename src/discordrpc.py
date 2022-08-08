import json, random, time, array, requests, ctypes
from colorama import Fore
from pypresence import Presence

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


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


with open('src/config/config.json') as f:
    config = json.load(f)

# Speed Var []-! DONT CHANGE !-[]
speed_var = config.get("SPEED")

# Customize RPC Vars []-! DONT CHANGE !-[]
large_image_var = config.get("LARGE_IMAGE")
small_image_var = config.get("SMALL_IMAGE")

# Customize RPC Vars []-! DONT CHANGE !-[]
token = config.get("TOKEN")
large_text_var =config.get("LARGE_TEXT")
small_text_var =config.get("SMALL_TEXT")
state_var = config.get("STATE")

# Change Party size
party_size_var=[int(69),int(420)]
# Change what you want the button to be: syntax = Change "My Website" to whatever you want the name of the button to be :: Change the url to the directory of a website... |]-! Only works for others to click on !-[|
buttons_var=[{"label":"My Website", "url":"https://nextrix.ml/"}, {"label":"My Github", "url":"https://github.com/ExtortedNextrix"}]



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




print(f"{Fore.BLUE}RPC Handler Started!\n")
print("\n")

framesDelay = 1
c = -1

if large_image_var == "gif":
    numFrames = input(f"{Fore.CYAN}How many frames does your GIF have:\t")
    time.sleep(0.8)
    print(f"Gif is using {numFrames} frames!")
    while True:
        # RPC Updater
        if c == numFrames:
            c = 0
        else:
            c = c+1
        RPC.update(
            large_image=str(c),
            small_image=small_image_var,
            large_text=large_text_var,
            small_text=small_text_var,
            details=str(random.choice(detailstext)),
            state=state_var,
            party_size=party_size_var,
            buttons=buttons_var,
            )
        time.sleep(framesDelay)
else:
    print(f"Using {large_image_var} as Large image!")
    while True:
        RPC.update(
            large_image=large_image_var,
            small_image=small_image_var,
            large_text=large_text_var,
            small_text=small_text_var,
            details=str(random.choice(detailstext)),
            state=state_var,
            party_size=party_size_var,
            buttons=buttons_var,
            )
        time.sleep(framesDelay)
        
    

    
