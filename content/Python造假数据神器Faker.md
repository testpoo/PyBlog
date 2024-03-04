title: Python造假数据神器Faker
date: 2024-02-27
category: python
tag: faker

[TOC]

### 1. 简介

Faker 是一个 Python 包，可以为您生成虚假数据。无论您是需要引导数据库，创建外观漂亮的 XML 文档，填写持久性来对其进行压力测试，还是匿名化从生产服务中获取的数据，Faker 都适合您。

#### **1.1. 安装**

    pip install Faker

#### 1.2 查看帮助

    (faker) E:\project\faker>faker -h
    usage: faker [-h] [--version] [-v] [-o output] [-l LOCALE] [-r REPEAT] [-s SEP] [--seed SEED] [-i [INCLUDE ...]] [fake] [fake argument ...]

    faker version 23.2.1

    positional arguments:
      fake                  name of the fake to generate output for (e.g. profile)
      fake argument         optional arguments to pass to the fake (e.g. the profile fake takes an optional list of comma separated field names as the first argument)

    options:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v, --verbose         show INFO logging events instead of CRITICAL, which is the default. These logging events provide insight into localization of specific providers.
      -o output             redirect output to a file
      -l LOCALE, --lang LOCALE
                            specify the language for a localized provider (e.g. de_DE)
      -r REPEAT, --repeat REPEAT
                            generate the specified number of outputs
      -s SEP, --sep SEP     use the specified separator after each output
      --seed SEED           specify a seed for the random generator so that results are repeatable. Also compatible with 'repeat' option
      -i [INCLUDE ...], --include [INCLUDE ...]
                            list of additional custom providers to user, given as the import path of the module containing your Provider class (not the provider class itself)

    supported locales:

      ar_AA, ar_AE, ar_BH, ar_EG, ar_JO, ar_PS, ar_SA, az_AZ, bg_BG, bn_BD, bs_BA, cs_CZ, da_DK, de, de_AT, de_CH, de_DE, dk_DK, el_CY, el_GR, en, en_AU, en_BD, en_CA, en_GB, en_IE, en_IN, en_NZ, en_PH, en_TH, en_US, es, es_AR, es_CA, es_CL, es_CO, es_ES, es_MX, et_EE, fa_IR, fi_FI, fil_PH, fr_BE, fr_CA, fr_CH, fr_FR, fr_QC, ga_IE, he_IL, hi_IN, hr_HR, hu_HU, hy_AM, id_ID, it_CH, it_IT, ja_JP, ka_GE, ko_KR, la, lb_LU, lt_LT, lv_LV, mt_MT, ne_NP, nl_BE, nl_NL, no_NO, or_IN, pl_PL, pt_BR, pt_PT, ro_RO, ru_RU, sk_SK, sl_SI, sq_AL, sv_SE, ta_IN, th, th_TH, tl_PH, tr_TR, tw_GH, uk_UA, vi_VN, zh_CN, zh_TW, zu_ZA

      Faker can take a locale as an optional argument, to return localized data. If
      no locale argument is specified, the factory falls back to the user's OS
      locale as long as it is supported by at least one of the providers.
         - for this user, the default locale is en_US.

      If the optional argument locale and/or user's default locale is not available
      for the specified provider, the factory falls back to faker's default locale,
      which is en_US.

    examples:

      $ faker address
      968 Bahringer Garden Apt. 722
      Kristinaland, NJ 09890

      $ faker -l de_DE address
      Samira-Niemeier-Allee 56
      94812 Biedenkopf

      $ faker profile ssn,birthdate
      {'ssn': u'628-10-1085', 'birthdate': '2008-03-29'}

      $ faker -r=3 -s=";" name
      Willam Kertzmann;
      Josiah Maggio;
      Gayla Schmitt;

#### 1.3 官方文档

faker官方文档：<https://faker.readthedocs.io/en/latest/index.html>

### **2. 简单使用**

    >>> from faker import Faker
    >>> fake = Faker(locale='zh_CN')
    >>> fake.name()
    '曹洋'
    >>> fake.address()
    '西藏自治区玉英县六枝特长春街m座 669309'

### 3. 参数 locale

参数为生成数据的文化选项（语种），默认为 en\_US，只有使用了相关文化，才能生成相对应的随机信息。

| 参数     | 说明     | 用法                      |
| :----- | :----- | :---------------------- |
| zh\_CN | 中文简体   | Faker(locale\='zh\_CN') |
| zh\_TW | 中文繁体   | Faker(locale\='zh\_TW') |
| en\_US | 英语（美国） | Faker(locale\='en\_US') |
| en\_GB | 英语（英国） | Faker(locale\='en\_GB') |
| de\_DE | 德语     | Faker(locale\='de\_DE') |
| ja\_JP | 日语     | Faker(locale\='ja\_JP') |
| ko\_KR | 韩语     | Faker(locale\='ko\_KR') |
| fr\_FR | 法语     | Faker(locale\='fr\_FR') |
| es\_ES | 西班牙语   | Faker(locale\='zh\_CN') |
| ……     | ……     | ……                      |

还有很多其他的语言，部分列举

### **4. 其他方法**

#### **4.1 地理信息类**

```Python
city_suffix()：市，县
# 市 或 县
country()：国家
# 葡萄牙
country_code()：国家编码
# IN
district()：区
# 黄浦
coordinate()：地理坐标
# Decimal('-6.314017')
latitude()：地理坐标(纬度)
# Decimal('-52.842700')
longitude()：地理坐标(经度)
# Decimal('-103.420509')
postcode()：邮编
# 930438
province()：省份
# 贵州省
address()：详细地址
# 江西省荆门市山亭宜都街G座 379902
street_address()：街道地址
# 王路H座
street_name()：街道名
# 刘路
street_suffix()：街、路
# 街 或 路
```

#### **4.2 基础信息类**

```Python
ssn()：生成身份证号
# 460105195602289565
bs()：随机公司服务名
# synthesize wireless channels
company()：随机公司名（长）
# 快讯科技有限公司
company_prefix()：随机公司名（短）
# 时刻
company_suffix()：公司性质，如'信息有限公司'
# 传媒有限公司
credit_card_expire()：随机信用卡到期日，如'03/30'
# 08/27
credit_card_full()：生成完整信用卡信息
# VISA 13 digit
# 佳 魏
# 4510659631299 09/27
# CVC: 292
credit_card_number()：信用卡号
# 4841223722482
credit_card_provider()：信用卡类型
# Mastercard
credit_card_security_code()：信用卡安全码
# 511
job()：随机职位
# 临床协调员
first_name()：第一个名字
# 莉
first_name_female()：女性名
# 军
first_name_male()：男性名
# 军
first_romanized_name()：罗马名
# ping
last_name()：最后一个名字
# 谢
last_name_female()：女姓
# 韩
last_name_male()：男姓
# 顾
last_romanized_name()：罗马姓氏
# Feng
name()：随机生成全名
# 彭华
name_female()：男性全名
# 任宁
name_male()：女性全名
# 王俊
romanized_name()：罗马名
# Juan Sun
msisdn()：移动台国际用户识别码，即移动用户的ISDN号码
# 9271661830556
phone_number()：随机生成手机号
# 15237436258
phonenumber_prefix()：随机生成手机号段，如139
# 180
```

#### **4.3 邮箱信息类**

```Cython
ascii_company_email()：随机ASCII公司邮箱名
# ming81@wangwang.cn
ascii_email()：随机ASCII邮箱
# xiamin@guiyingjing.cn
ascii_free_email()：随机ASCII免费邮箱
# yan93@gmail.com
ascii_safe_email()：随机ASCII安全邮箱
# yeyan@example.com
company_email()：公司邮箱
# yong66@leizheng.cn
email()：普通邮箱
# leixiang@example.net
free_email()：免费邮箱
# osun@gmail.com
free_email_domain()：免费邮箱域
# http://hotmail.com
safe_email()：安全邮箱
# wdu@example.org
```

#### **4.4 网络基础信息类**

```Cython
domain_name()：生成域名
# jing.cn
domain_word()：域词(即，不包含后缀)
# qiang
ipv4()：随机IP4地址
# 188.216.215.251
ipv6()：随机IP6地址
# df53:6891:74b9:7177:98ec:44b3:3498:7c69
mac_address()：随机MAC地址
# f0:1e:24:b3:b7:e8
tld()：网址域名后缀(.com,.net.cn,等等，不包括.)
# cn
uri()：随机URI地址
# http://46.cn/searchindex.php
uri_extension()：网址文件后缀
# .php
uri_page()：网址文件（不包含后缀）
# main
uri_path()：网址文件路径（不包含文件名）
# search/category
url()：随机URL地址
# https://www.rencao.cn/
user_name()：随机用户名
# jgao
image_url()：随机URL地址
# https://picsum.photos/619/449
```

#### **4.5 浏览器信息类**

```Cython
chrome()：随机生成Chrome的浏览器user_agent信息
# Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/16.0.879.0 Safari/533.1
firefox()：随机生成FireFox的浏览器user_agent信息
# Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_12_2; rv:1.9.3.20) Gecko/8618-06-21 05:10:08 Firefox/3.6.4
internet_explorer()：随机生成IE的浏览器user_agent信息
# Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Win 9x 4.90; Trident/3.0)
opera()：随机生成Opera的浏览器user_agent信息
# Opera/8.47.(Windows NT 6.1; kok-IN) Presto/2.9.178 Version/12.00
safari()：随机生成Safari的浏览器user_agent信息
# Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_6 rv:5.0; mr-IN) AppleWebKit/535.25.4 (KHTML, like Gecko) Version/4.1 Safari/535.25.4
linux_platform_token()：随机Linux信息
# X11; Linux i686
user_agent()：随机user_agent信息
# Mozilla/5.0 (Windows; U; Windows 98; Win 9x 4.90) AppleWebKit/534.34.6 (KHTML, like Gecko) Version/5.1 Safari/534.34.6
```

#### **4.6 数字信息**

```Cython
numerify()：三位随机数字
# 865
random_digit()：0~9随机数
# 5
random_digit_not_null()：1~9的随机数
# 7
random_int()：随机数字，默认0~9999，可以通过设置min,max来设置
# 2497
random_number()：随机数字，参数digits设置生成的数字位数
# 25011312
pyfloat()：随机Float数字
# 955.707810796746
pyint()：随机Int数字（参考random_int()参数）
# 2673
pydecimal()：随机Decimal数字（参考pyfloat参数）
# 9371388754385663915393032330587677.707987943449603003369594742167786
```

#### **4.7 文本加密类**

```Cython
pystr()：随机字符串
# VXaBYNWVfBNuvoLNAkYc
random_element()：随机字母
# c
random_letter()：随机字母
# R
paragraph()：随机生成一个段落
# 男人安全质量一起程序业务起来.因此非常浏览基本.
paragraphs()：随机生成多个段落
# ['女人任何在线登录到了精华管理.功能这个来源学生选择根据孩子.工具决定内容法律基本查看.', '不断有限大小下载.作者本站注意其中等级然后觉得.需要语言孩子作者手机积分.', '合作操作选择.希望同时决定最大管理.一次业务软件只是社区因为查看.密码在线加入 显示这么.']
sentence()：随机生成一句话
# 最后回复就是上海出现不同.
sentences()：随机生成多句话，与段落类似
# ['表示标题如果那些地区质量电话.', '东西这个责任完全.', '一起影响留言类型有限来自只有.']
text()：随机生成一篇文章
# 情况北京城市.技术没有可以安全政府完全电影.注意设备科技.
# 主题已经或者的人.方式信息如果关于看到不是.留言报告详细标题相关基本.
# 表示有些他们这里.制作就是成为方法希望他的电子单位.过程语言论坛可是.
# 法律客户程序报告有限只要表示.最新时候无法计划.目前相关不是深圳我的.
# 密码包括那么.地址一直说明商品.
# 一点显示设备最新最大功能我的国内.日期知道原因.目前朋友重要.
word()：随机生成词语
# 活动
words()：随机生成多个词语，用法与段落，句子，类似
# ['朋友', '经验', '出现']
binary()：随机生成二进制编码
boolean()：True/False
# False
language_code()：随机生成两位语言编码
# iu
locale()：随机生成语言/国际 信息
# kw_GB
md5()：随机生成MD5
# 56065e546f9cf078702e713c6981ce35
null_boolean()：NULL/True/False
# True
password()：随机生成密码,可选参数：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母
# $68W0+xp$+
sha1()：随机SHA1
# 3030de488299d4ed76806447e3741201ba9a326a
sha256()：随机SHA256
# 42bc239bd183f2e3f60ec54fceabc2eca4074f8d3598bedd685985d20c863e07
uuid4()：随机UUID
# c0424eb8-6793-42fa-b2b8-01ce7d5db3c9
```

#### 4.8 文件信息类

```Shell
file_extension()：随机文件扩展名
# json
file_name()：随机文件名（包含扩展名，不包含路径）
# 这是.
gif file_path()：随机文件路径（包含文件名，扩展名）
# /新闻/具有.
odp mime_type()：随机mime Type
# multipart/related
```

#### 4.9 时间信息类

```Cython
am_pm()：AM/PM
# PM
century()：随机世纪
# XII
date()：随机日期
# 2001-04-07
date_between()：随机生成指定范围内日期，参数：start_date，end_date取值：具体日期或者today,-30d,-30y类似
# 2011-04-21
date_between_dates()：随机生成指定范围内日期，用法同上
# 2022-11-15
date_object()：随机生产从1970-1-1到指定日期的随机日期。
# 2014-12-12
date_this_month()：现在这个月的日期
# 2022-11-12
date_this_year()：现在这一年的日期
# 2022-02-16
date_time()：随机生成指定时间（1970年1月1日至今）
# 1988-07-07 04:42:25
date_time_ad()：生成公元1年到现在的随机时间
# 1658-11-20 09:19:22
date_time_between()：用法同dates
# 2001-06-05 01:11:45
future_date()：未来日期
# 2022-12-02
future_datetime()：未来时间
# 2022-11-28 06:07:21
month()：随机月份
# 10
month_name()：随机月份（汉语）
# 十二月
past_date()：随机生成已经过去的日期
# 2022-11-06
past_datetime()：随机生成已经过去的时间
# 2022-10-28 18:36:07
time()：随机24小时时间
# 05:58:43
timedelta()：随机获取时间差
# /
time_object()：随机24小时时间，time对象
# 19:28:21
time_series()：随机TimeSeries对象
# <generator object Provider.time_series at 0x7fc346f30190>
timezone()：随机时区
# America/Noronha
unix_time()：随机Unix时间
# 55170123
year()：随机年份
# 1979
```

#### 4.10 集合信息类

```Cython
profile()：随机生成档案信息
# {'job': '高级建筑工程师/总工', 'company': '诺依曼软件传媒有限公司', 'ssn': '230822195904280066', 'residence': '湖南省玉梅县高明符路J座 227449', 'current_location': (Decimal('75.297849'), Decimal('-0.733280')), 'blood_group': 'A+', 'website': ['https://guiyingxiulan.cn/', 'http://yanxiuying.net/'], 'username': 'yangliu', 'name': '徐玉梅', 'sex': 'F', 'address': '甘肃省红霞市永川李路K座 215966', 'mail': 'wliang@hotmail.com', 'birthdate': datetime.date(1960, 11, 28)}
simple_profile()：随机生成简单档案信息
# {'username': 'qianghuang', 'name': '董阳', 'sex': 'F', 'address': '澳门特别行政区沈阳市东城东莞街n座 902934', 'mail': 'guiying78@hotmail.com', 'birthdate': datetime.date(1928, 10, 19)}

```

### **5. 实战使用**

在数据库建一张表，通过Faker造数据，插入到表中。并且打印Faker造的数据。

```Python
# coding=utf-8

from faker import Faker
import sqlite3
 
# 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect('faker.db')
cursor = conn.cursor()

# 表存在先删除
delete_exists_table = """drop table if exists faker_user"""
cursor.execute(delete_exists_table)

# 创建表格
create_table_query = '''CREATE TABLE IF NOT EXISTS faker_user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, address TEXT)'''
cursor.execute(create_table_query)

fake = Faker(locale='zh_CN')

# 插入数据
for i in range(20):
    sql = """insert into faker_user(username,password,address) 
    values('%s','%s','%s')""" % (fake.name(), fake.password(special_chars=False), fake.address())
    cursor.execute(sql)
 
# 提交更改
conn.commit()
 
# 查询数据
select_data_query = 'SELECT * FROM faker_user'
cursor.execute(select_data_query)
result = cursor.fetchall()
for row in result:
    print("姓名:{}|密码:{}|地址:{}".format(row[1], row[2], row[3]))
 
# 关闭连接
cursor.close()
conn.close()
```

输出的结果如下：

```Shell
姓名:马梅|密码:2hGP8eC186|地址:辽宁省拉萨县永川哈尔滨街I座 857047
姓名:谭荣|密码:msBdcfeiZ3|地址:广东省成县海陵北镇路q座 413065
姓名:陈俊|密码:nyULGcNf8g|地址:湖北省玲县璧山凌街z座 953074
姓名:单峰|密码:w4WOAZzyx2|地址:青海省合山市兴山福州街h座 756882
姓名:许亮|密码:2ABJj4d0AH|地址:福建省淑华县东丽侯街r座 882820
姓名:杨娟|密码:xVwtOOCl2l|地址:湖北省海门县南溪苏路K座 405426
姓名:李文|密码:5p8RTukwUw|地址:重庆市北京市安次杭州路A座 109157
姓名:颜杰|密码:8SjPmLZtaB|地址:山东省福州县兴山赵街g座 375532
姓名:宋玉英|密码:pNIPLaNeN7|地址:贵州省辛集市滨城邝路o座 250860
姓名:吴慧|密码:9kXieqeeXX|地址:四川省建县萧山太原街Q座 687935
姓名:杨岩|密码:eViwelXs9m|地址:宁夏回族自治区红梅县新城黄路M座 248851
姓名:胡东|密码:HTVi6KVxD6|地址:安徽省秀芳市高港南昌路z座 391643
姓名:古玉|密码:ndlGJS8uS8|地址:宁夏回族自治区北京市花溪陈路h座 217657
姓名:李丽|密码:K6GYm0PQi5|地址:宁夏回族自治区嘉禾市清城陈路n座 754327
姓名:孙桂珍|密码:NScteUAeX1|地址:河南省莉县东丽南宁路R座 968642
姓名:何秀英|密码:7h6VzJ8u25|地址:香港特别行政区金凤市永川嘉禾路m座 814796
姓名:黄玲|密码:7CPxLtH8WK|地址:上海市昆明市涪城王路J座 734183
姓名:高林|密码:NRm011Zb4H|地址:海南省玉英县东城袁路i座 168381
姓名:陆兰英|密码:7e6Q3nltOt|地址:山西省天津市高坪李路A座 605319
姓名:杨杨|密码:84LWBXxhK1|地址:辽宁省宜都县徐汇邯郸路k座 372826
```

