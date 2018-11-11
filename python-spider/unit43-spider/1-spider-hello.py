from urllib import request
with request.urlopen('http://www.runoob.com/') as f:
    # data=f.read()
    # #f.status 状态码 f.reason
    # print('Status:',f.status,f.reason)#Status:200 ok
    # print(data)

    if f.status==200:
        #读取返回的主题内容，赋值给data，此时数据格式为字节码
        data=f.read()
        # print(data.decode())
        #读取返回的头信息，头信息格式为元组列表
        for k,v in f.getheaders():
            print(k,v)


        # #把爬到的数据装入文件
        try:
            fp=None
            with open('first.html','wb') as fp:
                fp.write(data)
        except Exception as ex:
            print(ex)
        finally:
            if fp:
                fp.close()