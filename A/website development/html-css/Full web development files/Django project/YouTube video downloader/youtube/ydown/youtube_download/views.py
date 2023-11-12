from django.shortcuts import render

# Create your views here.

def ytb_down(request):
	return render(request,'ytb_main.html')
	
def yt_download(request):
	return render(request,'yt_download.html')