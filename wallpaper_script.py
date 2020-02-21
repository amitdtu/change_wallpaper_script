import ctypes
import os
import requests
import wget
import time



def set_wallpaper():
    wallpaper_path = get_wallpaper()
    # pathToBmp = os.path.normpath("C:/Users/amit9/OneDrive/Desktop/test.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path  , 0)

def get_wallpaper():
    url = "https://api.unsplash.com/photos/random/?client_id=71d168627b188c16d32034d9d9c47dd994b1f9f1dda20068f20c249476bc0af6"
    params = {
		'query': 'HD Wallpapers',
		'orientation': 'landscape'
	}
    response = requests.get(url, params=params).json()
    # print(response)
    image_source = response['urls']['full']
    # print(image_source)
    wallpaper = wget.download(image_source, "C:/Users/amit9/OneDrive/Desktop/wallpaper.jpg" )
    return wallpaper


if __name__ == '__main__':
    while True:
        set_wallpaper()
        time.sleep(10)

