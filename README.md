# oauth-valid
Oauth valid served by zaeval.

It is using for nonprofit.

![](https://img.shields.io/badge/pip-v0.0.2-blue.svg)
![](https://img.shields.io/github/license/mashape/apistatus.svg)
![](https://img.shields.io/badge/require-requests%20%7C%20bs4-orange.svg)
![](https://img.shields.io/badge/author-zaeval-red.svg)

# Oauth Process
![](https://raw.githubusercontent.com/among-software/oauth-valid/master/statics/oauth_server_process.png)

# FaceBook

Update soon

# Kakao

[kakao 연동 예제 바로가기](https://github.com/among-software/oauth-valid/blob/master/examples/kakao.py)

## 클라에서 코드 요청하기
### redirect_url과 함께 code 요청 ( 카카오 로그인 창 띄우기 )

https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_APP_ID}&redirect_uri={REDIRECTION_URI}&response_type=code

위 url로 리다이렉트를 하면 카카오 로그인 창이 뜹니다.

로그인 창에 회원 정보를 입력하여 로그인하면 redirection url로 이동하고 url parameter로 code가 같이 넘어옵니다.

### 허용 redirection url 설정하기

위 코드를 가져오기 위한 url을 완성하기 위해선 KAKAO_APP_ID와 REDIRECTION_URI가 필요합니다.

REDIRECTION_URI는 아래 화면에서 수정을 눌러 추가가 가능합니다.

![](https://raw.githubusercontent.com/among-software/oauth-valid/master/statics/kakao_redirect_url.png)

> 단 https://~:포트번호/path 까지 absolute url로 full path를 써주어야 합니다.

### client id 찾기 

요약 정보에서 Rest Api키 부분에 있는걸 쓰면 됩니다.

![](https://raw.githubusercontent.com/among-software/oauth-valid/master/statics/kakao_app_id.png)

### secret key 찾기

카카오 로그인 > 보안 탭에서 코드 부분에 있는 값을 쓰면 됩니다.

![](https://raw.githubusercontent.com/among-software/oauth-valid/master/statics/kakao_secret.png)


# Google

Update soon