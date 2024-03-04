#coding=utf-8

import os
import jinja2
import markdown
import copy
import datetime
import base64
import shutil
import time

###############################
#           配置参数
###############################
#站名标题信息
words = {
    "siteurl":"https://testpoo.github.io",
    #"siteurl":"http://127.0.0.1:8000",
    "sitename":"测试铺",
    "keywords":"Poo's Notes",
    "description":"一个80后老人，专注测试领域",
    "author":"TestPoo",
    "github":"https://github.com/testpoo",
    "mail":"pu_yawei@qq.com",
    "wechat":"puyaweis",
    "jump":"关于我"
}

#静态路径
pushdir="output"  # 输出文件夹
pulldir="content" # 输入文件夹
src=r"static"
dst=r"output/themes"
static=r"static"
output=r"output"

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

# 常量
lastBuildDate = datetime.datetime.now()
year = lastBuildDate.year
lastBuildDate = str(lastBuildDate)[0:19]

# 删除output中文件
def delfile():
    filelist=[]
    filelist=os.listdir(pushdir)
    for f in filelist:
        filepath = os.path.join( pushdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)

# 获取内容
def file_name(file_dir):
    for files in os.walk(file_dir): 
        files = files[2]
        return files

# 生成markdown
def md(filename):
    # 导入markdown额外插件
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    articles = []
    article = {}
    for i in range(len(filename)):
        with open(pulldir+'/'+filename[i], "r", encoding='utf-8') as file:
            for file_line in file:
                file_line = file_line.strip()
                if file_line.lstrip().startswith('title'):
                    article['title']=file_line.replace('title:','').replace(' ','')
                elif file_line.lstrip().startswith('date'):
                    article['date']=file_line.replace('date:','').strip()
                elif file_line.lstrip().startswith('category'):
                    article['category']=file_line.lower().replace('category:','').replace(' ','').split(',')
                elif file_line.lstrip().startswith('tag'):
                    article['tag']=file_line.lower().replace('tag:','').replace(' ','').split(',')
                else:
                    ret=file.read()
                    article['content'] = markdown.markdown(ret,extensions=exts,encoding='utf-8')
                    articles.append(article.copy())
                    article.clear()
    articles =  sorted(articles,key=lambda d:d['date'],reverse=True)
    return articles

# 生成文章
def posts(articles):
    posts = []
    for article in articles:
        posts.append(article['title'])

    categories = {}
    for category in articles:
        if category['category'][0] not in categories.keys():
            categories[category['category'][0]] = category['title']

    template = jinja_environment.get_template('article.html')
    counts = len(articles)
    for i in range(counts):
        if not os.path.exists(pushdir):
            os.makedirs(pushdir)
        category = articles[i]['category']
        cate_posts = []
        for article in articles:
            if article['category'] == category:
                cate_posts.append([article['title'],article['date'],article['content']])
        f = open(pushdir+"/"+articles[i]['title']+".html", "w", encoding="utf-8")
        f.write(template.render(article = articles[i],words=words,categories=categories,cate_posts=cate_posts,posts=posts,lastBuildDate=lastBuildDate))
        f.close()

# 生成RSS
def rss(articles):
    template = jinja_environment.get_template('rss.xml')
    if not os.path.exists(pushdir+"/"):
        os.makedirs(pushdir+"/")
    f = open(pushdir+"/rss.xml", "w",encoding="utf-8")   
    f.write(template.render(articles=articles,words=words,lastBuildDate=lastBuildDate))
    f.close()

# 生成首页
def home():
    template = jinja_environment.get_template('index.html')
    if not os.path.exists(pushdir+"/"):
        os.makedirs(pushdir+"/")
    f = open(pushdir+"/index.html", "w",encoding="utf-8")   
    f.write(template.render(words=words,lastBuildDate=lastBuildDate))
    f.close()

#拷贝静态文件
def copyFiles(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    srcFiles = os.listdir(src)
    #dstFiles = dict(map(lambda x:[x, ''], os.listdir(dst)))
    filesCopiedNum = 0

    # 对源文件夹中的每个文件若不存在于目的文件夹则复制
    for file in srcFiles:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        # 若源路径为文件夹，若存在于目标文件夹，则递归调用本函数；否则先创建再递归。
        if os.path.isdir(src_path):
            if not os.path.isdir(dst_path):
                os.makedirs(dst_path)  
            filesCopiedNum += copyFiles(src_path, dst_path)
        # 若源路径为文件，不重复则复制，否则无操作。
        elif os.path.isfile(src_path):                
            #if file not in dstFiles:
            shutil.copyfile(src_path, dst_path)
            filesCopiedNum += 1

    return filesCopiedNum

if __name__ == '__main__':
    delfile()
    articles = md(file_name(pulldir))
    posts(articles)
    rss(articles)
    home()
    copyFiles(src, dst)