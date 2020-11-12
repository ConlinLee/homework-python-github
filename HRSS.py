def hrss1():
    import requests
    import urllib3

    urllib3.disable_warnings()

    url1='https://hrss.h3c.com/Attendance/GetAutoEmployeeImageList?q=lvlei&limit=20&timestamp=1589559723950'
    header = {
        'Host': 'hrss.h3c.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://hrss.h3c.com/',
    }
    s = requests.session()
    res = s.get(url=url1, headers=header, verify=False, timeout=5,allow_redirects=False)

    cookies = requests.utils.dict_from_cookiejar(res.cookies)

    print(res)
    # print(cookies)
    print(res.text)

if __name__=='__main__':
    hrss1()