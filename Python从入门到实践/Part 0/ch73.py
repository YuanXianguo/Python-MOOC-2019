#!/usr/bin/env python 
# -*- coding:utf-8 -*-
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain?")
    responses[name] = response
    repeat = input("anther?(yes/no)")
    if repeat == 'no':
        polling_active = False
print ("\n---Poll Results---")
for name,response in responses.items():
    print (name + " would like to climb " + response + ".")
