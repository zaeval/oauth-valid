import json
import requests

ROOT_URL = "https://www.googleapis.com"
USER_ACCESS_URL = "/oauth2/v4/token"
TOKEN_VALID_URL = "/oauth2/v3/tokeninfo"
USER_INFO_URL = "/oauth2/v2/userinfo"

def get_token(client_id, redirect_uri, client_secret, code):
    res = requests.post(ROOT_URL + USER_ACCESS_URL,data={
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code',
    })
    return json.loads(res.text)

def get_token_valid(access_token):
    res = requests.get(ROOT_URL+TOKEN_VALID_URL,params={
        'access_token':access_token
    })
    return json.loads(res.text)

def get_user_info(access_token):
    res = requests.get(ROOT_URL+USER_INFO_URL, headers={'Authorization': 'Bearer '+access_token})
    return json.loads(res.text)

def refresh_token(client_id,client_secret,refresh_token):
    res = requests.post(ROOT_URL + USER_ACCESS_URL,data={
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token' : refresh_token,
        'grant_type': 'refresh_token',
    })
    return json.loads(res.text)

