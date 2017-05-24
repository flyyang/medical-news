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
    site_map = {
        "hc3i": u"中国数字医疗网",
        "iyiou": u"亿欧",
        "sina": u"新浪医药",
        "hchina": u"健康中国",
        "vcbeat": u"动脉网",
        "ckxx": u"参考消息",
        "xinhua": u"新华健康",
        "biodiscover": u"生物探索",
    }
    spider_bug = """
    ||  ||
     \\()//
    //(__)\\
    ||    ||
    """
    print "start ower spider .... "
    print spider_bug
    while True:
        for item in spider_man:
            spider_res = getattr(spider, item)()
            print spider_res["title"]
            try:
                spider_res = getattr(spider, item)()
            except:
                break
            if spider_man[item] and spider_man[item] != spider_res["title"]:
                print "new post find"
                wc.send(u'【' + site_map[item] + u'】' + spider_res['title'],
                        spider_res['preview'],
                        spider_res['url'])
            spider_man[item] = spider_res["title"]

        time.sleep(10)
        print "new loop"


if __name__ == '__main__':
    main()
