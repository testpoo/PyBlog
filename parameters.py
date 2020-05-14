#coding=utf-8

#站名标题信息
words = {
    #"sitename":"https://testpoo.github.io",
    "sitename":"http://127.0.0.1:8000",
    "title":"地空神一",
    "keywords":"Poo's Notes",
    "description":"Poo's Notes - 一个测试人的自虐。",
	"author":"TestPoo",
	"github":"https://github.com/testpoo",
	"mail":"pu_yawei@qq.com",
    "wechat":"puyaweis"
}

pushdir="output"  # 输出文件夹
pulldir="content" # 输入文件夹

# 学习网站
links = (('Requests', 'http://www.python-requests.org/'),
         ('Linux命令行', 'http://billie66.github.io/TLCL/book/'),
         ('Flask文档中文版', 'http://docs.jinkan.org/docs/flask/'),
         ('Jinja2文档中文版', 'http://docs.jinkan.org/docs/jinja2/'),
		 ('Git文档中文版','https://git-scm.com/book/zh/v2'))

#静态路径
src=r"themes/static"
dst=r"output/themes"
static=r"static"
output=r"output"

#分页数
count = 10
range_num = 2