import os
import json
import csv

def saveInfo(res):
    # 使用 json.loads() 方法将JSON文本解析为字典
    res_json = json.loads(res.text)
    data = res_json['data']
    userInfo = data['userInfo']
    UserName = userInfo['userName']
    keys = userInfo.keys()
    # CSV文件路径
    csv_file_path = 'Student_Info.csv'
    # 获取字典的所有键
    userInfo_keys = userInfo.keys()
    values = [userInfo[key] for key in userInfo_keys]

    # 检查文件是否存在
    if not os.path.isfile(csv_file_path):
        # 如果文件不存在，首先写入表头
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(keys)

    # 追加JSON数据到CSV文件
    with open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(values)

    print("Student_Info保存成功")

    return UserName