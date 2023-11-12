from pytube import YouTube

url = input("enter url: ")
vd = YouTube(url)

print("\nVideo title: " + vd.title)

print("\nVideo Thumnail url: " + vd.thumbnail_url)
print("\ndownloading!.......")
vd = vd.streams.get_highest_resolution()
i =  vd.download()
print("\ndownload finished: " + i)


