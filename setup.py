import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt-get install seanime")
    os.system("apt-get install serd")
    os.system("apt-get install strace")
    os.system("pip install progressbar")
elif c == "1":

     os.system("apt-get install seanime")
     os.system("apt-get install serd")
     os.system("apt-get install strace")
     os.system("pip3 install progressbar")
print("Done.")
