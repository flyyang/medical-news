# encoding= utf-8
from pyquery import PyQuery as pq

def hc3i():
    """中国数字医疗网"""
    d = pq(url="http://www.hc3i.cn", encoding="utf-8")
    element = d(".news .element")
    preview = element(".wrap .con").eq(0).text()
    title = element(".wrap .name a").eq(0).text()
    url = element(".wrap .name a").attr('href')

    return {
        "title": title,
        "preview": preview,
        "url": url,
    }

def iyiou():
    """亿欧"""
    d = pq(url="http://www.iyiou.com/i/yiliao", encoding="utf-8")
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

def sina():
    """新浪医药"""
    d = pq(url="http://med.sina.com/", encoding="utf-8")
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

def hchina():
    """健康中国"""
    d = pq(url="http://health.china.com.cn/", encoding="utf-8")
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

def vcbeat():
    """动脉网"""
    d = pq(url="http://vcbeat.net/", encoding="utf-8")
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

def ckxx():
    """参考消息"""
    d = pq(url="http://www.cankaoxiaoxi.com/science/jksh/", encoding="utf-8")
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

def xinhua():
    """新华健康"""
    d = pq(url="http://www.news.cn/health/", encoding="utf-8")
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
def biodiscover():
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
