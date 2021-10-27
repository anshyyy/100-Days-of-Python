from datetime import *
import requests

USERNAME = "anshyyy"
TOKEN = "anshumansharmaaa"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "anshyyy",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_cofig = {
    "id": "graph1",
    "name": "My coding graph",
    "unit": "hour",
    "type": "float",
    "color":"kuro",
}
headers = {
    "X-USER-TOKEN":TOKEN
}
#respnse=requests.post(url=graph_endpoint,json=graph_cofig,headers=headers)
# print(respnse.text)
today = datetime(year=2021,month=10,day=27)
pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"4",
}
# response1 = requests.post(url=pixel_creation,headers=headers,json=pixel)
# print(response1.text)
pixel_updation = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
body = {
    "quantity":"9"
}
# response = requests.put(url=pixel_updation,json=body,headers=headers)
# print((response.text))
response = requests.delete(url=pixel_updation,headers=headers)
print(response.text)

