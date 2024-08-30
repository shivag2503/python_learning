import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "jejrjkkakadn88dfsop"

parameters = {
    "token": TOKEN,
    "username": "shivam25",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(PIXELA_ENDPOINT, json=parameters)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/shivam25/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Questions",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(GRAPH_ENDPOINT, json=graph_config, headers=headers)

POST_GRAPH = f"{PIXELA_ENDPOINT}/shivam25/graphs/graph1"

post_config = {
    "date": "20240831",
    "quantity": "13",
}

# requests.post(POST_GRAPH, json=post_config, headers=headers)

PUT_GRAPH = f"{PIXELA_ENDPOINT}/shivam25/graphs/graph1/20240831"

put_config = {
    "quantity": "10"
}

# response = requests.put(PUT_GRAPH, json=put_config, headers=headers)
# print(response.text)

response = requests.delete(PUT_GRAPH, headers=headers)
