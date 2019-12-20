#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
# 如果以前存储了用户名，就加载它

# 否则，就提示用户名输入并储存它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
