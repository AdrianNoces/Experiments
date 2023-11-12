#!/bin/bash
import os
import time

def os_create_templatedir():
	os.mkdir("templates")
	os.chdir("templates/")
	
def os_create_cssdir():
	os.mkdir("css")
	os.chdir("css/")
	
def mkfile_html_snippet():
	i = open("index.html","w")
	i.write("<!doctype html>\n<html>\n\t<head>\n\t\t<!--title start here-->\n\n\t\t<title>Page title</title>\n\n\n\t\t<!--link stylesheet start here-->\n\n\t\t<link rel=\"stylesheet\" href=\"css/style.css\">\n\n\t</head>\n\t<body>\n\n\n\n\n\n\n\n\n\t</body>\n<html>")
	i.close()

def mkfile_css_snippet():
	css = open("style.css","w")
	css.write(".body {\n  margin: 0;\n}")
	css.close()
	
def output():
	print("Making template...")
	time.sleep(1)
	print("making index.html...")
	time.sleep(1)
	print("making css/style.css...")
	time.sleep(1)
	print("done✓\ndone✓\ndone✓")
			
def function():
	os_create_templatedir()
	mkfile_html_snippet()
	os_create_cssdir()
	mkfile_css_snippet()
	output()
	
function()	