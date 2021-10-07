import os
import keyboard
import webbrowser



def open_istg():
    webbrowser.open("https://www.instagram.com")

def play_music():
    music_dir = 'D:\\Songs' # ADD YOUR PATH TO MUSIC DIRECTORY HERE
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

def vs_code():  #ADD YOUR VS CODE PATH IN codepath BELOW
    codePath = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code" #ADD YOUR VS_CODE PATH HERE
    os.startfile(codePath)

keyboard.add_hotkey('i + g', open_istg)
keyboard.add_hotkey('m + u', play_music)
keyboard.add_hotkey('v + s', vs_code)
keyboard.wait('esc')
