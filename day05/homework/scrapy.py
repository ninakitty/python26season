import re
import json
from urllib.request import urlopen


def get_handle(url, re_str):
    '''
    获取内容句柄
    :param url:传入链接地址
    :param re_str: 传入re字符
    :return: 返回解析后的内容
    '''
    content = urlopen(url).read().decode("GBK")  # 获取页面信息并解码
    obj = re.compile(re_str, re.S)
    item = obj.finditer(content)
    return item  # 返回内容


def get_index(website, re_str):
    '''
    主页部分--获取2019最新电影链接
    :param website: 主面地址
    :param re_str: 正则表格式内容,字符串中使用(?P<url>)做为分组
    :return:返回链接列表
    '''
    url = []  # 返回链接列表
    item = get_handle(website, re_str)
    for element in item:
        temp_str = website + element.group('url')  # 拼接全网址
        url.append(temp_str)
    return url


def wipe_other(args):
    '''
    去除或替换不需要的内容
    :param args:传入列表或字符串
    :return:返回替换后内容
    '''
    if isinstance(args, list):
        for index, item in enumerate(args):
            if '&middot;' in item:  # 替换'&middot;'
                args[index] = args[index].replace('&middot;', '·')
            args[index] = args[index].strip()  # 去除空白
    elif isinstance(args, str):
        args = args.strip()
        args = args.replace('&middot;', '·')
    return args


def get_content(url):
    '''
    各个电影页面获取信息
    :param url:传入各页面地址
    :return:返回片名,演员,链接字典
    '''
    page_re_str = r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />◎年　　代.*?◎主　　演(?P<actors>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<link>.*?)">'
    item = get_handle(url, page_re_str)
    content_dict = {}
    for element in item:  # 解析内容
        content_dict['name'] = wipe_other(element.group('name'))
        content_dict['actors'] = wipe_other(element.group('actors').split('<br />　　　　　　'))
        content_dict['link'] = wipe_other(element.group('link'))
    return content_dict


def json_operate(json_file, mode='r', json_content=[]):
    '''
    JSON操作
    :param json_file: 要操作的文件
    :param mode: 操作模式
    :param json_list: 需要dump的内容
    :return:
    '''

    if mode == 'w':
        json.dump(json_content, open(json_file, mode=mode, encoding='utf8'))
    elif mode == 'r':
        res = json.load(open(json_file, mode=mode, encoding='utf8'))
        return res


def main_operate():
    '''
    主操作函数,将爬取结果dump到文件,然后load文件并输出
    :return:无返回值
    '''
    json_list = []  # 要dump到文件中的list
    json_file = 'Latest_movices_2019.json'  # dump文件
    website = 'https://www.dytt8.net'  # 主页地址
    re_str = r"最新电影下载</a>]<a href='(?P<url>.*?)'>"  # 主页正则

    url_list = get_index(website, re_str)  # 获取主页面URL_LIST

    for url in url_list:  # 获取各个页面内容,添加到列表
        json_list.append(get_content(url))

    json_operate(json_file, mode='w', json_content=json_list)  # dump到文件

    res = json_operate(json_file)  # load出内容
    for index, item in enumerate(res):
        print(index + 1, '-->', item)


if __name__ == '__main__':
    main_operate()
