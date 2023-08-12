import pytube

url = input("enter your url: ")
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)
