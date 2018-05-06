#
#

import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts" # r at the beginning tells python that the string that follows is Raw string. so all special characters are not interpreted.

redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18) :
        print("Its Working Hours !!!")
        time.sleep(5)
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content :
                    pass
                else :
                    file.write(redirect+" "+website+"\n")
    else :
        with open(host_path, 'r+') as file :
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Working Hours are OVER.. Go and PLAY !!!!")
        time.sleep(5)
