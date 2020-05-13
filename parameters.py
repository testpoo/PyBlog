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
	"mail":"pu_yawei@qq.com"
}

pushdir="output"  # 输出文件夹
pulldir="content" # 输入文件夹
#about = 'about'

# nav
# navs = (['分类','categories.html'],['标签','tags.html'],['归档','archives.html'],['导航','links.html'],['关于','about.html'])
#navs = (['首页',''],['搜索','search.html'],['关于','about.html'])

# about
introduction = '一个80后老人，专注测试领域。'
infos = {'email':'pu_yawei@qq.com','wechat':'puyaweis','staticblog':'https://github.com/testpoo/PyBlog','github':'https://github.com/testpoo'}

works = [
    {'worktime':'2018-','company':'北京银杉金服西安分公司','url':'http://aghoo.com/','position':'高级工程师','jobdescription':'互联网金融','adress':'西安'},
    {'worktime':'2015-2018','company':'北京慧眼智行科技有限公司','url':'http://www.bocode.cn/','position':'测试经理','jobdescription':'食品药品安全','adress':'北京'},
    {'worktime':'2014-2015','company':'方正国际软件（北京）有限公司','url':'http://www.founderinternational.com/','position':'测试总监','jobdescription':'银行核心系统建设','adress':'北京|绍兴'},
    {'worktime':'2010-2014','company':'北京斯顿信息技术有限公司','url':'http://www.infohold.com.cn/','position':'助理测试经理','jobdescription':'银行核心系统建设','adress':'北京|长春'},
    {'worktime':'2017-2010','company':'神州数码融信软件有限公司','url':'http://www.dcits.com/','position':'测试工程师','jobdescription':'银行核心系统建设','adress':'西安|深圳'}
]

#技术栈专栏
#categroies = ['Nginx','Redis','Jmeter','Selenium','Python','Git','Svn']

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