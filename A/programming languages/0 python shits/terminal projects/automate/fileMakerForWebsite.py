import os
import time

def os_create_templatedir():
	a = True
	while a==True:
	    f = input("enter directory: ")
	    os.mkdir(f)
	    os.chdir(f)
	    a = False
	
def os_create_cssdir():
	os.mkdir("css")
	os.chdir("css/")
	
def mkfile_html_snippet():
	a = True
	while a == True:
		f = input("html name: ")
		i = open(f,"w")
		i.write("<!Doctype html>\n<html lang=\"en\">\n\t<head>\n\t\t<title>Page title</title>\n\t\t<link rel=\"stylesheet\" href=\" \">\n\t</head>\n\t<body>\n\t</body>\n<html>")
		i.close()
		if f == "n":
			a = False
			os.remove("n")
	
def mkfile_css_snippet():
	a = True
	while a == True:
		f = input("css name: ")
		css = open(f,"w")
		css.close()
		if f == "d":
			a = False
			os.remove("d")
	
def output():
    print("making all files......")
    time.sleep(1)
    print("done")
			
def function():
	os_create_templatedir()
	mkfile_html_snippet()
	os_create_cssdir()
	mkfile_css_snippet()
	output()
	
function()
