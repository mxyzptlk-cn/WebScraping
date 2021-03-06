#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018/8/15

from bs4 import BeautifulSoup

html = '''

<!DOCTYPE html>
<html lang="zh-CN" >
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
    <meta name="baidu-site-verification" content="f2dwZkRE36" />
    <meta name="description" content="该博客用于记录网易云课堂中相关课程讲述的思路和一些扩展." />
    <meta name="keywords" content="blog, 博客, 黑板客, 爬虫闯关, 机器学习, django后端开发, 用python做些事." />
    <meta name="author" content="heibanke" />
    <head>
        <title>爬虫闯关——2</title>

        <link rel="stylesheet" href="/static/libs/bootstrap/css/bootstrap.min.css">
        <link href="/static/libs/jquery-ui-1.11.2/jquery-ui.min.css" rel="stylesheet" type="text/css"/>
 
        <!--[if lt IE 9]><script src="/static/libs/js/ie8-responsive-file-warning.js"></script><![endif]-->


        <!--[if lt IE 9]>
          <script src="/static/libs/js/html5shiv.js"></script>
          <script src="/static/libs/js/respond.min.js"></script>
        <![endif]-->
        <script src="/static/libs/jquery-ui-1.11.2/external/jquery/jquery.js"></script>
        <script src="/static/libs/bootstrap/js/bootstrap.min.js"></script>
        <script src="/static/libs/js/d3.min.js"></script>
        <script src="/static/libs/jquery-ui-1.11.2/jquery-ui.min.js"></script>
        
        <script>
            var _hmt = _hmt || [];
            (function() {
              var hm = document.createElement("script");
              hm.src = "//hm.baidu.com/hm.js?74e694103cf02b31b28db0a346da0b6b";
              var s = document.getElementsByTagName("script")[0]; 
              s.parentNode.insertBefore(hm, s);
            })();
        </script>
    
         
    </head>
    <body>
        <div class="container-fluid">
         
        <div class="row">
            <div class="col-sm-1 col-md-2 col-lg-3"></div>
            <div class="col-xs-12 col-sm-10 col-md-8 col-lg-6">
                
<h1>这里是黑板客爬虫闯关的第二关</h1>
<h3></h3>

<form method="post" action="">
    <input type='hidden' name='csrfmiddlewaretoken' value='CGFW8hpcvHqzmlAZMk6BrowttJH0Fx3e' />
    <div class="form-group">
        <label>昵称:(随便输入字符)</label>
        <input class="form-control" type="text" name="username"/>
    </div>
    <div class="form-group">
        <label>密码:(30以内的数字,猜对它就能过关)</label>
        <input class="form-control" id="id_password" name="password" type="password" />
    </div>
    <div class="form-group">
        <input class="btn btn-primary" id="id_submit" type="submit" value="提交">
    </div>
</form>




                <div class="text-center">
<table class="table">
<thead>
<tr>
<td><a href="http://www.miitbeian.gov.cn" target="_blank" ><small>京ICP备14042321号</small></a></td>
<td><a href="http://www.heibanke.com/jizhang" target="_blank" ><small>云记账demo</small></a></td>
<td><a href="http://www.heibanke.com" target="_blank" ><small>黑板客blog</small></a></td>
<td><a href="http://study.163.com/course/courseMain.htm?courseId=1000035" target="_blank" ><small>用Python做些事</small></a></td>

</tr>
</thead>
</table>
</div>    
            </div>
            <div class="col-sm-1 col-md-2 col-lg-3"></div>
        </div>  
        </div>
    <ol>
        <li class="special">this list item is special</li>
        <li class="special">this list item is also special</li>
        <li>this list item is not special</li>
    <ol>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
d = soup.find_all('div')
# print(d)

d = soup.find_all(class_="form-group")
# print(d)

# id: # foo
# class:  .foo
# children: div > foo
# descendents: div p

d = soup.select('#id_submit')  # id="id_submit"
# print(d)

d = soup.select(".form-group")  # class_ = "form-group"
# print(d)

d = soup.select("[data-vcomp]")  # attrs = {"data-vcomp": True}
# print(d)

d = soup.select('.special')
# for i in d:
#     print(i.get_text())
#     print(i.name)
#     print(i.attrs)

# print(soup.body.contents)

