import json

import requests

ROOT_URL = "https://kauth.kakao.com"
API_ROOT_URL = "https://kapi.kakao.com"
USER_ACCESS_URL = "/oauth/token"
TOKEN_VALID_URL = "/v1/user/access_token_info"
USER_INFO_URL = "/v2/user/me"

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
    res = requests.get(API_ROOT_URL+TOKEN_VALID_URL,headers={'Authorization': 'Bearer '+access_token})
    return json.loads(res.text)

def get_user_info(access_token):
    res = requests.get(API_ROOT_URL+USER_INFO_URL, headers={'Authorization': 'Bearer '+access_token})
    return json.loads(res.text)

def refresh_token(client_id,client_secret,refresh_token):
    res = requests.post(ROOT_URL + USER_ACCESS_URL,data={
        'grant_type':'refresh_token',
        'refresh_token':refresh_token,
        'client_id':client_id,
        'client_secret':client_secret,
    })
    return json.loads(res.text)
