
cookie = "uid=CgoUFF0+0D5uOkYjA0YqAg==; sid=0bfde42bea2b4ae8bfcaf2206b224fd6"

def get_headers(header_flag):
    if header_flag == 'data_form':
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie':cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            "origin":"https://erp.stage.ybm100.com",
        }
    elif header_flag == 'json':
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            "origin":"https://erp.stage.ybm100.com",
        }
    else:
        headers = {}

    return headers


if __name__ == '__main__':
    get_headers('data_form')
