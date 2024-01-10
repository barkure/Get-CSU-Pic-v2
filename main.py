from login import login
from saveInfo import saveInfo
from get_img_url import get_img_url
from download_urls import download_urls
from datetime import datetime


number = 12345678910 # 此处填写学号
number_str = str(number)
password = "Csu@{}".format(number_str[-6:]) # 默认密码为 Csu@学号后六位

res_login, headers = login(number, password)
userName = saveInfo(res_login)

# 获取当前时间
current_time = datetime.now()

begin_time = "2023-07-27 12:55:43" #开始时间可自己修改
# 以当前时间为 end_time
end_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

urls_file_path = get_img_url(headers, begin_time, end_time)

download_urls(urls_file_path, userName)