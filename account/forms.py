from django import forms
import random
def randstr(length):
        rstr = "0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
        rstr_len = len(rstr) - 1
        result = ""
        for i in range(length):
            result += rstr[random.randint(0, rstr_len)]
        return result