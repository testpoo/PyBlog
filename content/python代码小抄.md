title:python代码小抄
date:2024-08-13
category: 代码小抄
tag:python

[TOC]

> ### 清空文件夹

```
def delFile(path):
    paths = os.listdir(path)
    if paths != []:
        for f in paths:
            filepath = os.path.join(path, f)
            os.remove(filepath)
```
<hr />
> ### 获取任意周的周一和周五

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
> ### 获取工作日

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