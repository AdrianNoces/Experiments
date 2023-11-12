import os

os.mkdir("I love you all")

os.chdir("I love you all/")

f=open("shits.txt","w")

for i in range(30*2):
	
	word=str(i)+"\t"
	
	f.write(word)

print("done writing numbers!")

f.write("I love you all from den!" * 200)

f.close()
			
print("done writing all")			
		
		
		
		