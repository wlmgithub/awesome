
# http://stackoverflow.com/questions/28328890/python-requests-extract-url-parameters-from-a-string


from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests

url = "http://httpbin.org/get?token=TOKEN_TO_REPLACE&param2=c"

o = urlparse(url)

query = parse_qs(o.query)

url = o._replace(query=None).geturl()

if 'token' in query:
    query['token'] = 'NEW_TOKEN'

response = requests.get(url, params=query)

print(response.text)


