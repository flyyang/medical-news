## 简介

爬取相关医疗新闻网站，并推送给对应的企业号应用。采编要失业了:)

## 支持

目前支持以下几个网站:

* [中国数字医疗网](http://www.hc3i.cn)
* [亿欧](http://www.iyiou.com/)
* [新浪医药](http://med.sina.com/)
* [健康中国](http://health.china.com.cn/)
* [动脉网](http://vcbeat.net/)
* [参考消息](http://www.cankaoxiaoxi.com)
* [新华健康](http://www.news.cn/health/)
* [生物探索（biodiscovery）](http://www.news.cn/health/)

## demo

每当以上网站有内容更新时，推送通知到指定应用，所有关注者都可以查看。

<img src="demo.jpg" width="250" height="600">

## SET UP

运行之前，你需要在项目根目录新建 `config.ini`， 用于配置微信企业号:

```
corpid =
corpsecret =
party =
agentid =
token_url = https://qyapi.weixin.qq.com/cgi-bin/gettoken
msg_url = https://qyapi.weixin.qq.com/cgi-bin/message/send

```

另外，新建一个日志文件用来记录日志：

```
tocuh app.log
chmod +w app.log
```
