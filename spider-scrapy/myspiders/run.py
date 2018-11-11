# from scrapy.cmdline import execute
#
# execute('scrapy crawl jumei -o jumei.json'.split())
from datetime import datetime

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie='CwCzwf_sex_ta=2; CwCzwf_userid=11004091; 11004255=11004255; CwCzwf_dialog_greet_index=1; 10917494=10917494; 10637213=10637213; 10842417=10842417; 10820078=10820078; 10443693=10443693; 10997501=10997501; 10583600=10583600; 10729173=10729173; 10961561=10961561; 10666092=10666092; 10673026=10673026; 10554236=10554236; 10970329=10970329; 10433893=10433893; 10591754=10591754; 10587353=10587353; 10710495=10710495; 10598658=10598658; 10838862=10838862; 10963975=10963975; 10430633=10430633; 10981739=10981739; 10581579=10581579; 10786990=10786990; 10901490=10901490; 10763821=10763821; 329432=329432; 10500023=10500023; 10976045=10976045; 10427311=10427311; 10969246=10969246; 10713231=10713231; 10764176=10764176; 10825465=10825465; 10590704=10590704; Hm_lvt_13345a0835e13dfae20053e4d44560b9=1539570372,1539671853,1539764087,1539909782; PHPSESSID=cb7cd565fkgsgnq55l6e046fi2; CwCzwf_prompt_tomorry=1; 10981110=10981110; Hm_lpvt_13345a0835e13dfae20053e4d44560b9=1539910587'
    trans = transCookie(cookie)
    print(trans.stringToDict())
    # user=  {
    # "id": "11003405",
    # "addr": "\u4fdd\u5bc6",
    # "weight": "\u4fdd\u5bc6",
    # "constellation": "\u4fdd\u5bc6",
    # "blood": "O\u578b",
    # "nation": "\u6c49\u65cf",
    # "profession": "\u5176\u4ed6\u884c\u4e1a",
    # "house": "\u4fdd\u5bc6",
    # "school": "\u4fdd\u5bc6",
    # "children": "\u4fdd\u5bc6",
    # "img_src": "http://www.hongniang.com/data/upload/photo/20180908/5b939131e0d6b.jpeg"
    # }
    # del user["img_src"]
    # print(user)



