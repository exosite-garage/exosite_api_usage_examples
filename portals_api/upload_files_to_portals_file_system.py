# Example that uploads a file to the Portals File System using Portals API
# Access Level- Portals Domain Administrator
# Note: Uses Python 'Requests' module for calling API
# APIs:
# - http://docs.exosite.com/portals/#update-file-content


import requests
import getpass

directory = "images" #default directory name
domain = "" #example: example.exosite.com
user_email = "" #example: myname@example.com - assume administrator access to Portals Domain Solution
if domain == "":
	domain = raw_input('Enter Portals Domain (e.g. "example.exosite.com": ')
if user_email == "":
	user_email = raw_input('Enter Your Email Address: ')
user_password = getpass.getpass()  #ask for password each time at prompt


# Files to upload
files = {"MyLogo.png":open("./MyLogo.png", "rb"),
         "MyOtherLogo.jpg":open("./MyOtherLogo.jpg", "rb")
        }


url = "https://"+domain+"/api/portals/v1/fs/"+directory

print 'Uploading files to ' + domain

r = requests.post(url, files=files, auth=(user_email, user_password))

print("Status: ", r.status_code)

r = requests.get(url)

if r.status_code == 200:
        folder = r.json()
        for directory, filepath in folder.iteritems():
                for filename, filetype in filepath.iteritems():
                        print("/".join([url,directory,filename]))