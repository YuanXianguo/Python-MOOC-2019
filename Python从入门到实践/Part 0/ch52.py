#!/usr/bin/env python 
# -*- coding:utf-8 -*-
users = {
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
    },
}
for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name = user_info['first']+" "+user_info['last']
    print("\tFull name:" + full_name.title())
