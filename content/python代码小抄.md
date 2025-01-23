title:python代码小抄
date:2024-08-13
category: 代码小抄
tag:python

[TOC]

###  获取Linux程序名称/命令/图标/分类

```
path = "/usr/share/applications/"
lists = [list for list in os.listdir(path) if len(list.split("."))>1 and list.split(".")[1] == "desktop"]
apps = []
for list in lists:
    lines = open(path + list,"r").readlines()
    dicts = {}
    for line in lines:
        if line.startswith("Name="):
            dicts['Name'] = re.split("=|\n",line)[1]
        elif line.startswith("Name[zh_CN]="):
            dicts['NameCN'] = re.split("=|\n",line)[1]
        elif line.startswith("Exec="):
            dicts['Exec'] = re.sub(" %U| %F| %f| %u","",re.split("=|\n",line)[1])
        elif line.startswith("Icon="):
            dicts['Icon'] = re.split("=|\n",line)[1]
        elif line.startswith("Categories="):
            dicts['Categories'] = re.split("=|\n",line)[1]
        elif line.startswith("[Desktop Action"):
            break
    if 'NameCN' in dicts:
        dicts['Name'] = dicts['NameCN']
        dicts.pop('NameCN')
    if dicts != {} and 'Icon' in dicts:
        apps.append(dicts)
```
<hr />
###  获取Linux程序图标

```
# directries第一个元素是当前图标
directries = ["/usr/share/icons/Yaru/48x48/","/usr/share/icons/gnome/48x48/","/usr/share/pixmaps/","/usr/share/icons/hicolor/scalable/","/usr/share/icons/hicolor/48x48/","/opt/"]

def find_images_glob(self,directries,event=None):
    image_paths={}
    for directry in directries:
        for dirpath, dirnames, filenames in os.walk(directry):
            for app in apps:
                if app['Icon']+".png" in filenames:
                    if app['Icon']+".png" not in image_paths:
                        image_paths[app['Icon']] = dirpath + "/" + app['Icon']+".png"
                elif app['Icon']+".svg" in filenames:
                    if app['Icon']+".svg" not in image_paths:
                        image_paths[app['Icon']] = dirpath + "/" + app['Icon']+".svg"
                elif len(app['Icon'].split("/"))>1:
                    if app['Icon'].split("/")[-1] not in image_paths:
                        image_paths[app['Icon'].split("/")[-1].split('.')[0]] = app['Icon']
    return image_paths
```
<hr />
###  如何确定在tkinter中单击了哪个按钮

```
方法1：
from functools import partial

for i in range(10):
    btn = Button(frame,text="Button",command=partial(click, i))

方法2：
for i in range(10):
    btn = Button(frame,text="Button",command=lambda i=i: click(i))
```
<hr />
###  python定时任务
```
#!/usr/bin/env python
import time
 
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime()) # 刷新
    if time_now == "09:39:00": 
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  
        time.sleep(2) # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
```
<hr />
###  JinJa2代码

```
# 注册过滤器
env = app.jinja_env
env.filters["sum_car_food_by_category"] = sum_car_food_by_category

# 全局变量设置
@app.context_processor
def getSiteUrl():
    return dict(SITEURL=SITEURL)

# app执行前执行
@app.before_request
def authority():
    path = request.path
    if not session.get('logged_in'):
        if path not in ('/', '/login') and not path.startswith('/static'):
            return redirect(url_for('login'))
    elif session.get('logged_in'):
        if ''.join(['/',path.split("/")[1]]) not in auths(session['username']):
            return redirect(url_for('unPlan'))
```

<hr />
###  MySQL数据库连接

```
import pymysql

dblink = {"url": "127.0.0.1", "username": "test", "password": "11111111", "database": "test"}
def selectOne(sql, info=[]):
    try:
        # 连接MySQL数据库
        db = pymysql.connect(host=dblink['url'], user=dblink['username'], password=dblink['password'],db=dblink['database'], charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute()方法执行sql语句
        cursor.execute(sql, info)
        # 使用fetchone()方法获取所有数据
        results = cursor.fetchall()
        return results
    except Exception as err:
        logUtility.logger.debug("事务处理失败: {}".format(str(err)))
        return '事务处理失败'
    else:
        LogUtility.logger.debug("事务处理成功")
    # 关闭数据库
    finally:
        db.close()
```
<hr />
###  清空文件夹

```
def delFile(path):
    paths = os.listdir(path)
    if paths != []:
        for f in paths:
            filepath = os.path.join(path, f)
            os.remove(filepath)
```
<hr />
###  获取任意周的周一和周五

```
def get_which_week_monday_and_firday_by_date(move_days):
    needTime = datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()) + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    weekStartTime = needTime - timedelta(days=needTime.weekday() + move_days, hours=needTime.hour, minutes=needTime.minute, seconds=needTime.second, microseconds=needTime.microsecond)
    weekEndTime = weekStartTime + timedelta(days=4, hours=23, minutes=59, seconds=59)
    weekStartTime = weekStartTime.strftime("%Y-%m-%d")
    weekEndTime = weekEndTime.strftime("%Y-%m-%d")
    return weekStartTime, weekEndTime
```
<hr />
###  获取工作日

```
def calculate_workdays(start_date, end_date):
    start_date = datetime.strptime(start_date,'%Y-%m-%d')
    end_date = datetime.strptime(end_date,'%Y-%m-%d')
    # 法定假期
    holi_days = [datetime.strptime(holiday,'%Y-%m-%d') for holiday in holidays]
    # 补班
    extra_days = [datetime.strptime(extraday,'%Y-%m-%d') for extraday in extradays]
    current_date = start_date
    workdays = 0
    while current_date <= end_date:
        if current_date.weekday() not in [5, 6] and current_date not in holi_days or current_date in extra_days:
            workdays += 1
        current_date += timedelta(days=1)
    return workdays
```
