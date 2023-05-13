from collections import Counter
import requests
import json


def count(url):

    response = requests.get(url)
    content = response.text

# In the below code I have used Div tag just to make output small and simplified.. 
# but we can replace div tag with body tag then we can get whole content of static website

    start = content.find("<div")
    end = content.find("</div>")
    text = content[start:end].replace('\n', ' ')

    words = text.split()
    counts = Counter(words)

    return json.dumps(counts)

url = 'http://127.0.0.1:5500/static.html'

print(count(url))