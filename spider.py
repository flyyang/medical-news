# encoding= utf-8
from pyquery import PyQuery as pq
import functools
import logging

def make_request(url):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                d = pq(url=url, encoding="utf-8")
            except Exception as e:
                logging.error(e)
            return func(d)
        return wrapper
    return decorator
@make_request("http://www.hc3i.cn")
def hc3i(d):
    """中国数字医疗网"""
    element = d(".news .element")
    preview = element(".wrap .con").eq(0).text()
    title = element(".wrap .name a").eq(0).text()
    url = element(".wrap .name a").attr('href')

    return {
        "title": title,
        "preview": preview,
        "url": url,
    }


@make_request("http://www.iyiou.com/i/yiliao")
def iyiou(d):
    """亿欧"""
    li = d(".content-rpmain .active li").eq(0)
    a = li("a").eq(0)
    url = a.attr('href')
    title = a.attr('title')
    preview = li(".fl p").text()
    return {
        "title": title,
        "preview": preview,
        "url": url,
    }


@make_request("http://med.sina.com/")
def sina(d):
    """新浪医药"""
    li = d(".news_1List li").eq(0)
    a = li(".indextitle-text a").eq(0)
    url = a.attr('href')
    title = a.text()
    preview = li(".indextext-ms").text()
    return {
        "title": title,
        "preview": preview,
        "url": url,
    }

@make_request("http://health.china.com.cn/")
def hchina(d):
    """健康中国"""
    li = d(".rzuo .d1").eq(0)
    a = li("a").eq(0)
    url = a.attr('href')
    title = a.text()
    preview = a.text()
    return {
        "title": title,
        "preview": preview,
        "url": "http://health.china.com.cn/" + url,
    }

@make_request("http://vcbeat.net/")
def vcbeat(d):
    """动脉网"""
    li = d(".content li").eq(0)
    a = li("a").eq(1)
    url = a.attr('href')
    title = a.text()
    preview = li("h2").text()

    return {
        "title": title,
        "preview": preview,
        "url": "http://vcbeat.net/" + url,
    }

@make_request("http://www.cankaoxiaoxi.com/science/jksh/")
def ckxx(d):
    """参考消息"""
    li = d(".inner li").eq(0)
    a = li("a").eq(0)
    url = a.attr('href')
    title = a.text()
    preview = title

    return {
        "title": title,
        "preview": preview,
        "url": url,
    }

@make_request("http://www.news.cn/health/")
def xinhua(d):
    """新华健康"""
    news = d(".headNews").eq(0)
    a = news("a").eq(0)

    url = a.attr('href')
    title = a.text()
    preview = news('.ywzy').text()
    return {
        "title": title,
        "preview": preview,
        "url": url,
    }


@make_request("http://www.biodiscover.com/news.html")
def biodiscover(d):
    """生物探索"""
    d = pq(url="http://www.biodiscover.com/news.html", encoding="utf-8")
    news = d(".list_info .list_div").eq(0)
    a = news("h1 a").eq(0)

    url = a.attr('href')
    title = a.text()
    preview = news('.intro').text()

    return {
        "title": title,
        "preview": preview,
        "url": "http://www.biodiscover.com" + url,
    }
