# encoding=utf-8
import time
import spider
from wechat import WeChat

def main():
    wc = WeChat()
    spider_man = {
        "hc3i": "",
        "iyiou": "",
        "sina": "",
        "hchina": "",
        "vcbeat": "",
        "ckxx": "",
        "xinhua": "",
        "biodiscover": "",
    }
    while True:
        for item in spider_man:
            spider_res = getattr(spider, item)()
            if spider_man[item] and spider_man[item] != spider_res["title"]:
                print "new post"
                wc.send(spider_res['title'], spider_res['preview'],
                        spider_res['url'])
            spider_man[item] = spider_res["title"]

        time.sleep(30)
        print "another loop"


if __name__ == '__main__':
    main()
