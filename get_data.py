# get_data.py

import json, requests, pandas, html, os, urllib.request

print("REQUESTING SOME DATA FROM THE INTERNET...")
print("---------------------------------------------")
## TODO: Requesting a Product
request_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products/2.json"
r = requests.get(request_url)
print("URL1 has a single product:", r.json()["name"])
# print(type(r.json()["name"]))

# ALTERNATIVE PRINT METHOD
    # with urllib.request.urlopen(request_url) as url:
    #     data = json.loads(url.read().decode())
    #     print(data)
    #     print(type(data))


## TODO: Requesting Products
request_url_2 = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products.json"
r2 = requests.get(request_url_2)
prod_list = r2.json()
print("---------------------------------------------")
print("URL2 has the following products:")
[print("NAME:", i["name"]+",", "ID:", str(i["id"])) for i in prod_list]
print("---------------------------------------------")
## TODO: Requesting the Gradebook
request_url_3 = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/gradebook.json"
r3 = requests.get(request_url_3)
grades = r3.json()
print(type(grades))
# with open(grades, "r") as grades_file:
#     file_grades = grades_file.read()
# gradebook = json.loads(file_grades)

# print(gradebook)