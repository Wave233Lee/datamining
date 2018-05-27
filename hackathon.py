
#!-*- coding:utf-8 -*-
# 获取用户GitHub上的信息
import random

import chardet
from importlib import reload
from urllib import request  # 导入urllib库中的request模块
import re

import pymysql
from bs4 import BeautifulSoup
from urllib import error


# from data_manage import models
# from data_manage.models import stackoverflow_tags, user_tags, score_tags
# import pymysql
# import os,django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_manage.settings")
# django.setup()


# import urllib2
# import re
# from data_manage import models


def get_github(github_url):
    github_url = "https://github.com/TheAlgorithms"  # 随便找的一个大牛的GitHub

    res = request.urlopen(github_url)

    html = res.read().decode('utf-8')

    bs = BeautifulSoup(html)

    return bs.ol;


def get_csdn(csdn_url):
    csdn_url = "https://blog.csdn.net/xy294636185"  # 随便找的一个大牛的GitHub

    # 分页抓取
    page_num = 1
    notlast = 1
    article_list = []
    while notlast:
        page_url = csdn_url + '/article/list/' + str(page_num)  # 对每页的URL

        # 直接爬取
        res = request.urlopen(csdn_url)
        html = res.read().decode('utf-8')

        # 抓取标题、阅读数、评论数
        titles = re.findall('<span class="article-type type-1">.*?</span>\n(.*?)</a>', html, re.M | re.S)
        views = re.findall('<span class="read-num">阅读数：(.*?)</span>', html, re.M | re.S)
        comments = re.findall('<span class="read-num">评论数：(.*?)</span>', html, re.M | re.S)

        # 将数据存在article_list列表里面

        file = open('article.txt', 'w')
        for i in range(len(titles)):
            article_list.append([titles[i].strip(), views[i], comments[i]])
            # print("文章标题： ", titles[i], " 阅读数： ", views[i], " 评论数： ", comments[i])
            print(titles[i].strip(), views[i], comments[i])
            file.write(str(titles[i].strip() + " " + views[i] + " " + comments[i] + "\n"))
        file.close()

        page_num += 1

        # notlast = re.findall('', html, re.M|re.S)
        break

    return article_list


def get_csdn_1():
    # -*- coding: utf-8 -*-

    # 当前的博客列表页号
    page_num = 1
    # 不是最后列表的一页，如果有尾页说明不是最后一页
    notLast = 1

    account = "mrzhang628"

    # 首页地址
    baseUrl = 'http://blog.csdn.net/' + account

    while notLast:
        # 连接页号，组成爬取的页面网址
        myUrl = baseUrl + '/article/list/' + str(page_num)

        # 伪装成浏览器访问，直接访问的话csdn会拒绝

        # 构造请求
        # req = request.Request(baseUrl, headers=headers)

        # request = urllib2.Request(myUrl);
        # request.add_header(headers);

        # print("req = ",str(req));

        # 访问页面

        myResponse = request.urlopen(myUrl)  # timeout用来设置超时

        myPage = myResponse.read()

        # print("notLast = " ,str(notLast));

        print
        '-----------------------------第%d页---------------------------------' % (page_num,)

        # 利用正则表达式来获取博客的标题
        titles = re.findall('<span class="link_title"><a href=".*?">(.*?)</a></span>', myPage, re.S)
        titleList = []  # 表用[ ]标识。是python最通用的复合数据类型
        for items in titles:
            titleList.append(str(items).lstrip().rstrip())  # list.append(obj)：在列表末尾添加新的对象

        # 利用正则表达式获取博客的访问量
        views = re.findall('<span class="link_view".*?><a href=".*?" title="阅读次数">阅读</a>(.∗?)</span>', myPage, re.S)
        viewList = []
        for items in views:
            viewList.append(str(items).lstrip().rstrip())

            # 这里相当于创造一个迭代器
        index = []
        count = 0
        while (count < len(viewList)):
            index.insert(count, count)
            count = count + 1

        print(index)

        # 将结果输出
        # for n in index:  # range(len(titleList)):
        #     print
        #     '访问量:%s 标题:%s' % (viewList[n].zfill(4), titleList[n])

        # 页号加1
        page_num = page_num + 1

        # 在页面中查找是否存在‘尾页’这一个标签来判断是否为最后一页
        notLast = re.findall('<a href=".*?">尾页</a>', myPage, re.S)


def get_stackoverflow():
    # 抓取全网标签页
    tags_url = 'https://stackoverflow.com/tags'
    tags_html = request.urlopen(tags_url).read().decode('utf-8')
    print("......")
    tags_list = re.findall(
        r'<a href="/questions/tagged/.*?" class="post-tag" title="show questions tagged &#39;.*?&#39;" rel="tag">(?:<img src=".*?" height="16" width="18" alt="" class="sponsor-tag-img">)?(.*?)</a><span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">(.*?)</span></span>',
        tags_html, re.M | re.S)
    # print("tags: ", tags_list)


    db = pymysql.connect("localhost", "root", "123456", "Hackathon")
    print("连接数据库成功")
    cursor = db.cursor()
    for i in tags_list:
        print(i[0], i[1])
        cursor.execute('insert into stackoverflow_tags VALUES ("%s", "%d")' % \
                   (i[0], int(i[1])))
        db.commit()  # 加入这个语句才能执行插入操作
    print("插入完毕")
    db.close()


# 抓取单个用户的标签
def get_stackoverflow_one(user_name, user_id):
    # 抓取用户标签页   https://stackoverflow.com/users/413127/blundell?tab=tags
    user_tags_url = 'https://stackoverflow.com/users/' + user_id + '/' + user_name + '?tab=tags'

    # 解决编码问题？
    try:
        user_tags_html = user_tags_html = request.urlopen(user_tags_url).read()
        user_tags_html = user_tags_html.decode('utf-8')
        # print(user_tags_html)
        user_tags_score = re.findall(r'<div class="answer-votes" title=".*?" onclick=".*?">(.*?)</div>', user_tags_html,
                                     re.S | re.M)
        user_tags_name = re.findall(
            r'<a href=".*?" class="post-tag" title=".*?">(?:<img src=".*?" height="16" width="18" alt="" class="sponsor-tag-img">)?(.*?)</a>',
            user_tags_html, re.S | re.M)
        user_tags_point = re.findall(
            r'<span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">(.*?)</span>',
            user_tags_html, re.M | re.S)

        """
        <a href=".*?" target="_blank">top <b>(.*?)</b> .*?</a>
        <a href=".*?" target="_blank">top <b>(.*?)</b> .*?</a>
        <div class="g-row -rank-link js-top"><a href=".*?" target="_blank">top <b>14%</b>
        """
        reputation = re.findall(r'<span class="g-col fl-none -rep">(.*?)</span>',user_tags_html, re.M | re.S)[0]
        print("声望： ", reputation)
        if len(user_tags_point) > 5:
            print("user_tags_list: ", user_tags_name[0], user_tags_score[0], user_tags_point[0], ",", user_tags_name[4],
                  user_tags_score[4], user_tags_point[4])

            # Django 操作数据库
            # from data_manage import models
            # models.user_tags.objects.create(username=user_name, userid=user_id, tags1=user_tags_name[0], tags2=user_tags_name[1], tags3=user_tags_name[2], tags4=user_tags_name[3])
            # models.score_tags.objects.create(tags_name=user_tags_name[0],tags_score=user_tags_score[0],tags_point=user_tags_point[0])
            # models.score_tags.objects.create(tags_name=user_tags_name[4], tags_score=user_tags_score[4],tags_point=user_tags_point[4])
            # print("已执行数据库操作")

            # python 操作数据库

            db = pymysql.connect("localhost", "root", "123456", "Hackathon")
            print("连接数据库成功")
            cursor = db.cursor()

            cursor.execute('insert into user_tags VALUES ("%s", "%s","%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s")'%\
                           (user_name, user_id, reputation, user_tags_name[0], user_tags_point[0], user_tags_name[4], user_tags_point[4], user_tags_name[2], user_tags_point[2], user_tags_name[3], user_tags_point[3]))
            db.commit()     # 加入这个语句才能执行插入操作

            cursor.execute('insert into score_tags VALUES ("%s", "%s", "%s")'%\
                           (user_tags_name[0], user_tags_score[0], user_tags_point[0]))
            db.commit()
            #
            cursor.execute('insert into score_tags VALUES ("%s", "%s", "%s")' % \
                           (user_tags_name[4], user_tags_score[4], user_tags_point[4]))
            db.commit()  # 加入这个语句才能执行插入操作
            print("插入完毕")
            db.close()

        else:
            print("该用户标签少于4")
    except:
        print("编码错误")
        pass

    # print(user_tags_html)


# 抓取10000个用户的标签页
def get_stackoverflow_all():
    # 抓取用户标签页 157247
    user_id = 513141
    """
    第一次爬取：100000~110000     开始时间：2018-5-26 23:42:53   -> 0:45     100260
    删掉重建,更改程序结构，函数嵌入，改掉链接中空格导致编码错误的bug
    
    第二次爬取：开始时间：2018-5-27 02:38:55   开始ID：413127     间隔：1   -----> 
                                                    413266  4:54
                                                    413354  -------> 415000     2018-5-27 10:27:36
     
    """

    db = pymysql.connect("111.230.55.56", "root", "123456", "hackathon")
    print("连接数据库成功")
    cursor = db.cursor()
    for i in range(10000):
        # randnum = random.randint(0,99)
        userid = str(user_id + i)
        user_url = 'https://stackoverflow.com/users/' + userid

        try:    # 第一层访问网页，若访问失败，则该id不存在用户
            res = request.urlopen(user_url)
            html = res.read().decode('utf-8')
            # bs = BeautifulSoup(html, "html.parser")
            # print(bs.title)
            # title = str(bs.title)
            username = re.findall(r'<title>User (.*?) - Stack Overflow</title>', html)[0]
            username = username.replace(' ', '-')   # 解决编码错误的问题，链接中不能存在空格，要改成‘ - ’
            # print("user: ", str(username), "id：", user_id + i)
            # get_stackoverflow_one(username, str(user_id + i))
            # userid = str(user_id + i)
            # user_name = str(username)
            user_tags_url = 'https://stackoverflow.com/users/' + userid + '/' + username + '?tab=tags'


            try:    # 第二层
                user_tags_html = user_tags_html = request.urlopen(user_tags_url).read()
                user_tags_html = user_tags_html.decode('utf-8')
                # print(user_tags_html)
                user_tags_score = re.findall(r'<div class="answer-votes" title=".*?" onclick=".*?">(.*?)</div>',
                                             user_tags_html,
                                             re.S | re.M)
                user_tags_name = re.findall(
                    r'<a href=".*?" class="post-tag" title=".*?">(?:<img src=".*?" height="16" width="18" alt="" class="sponsor-tag-img">)?(.*?)</a>',
                    user_tags_html, re.S | re.M)
                user_tags_point = re.findall(
                    r'<span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">(.*?)</span>',
                    user_tags_html, re.M | re.S)
                reputation = re.findall(r'<span class="g-col fl-none -rep">(.*?)</span>', user_tags_html, re.M | re.S)[
                    0]
                # print("reputation:", reputation)
                reputation = int(reputation.replace(',', ''))
                # print("reputation:", reputation)
                # print("声望： ", reputation)
                if len(user_tags_point) > 5:
                    # print("user_tags_list: ", user_tags_name[0], user_tags_score[0], user_tags_point[0], ",",
                    #       user_tags_name[4],
                    #       user_tags_score[4], user_tags_point[4])
                    # python 操作数据库

                    # print("转化开始")
                    # print(user_tags_score[0])
                    # print(user_tags_score[0][-1])
                    for i in range(5):
                        user_tags_point[i] = int(user_tags_point[i])
                        # print("point(int):",user_tags_point[i])

                        if (user_tags_score[i][-1] == 'k'):
                            user_tags_score[i] = int(user_tags_score[i][0:-1]) * 1000
                            # print("将k转化为1000：", user_tags_score[i])
                        else:
                            user_tags_score[i] = int(user_tags_score[i])
                    # print("转化结束")
                    cursor.execute(
                        'insert into user_tags VALUES ("%s", "%s","%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s")' % \
                        (username, userid, reputation, user_tags_name[0], user_tags_score[0], user_tags_name[4],
                         user_tags_score[4], user_tags_name[2], user_tags_score[2], user_tags_name[3],
                         user_tags_score[3]))
                    db.commit()  # 加入这个语句才能执行插入操作

                    cursor.execute('insert into score_tags VALUES ("%s", "%s", "%s")' % \
                                   (user_tags_name[0], user_tags_score[0], user_tags_point[0]))
                    db.commit()
                    #
                    cursor.execute('insert into score_tags VALUES ("%s", "%s", "%s")' % \
                                   (user_tags_name[4], user_tags_score[4], user_tags_point[4]))
                    db.commit()  # 加入这个语句才能执行插入操作
                    print(userid, "插入完毕")


                else:
                    print(userid, "标签少于4")
            except:
                print(username, "编码错误/")
                pass

        except error.URLError as e:
            print(userid, "爬取失败:链接不存在")
    db.close()


if __name__ == '__main__':
    github_url = "https://github.com/TheAlgorithms"
    csdn_url = "https://blog.csdn.net/xy294636185"
    # csdn_data = get_csdn(csdn_url)
    # github_data = get_github(github_url)

    # print(csdn_data)
    # print(github_data)

    # https://stackoverflow.com/users/413127/blundell?tab=tags

    user_id = '513141'
    user_name = 'blundell'
    # get_stackoverflow_one(user_name, user_id)
    # get_stackoverflow()
    get_stackoverflow_all()
    # db = pymysql.connect("localhost", "root", "123456", "Hackathon")
    # cursor = db.cursor()
    # cursor.execute("select version()")
    # data = cursor.fetchone()
    # print("database version: %s" % data)
    # db.close()