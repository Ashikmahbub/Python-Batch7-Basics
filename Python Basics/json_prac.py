import json

# Parsing JSON string to Python object (dictionary) deserialization
data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"]) 



# Converting Python object (dictionary) to JSON string serialization

json_data = {"name": "Jane", "age": 25, "city": "Los Angeles"}
json_string = json.dumps(json_data)
print("JSON String:", json_string)


import requests
# get data from a public API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)
post_data = response.json()
print (post_data)
print("Post Title:", post_data['title'])
print("Post Body:", post_data['body'])

#post request
new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1 
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print("Status Code:", response.status_code)
created_post = response.json()
print("Created Post:", created_post)
print("Created Post ID:", created_post['id'])

#put request update
updated_post = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}


response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
print("Status Code:", response.status_code)
post = response.json()
print("Updated Post:", post)
print("Updated Post Title:", post['title'])
print("Updated Post Body:", post['body'])

#delete request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Post deleted successfully")
else:
    print("Failed to delete the post")