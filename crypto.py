#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-


##########################################
# Auth: Garzaro Paul-Michel              #
# Script IOT:crypto                      #
##########################################

import requests
import json
import sys

try:
    response=requests.get("https://www.cryptocompare.com/api/data/coinlist/")
    json=response.json()
    list=json["Data"].keys()

    def ask():
        user_input = input("""\n############################################################
##    Qu\'elle crypto monnaie souhaitez vous ?             ##
##   (list pour afficher la liste, ctrl+c pour quitter)   ##
############################################################\n\n""")
        if user_input == "list":
            print(list)
            ask()
        else:
            print(requests.get("https://min-api.cryptocompare.com/data/price?fsym="+user_input+"&tsyms=EUR").json())
            print()
    ask()
except KeyboardInterrupt:
    print("\n Aurevoir et a bientôt !")
    sys.exit(0)
