from oauth_valid.kakao import get_token, get_token_valid, get_user_info

KAKAO_APP_ID = "{YOUR_APP_ID}"
KAKAO_SECRET_KEY = "{YOUR_SECRET_KEY}"
REDIRECTION_URI = "{WHERE_TO_REDIRECTION_URL}"
CODE = "{GET CODE FROM URL PARAM}"

token_res = get_token(KAKAO_APP_ID, REDIRECTION_URI, KAKAO_SECRET_KEY, CODE)
print(token_res)

access_token = token_res.get('access_token', None)
refresh_token = token_res.get('refresh_token', None)

print(access_token, refresh_token)

if access_token == None or refresh_token == None:
    #TODO: unauthorized exception
    pass

valid_res = get_token_valid(access_token)

print(valid_res)

user_info_res = get_user_info(access_token)

properties = user_info_res.get('properties', None)
print(properties)

kakao_account = user_info_res.get('kakao_account', None)
print(kakao_account)

# redirect to this url you can see the dialog to kakao login
# https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID==KAKAO_APP_ID}&redirect_uri={REDIRECTION_URI}&response_type=code

