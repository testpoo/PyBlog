title:javascript代码小抄
date:2024-08-13
category: 代码小抄
tag:javascript

[TOC]

###  获取工作日

```
function getWorkdays() {
    const startDate = new Date(document.querySelector("[name='startime']").value);
    const endDate = new Date(document.querySelector("[name='endtime']").value);
    const holidays = {{ holidays|safe if holidays else [] }}; //节假日
    const extradays = {{ extradays|safe if extradays else [] }}; //补班
    let days = 0;
    let currentDate = startDate;
 
    // 确保结束日期在开始日期之后
    if (currentDate > endDate) {
        [startDate, endDate] = [endDate, startDate];
    }

    while (currentDate <= endDate) {
        const temp = currentDate.getFullYear().toString() + '-' + (currentDate.getMonth() + 1).toString() + '-' + currentDate.getDate().toString();
        if (![0, 6].includes(currentDate.getDay()) && !holidays.includes(temp) || extradays.includes(temp)) {
            days++;
        }
        currentDate.setDate(currentDate.getDate() + 1);
    }
    document.querySelector("[name='spentime']").value = days;
}
```

<hr />