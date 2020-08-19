import os

hostname = input('Please enter a hostname or IP address: ')
response = os.system('ping -n 1 ' + hostname)
if response == 0:
    pingstatus = 'Network Active'
else:
    pingstatus = 'Network Error'

print(pingstatus)
