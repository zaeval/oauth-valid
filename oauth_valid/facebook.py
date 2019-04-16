import json

import requests

VERSION = "v3.2"
ROOT_URL = "https://graph.facebook.com/%s" % VERSION
APP_ACCESS_URL = "/oauth/access_token"
USER_ACCESS_URL = "/oauth/access_token"
TOKEN_VALID_URL = "/debug_token"

def get_token(client_id, redirect_uri, client_secret, code):
    res = requests.get(ROOT_URL + USER_ACCESS_URL, params={
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'client_secret': client_secret,
        'code': code
    })
    return json.loads(res.text)

def get_app_access_token(client_id,client_secret):
    res = requests.get(ROOT_URL+APP_ACCESS_URL,params={
        'grant_type':'client_credentials',
        'client_id':client_id,
        'client_secret' : client_secret,
    })
    return json.loads(res.text)

def get_token_valid(user_access_token,app_access_token):
    res = requests.get(ROOT_URL+TOKEN_VALID_URL,params={
        'input_token':user_access_token,
        'access_token':app_access_token
    })
    return json.loads(res.text)

def get_user_info(user_id,scopes,access_token):
    res = requests.get(ROOT_URL[:-2] + "/" + user_id, params={
        'fields':",".join(scopes),
        'access_token':access_token,
    })
    return json.loads(res.text)
