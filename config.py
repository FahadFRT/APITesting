import requests
from requests.structures import CaseInsensitiveDict


URL = 'https://httpbin.org'
URLDA = 'https://httpbin.org/digest-auth'
USER = 'fahad'
PASSWORD = 'my_pass'
USER_PASS = 'fahad/my_pass'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzMDAwNTg4LCJqdGkiOiI4YTdiMzhlY2JjMTI0NTZlOTgzYzlhYTEzZDFhOGJjNCIsInVzZXJfaWQiOjI3MzMsImZpcnN0X25hbWUiOiJ4bG5rIiwibGFzdF9uYW1lIjoibG9hZDI3NTAiLCJ2aXNpdF9sb2dzIjoyLCJkYXRlX2pvaW5lZCI6IjIwMjEtMDgtMzAgMTI6MDc6MTMuODExOTk4KzAwOjAwIn0.qU4VE9-AiidDi92IOim33maIdijvS8PSUH3zXxy7KyM'
HEADERS = CaseInsensitiveDict()
# HEADERS = {
#                 'authorization':f'Bearer {TOKEN}',
#                 'content-type':'application/json',
#                 'Accept':'application/json'
#                 'qop': 'auth',
#                 'If_Modified_Since': 'test',
#                 'If_Modified_Since': 'test',
#                 'stale_after': 'never',
#                 'algorithm': 'MD5',
#
#            }


QOP = HEADERS['qop'] = 'auth'
ALGORITHM = HEADERS['algorithm'] = 'MD5'
STALE_AFTER = HEADERS['stale_after'] = 'never'
ACCEPT = HEADERS['Accept'] = 'application/json'
AUTHORIZATION = HEADERS['Authorization'] = f'Bearer {TOKEN}'
IF_MODIFIED_SINCE = HEADERS['If-Modified-Since'] = 'test'
IF_None_MATCH = HEADERS['IF-None-MATCH'] = 'test'
CONTENT_TYPE = HEADERS['Content-Type'] = 'application/json'
DSTRING = 'HTTPBIN is awesome'
SESSION = requests.Session()


