import json
import requests

saleRequestUrl = "http://sale.backend.hkdev.cn"
fouraSaleRequestUrl = "http://4a-api.hkdev.cn"
# 4a账号密码

loginName = "gadmin"
plainPassword = "fL8K+wj68cA2XL4YD50SMBrDBClSPXfcOkNVxbtIbroqbN8lY9DQGLJWFoJ9B++y40ZAzG5f0lqE3kXzRI4b0INwu6dZ6lu4wt6rXnz6G1wIjt2O9eEHS4IeKXd4tYe1BP6VGk8ZYqmAVZjAmqKMGhxtRkwP0PkVsmDA1TLkmTI="


class GroupActivity:
    def __init__(self):
        pass

    # 拼团详情
    def getGroupActivityDetail(self, groupActivityId, cookie):
        url = f"{saleRequestUrl}/mds/groupActivity/detail?groupActivityId={groupActivityId}&_t=1664519994687"
        payload = {}
        headers = {
            'Cookie': cookie
        }
        # 响应体
        response = requests.request("GET", url, headers=headers, data=payload)
        # 字符串转对象
        json_object = json.loads(response.text)
        # 字符串格式化输出商品skuid和spuid
        print(
            f'skuId:{json_object["data"]["groupActivitySkuDtoList"][0]["skuId"]} spuId：{json_object["data"]["groupActivitySkuDtoList"][0]["spuId"]}')

    # 有效拼团
    def getGroupActivityList(self, cookie):
        url = f"{saleRequestUrl}/mds/groupActivity/list?pageNo=1&status=1&spellModel=0&pageSize=100&totalPage=100&_t=1664521399156"

        payload = {}
        headers = {
            'Cookie': cookie
        }
        #
        response = requests.request("GET", url, headers=headers, data=payload)

        # print(response.text)
        #
        arr = json.loads(response.text)["data"]["results"]
        list = []
        for i in range(len(arr)):
            list.append(arr[i]['id'])
        #
        print(list)
        return list

    def backendLogin(self):
        url = f"{fouraSaleRequestUrl}/auth/login"
        # 对象转字符串
        payload = json.dumps({
            "loginName": loginName,
            "plainPassword": plainPassword
        })
        # 请求头
        headers = {
            'Content-Type': 'application/json',
        }
        # 响应体
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        # 响应头
        # print(response.headers['Set-Cookie'])
        # 判断登录结果
        if (json.loads(response.text))["success"]:
            return {"result": "success", "data": response.headers['Set-Cookie']}
        else:
            return {"result": "success", "data": None}


if __name__ == '__main__':
    # 登录
    cookie = GroupActivity().backendLogin()["data"]
    # 有效拼团
    effectiveGroupActiviy = GroupActivity().getGroupActivityList(cookie)
    # 拼团商品信息
    for activityID in effectiveGroupActiviy:
        GroupActivity().getGroupActivityDetail(activityID, cookie)
