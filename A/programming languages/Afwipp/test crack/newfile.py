import hashlib

pass_hash = input("Enter md5 hash: ")


wordlist = input("file name: ")

try:
	pass_file = openv(wordlist, "r")
except:
	print("no file found!")
	quit()
	
for word in pass_file:
	
	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word)