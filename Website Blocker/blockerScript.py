import time
from datetime import datetime as dt #set the variable as dt so it is easy to write
hosts_temp="hosts" #file in directory
hosts_path = "/etc/hosts" #you can place r in front of quotes to identify as row
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.buzzfeed.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours")
    time.sleep(5) #run script every 5 seconds