import requests

BASE = 'http://127.0.0.1:5000/'
'''
data =[{"likes":100000,"name":"Gorgeous","views":10000},
{"likes":800000,"name":"Anti-Hero","views":100000000},
{"likes":50000,"name":"Karma","views":10000},
{"likes":900,"name":"Cowboy like me","views":1000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())
'''


response = requests.patch(BASE + 'video/2', {})
print(response.json())
