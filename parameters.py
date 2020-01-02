#coding=utf-8

#站名标题信息
words = {
    "sitename":"https://testpoo.github.io",
    "title":"Poo's Notes",
    "keywords":"Poo's Notes",
    "description":"Poo's Notes - 一个测试人的自虐。",
	"author":"TestPoo",
	"github":"https://github.com/testpoo",
	"mail":"pu_yawei@qq.com"
}
'''
#读取模板
template_file = [
    ['about.html','output/about/']
]
'''
pushdir="output"  # 输出文件夹
pulldir="content" # 输入文件夹
about = 'about'

# nav
navs = (['分类','categories.html'],['标签','tags.html'],['归档','archives.html'],['导航','links.html'],['关于','about.html'])

#技术栈专栏
knowledge = ['Nginx','Redis','Jmeter','Selenium','Python','Git','Svn']

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