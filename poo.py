#coding=utf-8

import os
import jinja2
import shutil
import math
import markdown
import html
import re
import copy
import datetime
import base64

from parameters import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'themes/templates')))

#def b64encode(base64temp):
#    b64str=str(base64.b64encode(bytes(base64temp,encoding='utf8')),encoding = "utf8")
#    return b64str

#jinja_environment.filters['b64encode'] = b64encode

# 常量
lastBuildDate = datetime.datetime.now()
year = lastBuildDate.year

# 删除output中文件
def delfile():
    filelist=[]
    #rootdir="output"
    filelist=os.listdir(pushdir)
    for f in filelist:
        filepath = os.path.join( pushdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)

# 获取内容
def file_name(file_dir):
    #for root, dirs, files in os.walk(file_dir):  
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        #print(files) #当前路径下所有非目录子文件
    for files in os.walk(file_dir): 
        files = files[2]
        #files.reverse(key=file)
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

# 类别/标签
def params(articles,param):

    params = []
    count = {}
    for i in range(len(articles)):
        if param in articles[i] and articles[i][param]!='':
            params += articles[i].copy()[param]
    for par in params:
        count[par] = params.count(par)
    return count

#生成文章列表
def home(articles,path,categroies):

    cate = list(params(articles,'category').keys())
    if len(cate) < 2:
        cate = cate[0]
    
    files = file_name(pulldir)

    total_record = len(articles)
    
    page_total = int(math.ceil(total_record / count))

    template = jinja_environment.get_template('index.html')
    if not os.path.exists(pushdir+"/"):
        os.makedirs(pushdir+"/")
    for current_page in range(1, 1 + page_total):
        start = (current_page - 1) * count
        end = start + count
        paginator = {'count':count,'current_page':current_page,'total_record':total_record,'page_total':page_total,'start':start,'end':end,'range_num':range_num}
        f = open(pushdir+"/"+path+str(current_page if current_page > 1 else '')+".html", "w",encoding="utf-8")   
        f.write(template.render(articles=articles[start:end],pag=paginator,words=words,year=year,current='index.html',categroies=categroies,cate=cate))
        f.close()

# 生成类别列表
def categories_home(articles):

    cas = params(articles,'category')

    template = jinja_environment.get_template('categories.html')
    if not os.path.exists(pushdir+"/"):
        os.makedirs(pushdir+"/")
    f = open(pushdir+"/categories.html", "w",encoding="utf-8")
    f.write(template.render(cas=cas,words=words,year=year))
    f.close()

# 生成类别文章
def category(articles,categroies):
    
    temp = []

    if not os.path.exists(pushdir+'/categories'):
        os.makedirs(pushdir+'/categories')

    cates = list(params(articles,'category').keys())
    for i in range(len(cates)):
        for j in range(len(articles)):
            if 'category' in articles[j] and cates[i] in articles[j]['category']:
                temp.append(articles[j])
        home(temp,'categories/'+cates[i].lower(),categroies)
        temp.clear()

# 生成文章
def posts(articles):

    template = jinja_environment.get_template('article.html')
    counts = len(articles)
    for i in range(counts):
        if not os.path.exists(pushdir+'/post'):
            os.makedirs(pushdir+'/post')
        if i == 0:
            previous = ''
        else:
            previous = articles[i-1]
        if i == counts-1:
            next = ''
        else:
            next = articles[i+1]
        #f = open(pushdir+"/post/"+str(base64.b64encode(bytes(articles[i]['title'],encoding='utf8')),encoding = "utf8")+".html", "w", encoding="utf-8")
        f = open(pushdir+"/post/"+articles[i]['title']+".html", "w", encoding="utf-8")
        f.write(template.render(article = articles[i],words=words,previous=previous,next=next,year=year))
        f.close()

# 生成RSS
def rss(articles):

    template = jinja_environment.get_template('rss.xml')
    if not os.path.exists(pushdir+"/"):
        os.makedirs(pushdir+"/")
    f = open(pushdir+"/rss.xml", "w",encoding="utf-8")   
    f.write(template.render(articles=articles,words=words,year=year))
    f.close()

#about
def about():

    # 导入markdown额外插件
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    with open('about/about.md', "r", encoding='utf-8') as file:
        ret=file.read()
    about = markdown.markdown(ret,extensions=exts,encoding='utf-8')
    template = jinja_environment.get_template('about.html')
    f = open(pushdir+"/about.html", "w", encoding="utf-8")
    f.write(template.render(about=about,words=words,year=year))
    f.close()

def nonexistent():
    with open('about/about.md', "r", encoding='utf-8') as file:
        nonexistent=file.read()
    template = jinja_environment.get_template('404.html')
    f = open(pushdir+"/404.html", "w", encoding="utf-8")
    f.write(template.render(nonexistent=nonexistent,words=words,year=year))
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

#函数调用
def makehtml():

    articles = md(file_name(pulldir))
    categroies = params(articles,'category')
    delfile()
    home(articles,'index',categroies)
    category(articles,categroies)
    posts(articles)
    about()
    nonexistent()
    rss(articles)
    copyFiles(src, dst)
    copyFiles(static, output)

if __name__ == '__main__':
    makehtml()