import requests
from datetime import datetime

USERNAME = "your user name"
TOKEN = "your token"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"


}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Meditation graph",
    "unit": "Min",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you meditate today? ")
}

response = requests.post(url=post_pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)

# today = datetime(year=2024,month=8,day=20)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20240820"

pixel_update_config = {
    
    "quantity": "5"
}
# response = requests.put(url=update_pixel_endpoint,json=pixel_update_config,headers=headers)
# print(response.text)

#DELETE

# response = requests.delete(url=update_pixel_endpoint,headers=headers)
# print(response.text)
