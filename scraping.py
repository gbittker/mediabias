import http.client

conn = http.client.HTTPSConnection("twitter241.p.rapidapi.com")

headers = { 'x-rapidapi-host': "twitter241.p.rapidapi.com" }

conn.request("GET", "/user-tweets?user=2455740283&count=20", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))