import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes":10, "name":"Anthony", "views":28},
#         {"likes":78, "name":"Miguel", "views":100},
#         {"likes":226000, "name":"Melvin", "views":300000}]


# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print("[*] ",response.json())

response = requests.patch(BASE + "video/2", {"views": 999})
print(response.json())