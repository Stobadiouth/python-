from urllib import request
req=request.Request('https://s.taobao.com/search?q=shouji&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306')

#添加头信息
req.add_header('user-agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')

#获取请求的完整地址
print(req.full_url)
#获取请求头信息
print(req.headers['User-agent'])

with request.urlopen(req) as f:
    if f.status == 200:
        data = f.read()
        try:
            fp=None
            with open('first.html','wb') as fp:
                fp.write(data)
        except Exception as ex:
            print(ex)
        finally:
            if fp:
                fp.close()