#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def print_models(unprint_designs,completed_models):
    while unprint_designs:
        current_design = unprint_designs.pop()
        print("Printing model:"+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
