# -*- coding: utf-8 -*-
from django.template import loader,Context
from django.http import HttpResponse, HttpResponseRedirect
import md5crypt
import checkuser

def index(request):
    #actionlist = myaction.objects.all()[:5]
    #cailist = Cai.objects.all()
    imagelist = range(6)
    t = loader.get_template('svnman/index.html')
    c = Context({
        #'actionlist':actionlist,
        #'cailist':cailist,
        'imagelist':imagelist,
        })
    return HttpResponse(t.render(c))

def getsvninfo(request):
    str = request.GET.get('info', False)
    u = str.split(':')[0]
    p = str.split(':')[1]
    ha = getuserhash(u)
    str = '用户名或密码错误'
    if (ha):
        if (testpwd(p, ha)):
            #str = '密码正确!'
            str = checkuser.get_url_list(u)
        else:
            return HttpResponse('用户名或密码错误')
    else:
        return HttpResponse('用户名或密码错误')
        
    all = []
    for a in str:
        if (a[0] == 'r'): 
            r = '只读'
        if (a[0] == 'w'): 
            r = '只写'
        if (a[0] == 'rw'):
            r = '读写'
        all.append((r, 'https://foreversvn/svn/'+a[1]+'\n'))
    #all.sort()
    t = loader.get_template('svnman/display.html')
    c = Context({
        'tablelist':all,
        })
    return HttpResponse(t.render(c))

def testpwd(clear_password, the_hash):
    magic, salt = the_hash[1:].split('$')[:2]
    magic = '$' + magic + '$'
    if (md5crypt.md5crypt(clear_password, salt, magic) == the_hash):
        return True
    return False


def getuserhash(username):
    f = open('D:\\sandbox\\django\\cpsjb\\svnman\\htpasswd')
    all = f.readlines()
    f.close()
    for str in all:
        u,p = str.split(':')[:2]
        if (u == username):
            p = p.replace('\n','')
            return p
    return False;
