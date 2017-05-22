# encoding= utf-8
"中国数字医疗网"
from pyquery import PyQuery as pq

def hc3i():
    d = pq(url="http://www.hc3i.cn", encoding="utf-8")
    element = d(".news .element")
    preview = element(".wrap .con").eq(0).text()
    print preview
    title = element(".wrap .name a").eq(0).text()
    url = element(".wrap .name a").attr('href')
    print "title", title
    print "url", url
    latest_update_time = element(".foot .deta").eq(0).text()
    return {
        "title": title,
        "preview": preview,
        "url": url,
        "latest_update_time": latest_update_time
    }

