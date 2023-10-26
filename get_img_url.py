from conn import conn
from math import ceil
import json
def get_img_url(headers, begin_time, end_time):

    # 定义请求载荷
    payload = {
        "page_index": 1,
        "page_size": 30,
        "search": {
            "kssj": begin_time,
            "jssj": end_time
        },
        "calendarId": "17"
    }
    # 取得分页数量
    res3 = conn.post('http://classroom.csu.edu.cn/api/rawData/getRawDataCount?cal=17&rm=SYS004',headers=headers, json=payload)
    res3_json = json.loads(res3.text)
    page_num_max = ceil(res3_json['data']/30) # 向上取整，每个分页有30条数据


    # 初始化一个空列表来存储所有的 "recordPhoto"
    urls = []
    # 获取图片链接
    for page_index in range(1, page_num_max + 1):
        # 定义请求载荷
        payload = {
            "page_index": page_index,
            "page_size": 30,
            "search": {
                "kssj": begin_time,
                "jssj": end_time
            },
            "calendarId": "17"
        }

        res4 = conn.post('http://classroom.csu.edu.cn/api/rawData/getRawData?cal=17&rm=SYS004',headers=headers, json=payload)
        res4_json = json.loads(res4.text)
        data = res4_json['data']
        records = data["records"]
        # 获取学号
        first_record = records[0]
        userNo = first_record["userNo"]

        # 遍历每个记录并提取 "recordPhoto"
        for record in records:
            if "recordPhoto" in record:
                urls.append(record["recordPhoto"])

    # 完善图片链接
    prefix = "http://classroom.csu.edu.cn/api"
    new_urls = [prefix + url for url in urls]

    # 写入链接
    file_path = userNo + ".txt"
    with open(file_path, "w") as file:
        for url in new_urls:
            file.write(url + "\n")
    
    return(file_path)