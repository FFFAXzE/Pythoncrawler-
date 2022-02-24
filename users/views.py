# Description:
# @File    : views.py
# @Author  : 成少雷
# @QQ      : 313728420
# @Time    : 2021/1/19 10:38
import re
from lib2to3.pgen2.grammar import line

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, redirect
from pyecharts.charts import Bar, Pie, Line, Scatter, Funnel
from pyecharts import options as opts
from pyecharts.faker import Faker
from sqlalchemy import func

from users.models import db, Tbbeike, TbShorts, MoviesInfo, TbPopulation
# from users.models import TbStudent
from pyecharts.globals import ThemeType         # 内置主题类型

user = Blueprint("user", __name__)

# @user.route("/")
# def home():
#     return "首页"

# 添加数据
#
# @user.route("/add/")
# def add_list():
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
#     for i in range(0, 101, 20):
#         url = "https://movie.douban.com/subject/1292722/comments?start={}&limit=20&status=P&sort=new_score".format(i)
#         response = requests.get(url=url, headers=headers)
#         bs = BeautifulSoup(response.content, "html5lib")
#
#         users = bs.select('.comment-info a')
#         users = [tag.text.strip() for tag in users]
#
#         views = bs.select('.rating')
#         k = 0
#         for value in views:
#             views[k] = value.attrs["title"]
#             k += 1
#
#         j = 0
#         for value in views:
#             if (value == "力荐") or (value == "推荐"):
#                 views[j] = 1
#             elif value == "还行":
#                 views[j] = 2
#             else:
#                 views[j] = 3
#             j += 1
#         # print(views)
#         #
#         times = bs.select('.comment-time')
#         k = 0
#         for value in times:
#             times[k] = value.attrs["title"]
#             k += 1
#
#         votes = bs.select('.votes')
#         votes = [tag.text.strip() for tag in votes]
#
#         shorts = bs.select('.short')
#         shorts = [tag.text.strip() for tag in shorts]
#         k=0
#         for value in users:
#             s1=TbShorts(userid=k+i,users=users[k],views=views[k],times=times[k],votes=votes[k],shorts=shorts[k])
#             try:
#                 TbShorts.save_all(s1)
#             except Exception as e:
#                 print(e)
#             k+=1
#
#     return "插入成功"

@user.route("/add/")
def add_beike():
    j=1
    for pages in range(1, 10):
        url = "https://www.douban.com/doulist/1641439/?start=" + str(pages * 25) + "&sort=seq&playable=0&sub_type="
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        response = requests.get(url, headers=headers)
        bs = BeautifulSoup(response.content, "html5lib")
        mname = []
        rate = []
        details = []
        date = []

        # print(bs)

        for i in bs.find_all('div', class_='bd doulist-subject'):
                mname.append(i.select(".title>a")[0].get_text().replace(' ', '').replace('\n', ''))
                rate.append(i.select(".rating_nums")[0].get_text().replace(' ', '').replace('\n', ''))
                details.append(i.select(".abstract")[0].get_text().replace(' ', '').replace('\n', ''))
        for i in bs.find_all('div', class_='ft'):
                date.append(i.select(".actions>.time>span")[0].get_text().replace(' ', '').replace('\n', ''))
        # print(mname)

        for a in range(len(mname)):
            s1 = MoviesInfo(id=j, mName=mname[a], pf=rate[a], detial=details[a], Dtime=date[a])
            j+=1
            db.session.add(s1)
            db.session.commit()
            # MoviesInfo.save(s1)
            print(s1)
            print(j)
            print(mname[a])
            print(rate[a])
            print(details[a])
            print(date[a])
        # # print(bs)
        # content = bs.select(
        #          "#content > div > div.article")
        # # print(content)
        # for tag in content:
        #          mname = tag.select("div.bd.doulist-subject > div.title > a")
        #          rate = tag.select(" div.bd.doulist-subject > div.rating > span.rating_nums")
        #          details = tag.select(" div.bd.doulist-subject > div.abstract")
        #          date = tag.select("div.ft > div.actions > time > span")
        #          # print(mname)
        #
        #          mname = "\n".join([tag.text.strip() for tag in  mname])
        #          rate = "\n".join([tag.text.strip() for tag in rate ]).replace(" ", "").replace("\n", "")
        #          details = "\n".join([tag.text.strip() for tag in details]).replace(" ", "").replace("\n", "")
        #          date = "\n".join([tag.text.strip() for tag in date]).replace(" ", "").replace("\n", "")
        #          k=0
        #          for value in mname:
        #             s1 = MoviesInfo(id=k+pages*25, mName=mname[k], pf=rate[k], detial=details[k], Dtime=date[k])
        #
        #             print(mname)
        #             print(rate)
        #             print(details)
        #             print(date,"\n")
        #             db.session.add(s1)
        #             k=k+1
    return "插入一个记录"
    # url = "https://cd.ke.com/ershoufang/"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    # j=1
    # for i in range(1, 10):
    #     url = "https://cd.ke.com/ershoufang/pg{}/".format(i)
    #     print(url)
    #     response = requests.get(url=url, headers=headers)
    #     bs = BeautifulSoup(response.content, "html5lib")
    #     content = bs.select(
    #         "#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul > li> div")
    #     for tag in content:
    #
    #         title = tag.select("div.title > a")
    #         position = tag.select("div.address > div.flood > div")
    #         houseInfo = tag.select("div.address > div.houseInfo")
    #         followInfo = tag.select(" div.address > div.followInfo")
    #         totalPrice = tag.select(" div.address > div.priceInfo > div.totalPrice > span")
    #         unitPrice = tag.select("div.address > div.priceInfo > div.unitPrice > span")
    #
    #         title = "\n".join([tag.text.strip() for tag in title]).replace("\n", "")
    #         position = "\n".join([tag.text.strip() for tag in position]).replace(" ", "").replace("\n", "")
    #         houseInfo = "\n".join([tag.text.strip() for tag in houseInfo]).replace(" ", "").replace("\n", "")
    #         followInfo = "\n".join([tag.text.strip() for tag in followInfo]).replace(" ", "").replace("\n", "")
    #         totalPrice = "\n".join([tag.text.strip() for tag in totalPrice])
    #         totalPrice1 = float(totalPrice)
    #         unitPrice = "\n".join([tag.text.strip() for tag in unitPrice])
    #         unitPrice =re.sub("\D", "", unitPrice)
    #         unitPrice = float(unitPrice)
    #         s1 = Tbbeike(id=j, position=position, title=title, houseInfo=houseInfo, totalPrice=totalPrice1, unitPrice=unitPrice)
    #         j=j+1
    #         print(title)
    #         print(position)
    #         print(houseInfo)
    #         print(followInfo)
    #         print(totalPrice)
    #         print(unitPrice, "\n")
    #         db.session.add(s1)
    #         # db.session.commit()  # 手动提交
    #         # db.session.rollback()  # 回滚

    # return "插入一个记录"

@user.route("/drawecharts/")
def drawecharts():
    positionList = []
    totalPriceList = []
    averageList = []

    data = db.session.query(Tbbeike.position).all()
    data1 = db.session.query(Tbbeike.totalPrice).all()
    average1 = db.session.query(Tbbeike.unitPrice).all()
    for data2 in data:
        positionList.append(data2[0])
        # print(positionList[len(positionList)-1])
    for data3 in data1:
        totalPriceList.append(data3[0] * 10000)
    for data4 in average1:
        averageList.append((data4[0]))

    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    # x为地理位置，y为房价
    bar.add_xaxis(positionList)
    bar.add_yaxis("房价", totalPriceList, category_gap="50%")
    bar.add_yaxis("平米价",averageList,category_gap="50%")
    # line = Line()
    # line.add_xaxis(positionList)
    # line.add_yaxis("每平价格", averageList)
    print(averageList)
    print(totalPriceList)
    print(positionList)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="成都二手房房价"),
                        yaxis_opts=opts.AxisOpts(name="单位:元"),  # 设置y轴名字，x轴同理
                        xaxis_opts=opts.AxisOpts(name="地理位置"),
                        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")] # 设置水平缩放，默认可滑动(*好东西)
                        )
    # 标记峰值
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_='max', name='最大值'),  # 最大值标记点
                opts.MarkPointItem(type_='min', name='最小值'),  # 最小值标记点
                opts.MarkPointItem(type_='average', name='平均值')  # 平均值标记点
            ]
        )
    )

    # return render_template("cd.html")

    return bar.dump_options_with_quotes()

@user.route("/cdScatter/")
def cdScatter():
    data = db.session.query(Tbbeike.position).all()
    data1 = db.session.query(Tbbeike.totalPrice).all()
    average1 = db.session.query(Tbbeike.unitPrice).all()
    positionList=[]
    totalPriceList=[]
    averageList=[]
    for data2 in data:
        positionList.append(data2[0])
        # print(positionList[len(positionList)-1])
    for data3 in data1:
        totalPriceList.append(data3[0]*10000)
    for data4 in average1:
        averageList.append((data4[0]))

    c = (
        Scatter()
            .add_xaxis(positionList)
            .add_yaxis("每平米价格", averageList)
            .add_yaxis("总价格",totalPriceList)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="成都二手房价格分布图"),
            visualmap_opts=opts.VisualMapOpts(max_=50000,min_=3000),
            datazoom_opts=opts.DataZoomOpts()  # 设置水平缩放，默认可滑动
        )
        # .render("templates/average.html")
    )
    return c.dump_options_with_quotes()

@user.route("/position/")
def position():
    data = db.session.query(Tbbeike.position).all()
    data1 = db.session.query(Tbbeike.totalPrice).all()
    average1 = db.session.query(Tbbeike.unitPrice).all()
    positionList = []
    totalPriceList = []
    averageList = []
    for data2 in data:
        positionList.append(data2[0])
        # print(positionList[len(positionList)-1])
    for data3 in data1:
        totalPriceList.append(data3[0] * 10000)
    for data4 in average1:
        averageList.append((data4[0]))

    c1 = (
        Funnel()
            .add(
            "位置",
            [list(z) for z in zip(positionList, Faker.values())],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="地区分布情况"))
            # .render("templates/position.html")
    )
    return c1.dump_options_with_quotes()

@user.route("/query/")
def query_student():
    alldata1 = TbShorts.query.order_by(-TbShorts.userid).all()
    alldata2 = TbShorts.query.order_by(-TbShorts.userid).all()

    nice = 0
    gen = 0
    bad = 0
    for value in alldata1:
        if value.views==1:
            nice+=1
        elif value.views==2:
            gen+=1
        else:
            bad+=1
    print(nice,gen,bad)
    data = [('好评', nice), ('一般', gen), ('差评', bad)]
    pie=Pie()
    pie.add(
        # 设置系列名称
        series_name='观影评价',
        # 设置需要展示的数据
        data_pair=data,
        # 设置圆环空⼼部分和数据显示部分的⽐例
        radius=['30%', '70%'],
        # 设置饼是不规则的
        # rosetype='radius'
    )
    pie.set_colors(["#2EC7C9","#B6A2DE","#5AB1EF"])
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}：{d} % '))
    # 设置图表的标题
    pie.set_global_opts(title_opts=opts.TitleOpts(title='观影评价'))
    # 5. 渲染数据
    return pie.dump_options_with_quotes()

@user.route("/XZFA/")
def query_studentA():
    alldata1 = TbShorts.query.order_by(-TbShorts.userid).all()
    alldata2 = TbShorts.query.order_by(-TbShorts.userid).all()

    votes=alldata1
    users=alldata2
    i=0
    for value in votes:
        votes[i]=value.votes
        i+=1
    i=0
    for value in users:
        users[i]=value.users
        i+=1
    bar=Bar({"theme": ThemeType.MACARONS})
    bar.add_xaxis(users)  # 确定x轴上要显示的内容
    bar.add_yaxis('票数', votes)
    # bar.set_colors("purple")
    bar.is_datazoom_show = True # 显示 dataZoom控制条;

    # 全局设置
    bar.set_global_opts(
        # 设置标题信息
        title_opts=opts.TitleOpts(title='泰坦尼克号',subtitle='用户短评被采纳度',),

        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        xaxis_opts = opts.AxisOpts(name="用户"),
    )
    # 系列设置
    bar.set_series_opts(
        # 设置是否显示数值
        label_opts=opts.LabelOpts(is_show=False),
        # 添加标记点
        markpoint_opts=opts.MarkPointOpts(data=[
            opts.MarkPointItem(type_='min', name='最⼩值'),
            opts.MarkPointItem(type_='max', name='最⼤值')
        ]))
    # 5. 数据渲染 - ⽣成图表
    # bar.render('templates/view2.html')
    return bar.dump_options_with_quotes()

@user.route("/XTZ1/")
def DianYing():
    mName = []
    pf = []
    # averageList = []

    data = db.session.query(MoviesInfo.mName).all()
    print(data)
    data1 = db.session.query(MoviesInfo.pf).all()
    # average1 = db.session.query(Tbbeike.unitPrice).all()
    for data2 in data:
        mName.append(data2[0])
        # print(positionList[len(positionList)-1])
    for data3 in data1:
        pf.append(data3[0])
    # for data4 in average1:
    #     averageList.append((data4[0]))

    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    # x为地理位置，y为房价
    bar.add_xaxis(mName)
    bar.add_yaxis("评分", pf, category_gap="50%")
    print(mName)
    print(pf)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="电影评分"),
                        yaxis_opts=opts.AxisOpts(name="分"),  # 设置y轴名字，x轴同理
                        xaxis_opts=opts.AxisOpts(name="电影名"),
                        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")] # 设置水平缩放，默认可滑动(*好东西)
                        )
    # 标记峰值
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_='max', name='最大值'),  # 最大值标记点
                opts.MarkPointItem(type_='min', name='最小值'),  # 最小值标记点
                opts.MarkPointItem(type_='average', name='平均值')  # 平均值标记点
            ]
        )
    )

    # return render_template("cd.html")

    return bar.dump_options_with_quotes()

@user.route("/HDW1/")
def query_shorts2():
    alldata1 = TbPopulation.query.order_by(-TbPopulation.id).all()
    alldata2 = TbPopulation.query.order_by(-TbPopulation.id).all()
    alldata3 = TbPopulation.query.order_by(-TbPopulation.id).all()
    alldata4 = TbPopulation.query.order_by(-TbPopulation.id).all()
    alldata5 = TbPopulation.query.order_by(-TbPopulation.id).all()
    alldata6 = TbPopulation.query.order_by(-TbPopulation.id).all()
    pro=alldata5
    total15=alldata6
    male15=alldata1
    female15=alldata2
    maleNotMarry=alldata3
    femaleNotMarry = alldata4
    i=0
    for value in maleNotMarry:
        pro[i] = value.pro
        male15[i]=value.male15
        female15[i]=value.female15
        maleNotMarry[i]=value.maleNotMarry
        femaleNotMarry[i] = value.femaleNotMarry
        total15[i]=value.total15
        i+=1

    print(total15)
    print(male15)
    print(female15)
    line = (
        Line()
            .add_xaxis(xaxis_data=pro)
            .add_yaxis(
            series_name="15岁及以上人口",
            # yaxis_index=1,
            y_axis= total15,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="15岁及以上男性人口",
            # yaxis_index=1,
            y_axis=male15,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="15岁及以上女性人口",
            # yaxis_index=1,
            y_axis=female15,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    bar=Bar({"theme": ThemeType.MACARONS})
    bar.add_xaxis(pro)  # 确定x轴上要显示的内容
    bar.add_yaxis("未婚男性", maleNotMarry, stack="stack1", category_gap="50%")
    bar.add_yaxis("未婚女性", femaleNotMarry, stack="stack1", category_gap="50%")
    # bar.set_colors("purple")
    bar.is_datazoom_show = True # 显示 dataZoom控制条;
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title='各地区人口'),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        xaxis_opts = opts.AxisOpts(name="省份"),
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(data=[
            opts.MarkPointItem(type_='min', name='最⼩值'),
            opts.MarkPointItem(type_='max', name='最⼤值')
        ])
    )
    # bar.overlap(line).render('templates/view2.html')
    # return render_template("view2.html", **locals())
    return bar.overlap(line).dump_options_with_quotes()

@user.route("/")
def zhuye():
    return render_template("index.html")
