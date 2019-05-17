#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 30
'''
1, 爬取电影天堂 2019新片精品 区域内的电影. json结果格式为 [{电影名: name, 演员: [actress, actor], 下载地址: downloadUrl}, ...]
2, 爬取链家租房的房源信息
'''
import requests
import time
import re


class HttpHelper(object):
    '''
    一个http请求助手,可以根据域名与资源uri来批量获取对应的页面内容.
    主要作用是针对业务需求,对requests进行了一次功能筛选性的封装. 便于使用,减少冗余代码的作用.
    随着学习的不断深入,对功能性需求和代码可复用度也会越来越高. 那么就需要关注到代码的可扩展空间问题了.
    比较习惯用requests模块,所以http请求部分使用requests模块来做了.我看requests是基于urllib3封装的.应该会比urllib和urllib2好吧?
    并且支持keep-alive了,现在网站几乎全部都会利用http1.1的长链接特性.并且2.0以后还支持了长链接并发.应该urllib3是趋势吧.等后面听听老师怎么讲.
    '''
    def __init__(self, domain_name, uris=None, mode="get", code="utf-8", interval=1, headers=None):
        self.domain_name = domain_name
        self.uris = uris    # 格式为 [{"path": path, "params": {params}}, ...] 如果以后需要增加post数据或修改headers可以利用这个数据结构进行扩展
        self.headers = headers
        self.mode = mode
        self.code = code
        self.interva = interval
        if not uris:
            self.uris = [{"path": "/", "params": {}}]
        if not headers:
            self.headers = {}

    def contents(self):
        mappings = {"get": self.__get_contents,
                    "post": None}
        if not mappings.get(self.mode):
            print("mode模式选择错误或功能尚未启用,请在%s内选择" % [k for k in mappings.keys() if k])
            return False
        # 根据http请求方法来执行相应的类方法,通过生成器返回页面信息.以后还可以加post,put,delete等方法,便与扩展.
        for result in mappings[self.mode]():
            # 如果设置了间隔时间,那么启用sleep机制.反爬其实还可以做修改httpheader等.
            # 默认interval为1秒,如果以后加了修改http头的反爬机制,那么interval可以设置为False了.
            if self.interva and (isinstance(self.interva, float) or isinstance(self.interva, int)):
                time.sleep(self.interva)
            yield result

    def __get_contents(self):
        for uri in self.uris:
            path = uri["path"]
            url = self.domain_name + path
            params = uri.get("params")
            req = requests.get(url=url, params=params, headers=self.headers)
            result = dict()
            result["url"] = url
            result["status"] = req.ok
            result["status_code"] = req.status_code
            # 尝试过使用requests.text来获得页面内容,但是发现解码有问题. 最后还是自己手动解码了.
            result["content"] = req.content.decode(self.code)
            yield result


def dytt():
    def get_paths_of_2019_div(content):
        p = r"2019新片精品.*?更多>>.*?(最新电影下载.*?href='.*?)</table>"
        find_div = re.compile(p, re.DOTALL)
        content_2019_div = find_div.search(content).group()
        find_href = re.compile(r"最新电影下载.*?href='(.*?)'", re.DOTALL)
        # 这里其实可以直接使用findall
        result = []
        for i in find_href.finditer(content_2019_div):
            result.append({"path": i.group(1)})
        return result

    def add_result(result_list, respons):
        content = respons["content"]
        p = r"<div id=\"Zoom\".*?◎片　　名(.*?)<br />.*?◎主　　演(.*?)<br />◎.*?<tbody>.*?href=\"(.*?)\".*?</tbody>"
        find_item = re.compile(p, re.DOTALL)
        matchs = find_item.search(content)
        item = {"url": respons["url"]}
        if matchs:
            name = matchs.group(1).replace("&middot;", "·").replace("\u3000", " ").strip()
            actors = [i.replace("&middot;", "·").replace("\u3000", " ").strip() for i in matchs.group(2).split("<br />") if i]
            download_url = matchs.group(3)
            item = {"name": name, "actors": actors, "download_url": download_url}
        result_list.append(item)

    # 面向过程部分
    domain_name = "https://www.dytt8.net"
    portal_content = HttpHelper(domain_name, code="gbk", interval=False).contents().__next__()   # 获得首页内容
    paths = get_paths_of_2019_div(portal_content["content"])      # 获得2019新片精品div部分的链接
    result = []
    for i in HttpHelper(domain_name, paths, code="gbk", interval=0.1).contents():
        # i是2019新片精品div内的页面信息 {"url": url, "status": bool, "status_code": code, "content": 页面内容}
        if not i["status"]:
            result.append({i["url"]: i["status_code"]})
            continue
        add_result(result, i)    # 根据题意筛选出 电影名 主演 下载地址 并加入到result列表内.
    return result


def lianjia():
    def handler(house_info, response):
        # 页面请求异常处理.
        if not response["status"]:
            print("%s 请求失败 code: %s" % (response["url"], response["status_code"]))
            return False
        # 爬取 房源信息名称 和 租金
        p = r'<a target="_blank" href=".*?">(.*?)</a>.*?<em>(\d+)</em> 元/月'
        find_item = re.compile(p, re.DOTALL)
        # 循环将每条格式化好的信息记录在列表内一份,用来return. 因为每个页面是生成器出来的,所以爬一页print一页,用户体验会好一些.
        for i in find_item.finditer(response["content"]):
            house = i.group(1).strip()
            cost = "%s 元/月" % i.group(2)
            record = {"house": house, "cost": cost}
            house_info.append(record)
            print(record)

    # 链家有反爬机制,需要改一下httpheader中的客户端信息. 否则会403的.
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    domain_name = "https://bj.lianjia.com"
    # 链家租房有100个页面, 这里生成一下100个页面的uri.
    uris = []
    for n in range(1, 101):
        path = "/zufang/pg%s/#contentList" % n
        uris.append({"path": path})
    house_info = []
    for response in HttpHelper(domain_name, uris=uris, mode="get", code="utf-8", interval=1, headers=headers).contents():
        # 每个response是每个页面的响应信息
        handler(house_info, response)     # 这里处理每个页面,使用正则摘取出需要的信息并打印.
    return house_info


def main():
    '''
    爬取电影天堂
    '''
    # for i in dytt():
    #     print("片名: %s" % i["name"])
    #     print("主演: %s" % i["actors"])
    #     print("下载地址: %s" % i["download_url"])
    #     print("-" * 30)

    '''
    爬取链家租房信息
    '''
    lianjia()


if __name__ == "__main__":
    main()

