import requests

data = {
    "gridId":"X_Table","pageUrl":"//order//salesOrder//toList"
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'cookie': "uid=CgoUFF0+0D5uOkYjA0YqAg==; sid=5dd6f55102ea492e8a9aafd49e731ca0",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "origin": "https://erp.stage.ybm100.com",
}
r = requests.post(url="https://erp.test.ybm100.com/system/queryUserGridInfoList",data=data,headers=headers)
print(r.text)