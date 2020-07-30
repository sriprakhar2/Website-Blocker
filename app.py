# This is a website blocker project which blocks certain website for certain period of time i.e 8 AM to 8 PM
# To run it as soon as when computer start follow the steps
#   For the linux users 
#       open sudo crontab -e
#       type @reboot python3 "absolute path of the file"
#       save it.
#   For the windows users
#       set host_path of this script as "C:\Windows\System32\drivers\etc\hosts"
#       Do it with task-scheduler, add task over there and create processes
import time
from datetime import datetime as dt

website_list=['www.facebook.com','facebook.com']
host_address=r'/etc/hosts'
redirect='127.0.0.1'
host_temp="hosts"
# As this file should be run as process when machine starts hence as infinte loop is used
while True:
    # This conditional will check for the time that ranges between 8 AM to 8 PM
    # In this perios we are not allowed to access the websites of that list
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        with open(host_address,'r+') as file:
            # We read the content of file in r+ mode which allows the reading and appendnig content at the same time
            content = file.read()
            # We check for every value of website list
            # If that value or website already exist in content(The content of file) we simply pass
            # else we write those websites in the file
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_address,'r+') as file:
            # Here we read lines line by line, content will be list which contains input.
            # readlines() method will take input line by line and store as input
            content=file.readlines()
            # seek() method will take the file pointer to the begining of file
            file.seek(0)
            # Here, we go through per value of content list
            for line in content:
                # We check every line of content
                # If any line of content list contains the value that was in website_list 
                # Then that line will not be written back
                 if not any(website in line for website in website_list):
                    file.write(line)
            # We delete all the previous contents of file to escape the re-writing content
            file.truncate()
    time.sleep(5)