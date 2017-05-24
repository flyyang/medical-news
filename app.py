# encoding=utf-8
import time
import spider
from wechat import WeChat
import logging
from const import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def main():
    wc = WeChat()
    spider_man = {
        "hc3i": "",
        "iyiou": "",
        "sina": "",
        "hchina": "",
        "vcbeat": "",
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
    logging.info("start ower spider .... ")
    logging.info(spider_bug)
    while True:
        for item in spider_man:
            try:
                spider_res = getattr(spider, item)()
            except Exception as e:
                logging.error(e)
                continue
            logging.info(u'【' + site_map[item] + u'】' + spider_res['title'])
            if spider_man[item] and spider_man[item] != spider_res["title"]:
                logging.info("new post find:")
                wc.send(u'【' + site_map[item] + u'】' + spider_res['title'],
                        spider_res['preview'],
                        spider_res['url'])
            spider_man[item] = spider_res["title"]

        time.sleep(10)
        logging.info("new loop")


if __name__ == '__main__':
    main()
