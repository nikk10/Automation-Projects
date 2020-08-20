#!/usr/bin/env python3

import os
import requests

file_location = "/home/student-04-59f5f9ee2d97/data/feedback"
url = "http://34.66.248.253/feedback/"
feedback = {}


for file in os.listdir(file_location):
    #print file location to show correct file location
    print(str(os.path.join(file_location,file)))
    with open(os.path.join(file_location,file)) as f:
        feedback["Title"] = f.readline().strip()
        feedback["Name"] = f.readline().strip()
        feedback["Date"] = f.readline().strip()
        #comments are read into a list to teh end of teh file,
        #then combined into one string and s/n is replaced with empty text
        feedback["Comments"] = " ".join(f.readlines()).replace("\n", "")

    #print feedback to test that dictionaries are being created
    print(feedback)
    print()
    post = requests.post(url, data=feedback)
    #print response code to verify posting
    print(post.status_code)
    #if the feedback has sucessfully posted (status 201), alert user
    if post.status_code == 201:
        post.raise_for_status()
