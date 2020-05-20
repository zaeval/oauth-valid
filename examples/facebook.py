from oauth_valid.facebook import get_token, get_app_access_token, get_token_valid, get_user_info

FACEBOOK_APP_ID = "{YOUR_APP_ID}"
FACEBOOK_SECRET_KEY = "{YOUR_SECRET_KEY}"
REDIRECTION_URI = "{WHERE_TO_REDIRECTION_URL}"
CODE = "{GET CODE FROM URL PARAM}"
# here is token issued
res = get_token(FACEBOOK_APP_ID,REDIRECTION_URI,FACEBOOK_SECRET_KEY,CODE)
access_token = res.get('access_token',None)
print(res)

# here is token valid logic
app_access_token_res = get_app_access_token(FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY)
print(app_access_token_res)

valid_res = get_token_valid(access_token, app_access_token_res['access_token'])
print(valid_res)

if not valid_res['data']['is_valid']:
    #TODO: unauthorized exception
    pass

user_info_res = get_user_info(valid_res['data']['user_id'],['email','gender','id','name'],access_token)

user_id = user_info_res.get('id', None)

if user_id == None:
    #TODO: unauthorized exception
    pass

# redirect to this url you can see the dialog to facebook login
# https://www.facebook.com/dialog/oauth?client_id={CLIENT_ID}&redirect_uri={REDIRECTION_URI}&scope=email,public_profile