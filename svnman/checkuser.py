# -*- coding: utf-8 -*-

import ConfigParser

cfg = ConfigParser.ConfigParser()

cfg.read('D:\\sandbox\\django\\cpsjb\\svnman\\authz')

allurl = []
groups = {}

class myurl:
    def __init__(self, key, users):
        self.key = key
        self.name = key.split(':')[0]+key.split(':')[1]
        self.users = users

    def checkuser(self, username):
        if (self.users.has_key(username)):
            return self.users[username]
        return False


for grp in cfg.items('groups'):
    groups[grp[0]] = grp[1]


for url in cfg._sections.keys():
    if (url != 'groups'):
        users = {}
        for item in cfg.items(url):
            if (item[0][0] == '@'):
                for user in groups[item[0][1:]].split(','):
                    users[user]=item[1]
            else:
                users[item[0]] = item[1]
        allurl.append(myurl(url, users))


def get_url_list(username):
    urllist = []
    for url in allurl:
        r = url.checkuser(username)
        if (r):
            urllist.append((r, url.name))
    return urllist

