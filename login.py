import json
from conn import conn
from password2pwd import encrypt
from captcha2text import captcha2text

def login(number, password):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }

    # Get验证码图片
    res1 = conn.get('http://classroom.csu.edu.cn/api/account/getVerify?num', headers=headers)
    # 保存此 cookies ，后续提交验证码若 cookies 不一致，会显示验证码错误
    cookie = res1.cookies
    # 识别验证码
    captcha_img = res1.content
    with open('captcha.jpg','wb') as f:
        f.write(captcha_img)
    captcha_text = captcha2text('captcha.jpg')

    # 构建登陆数据
    pwd = encrypt(password)

    login_data = {
        "client": "web_atd",
        "loginName": number,
        "pwd": pwd,
        "type": "1",
        "verificationCode": str(captcha_text)
    }

    # POST请求登录
    res2 = conn.post('http://classroom.csu.edu.cn/api/account/loginCheck?', headers=headers, cookies=cookie, json=login_data)
    # 获取token
    res_json = json.loads(res2.text)
    data = res_json['data']
    token = data['token']
    # 处理请求标头，方便后续使用
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
    Authorization = f'Token {token}'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Content-Length': '118',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': str(cookie),
        'Host': 'classroom.csu.edu.cn',
        'Origin': 'http://classroom.csu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://classroom.csu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }

    return res2, headers