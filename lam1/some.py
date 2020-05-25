import json
import os
import pymysql
import logging
import sys
from datetime import datetime
import boto3
import requests


def lambda_handler(event, context):
    res= requests.get('https://w3schools.com')
    print(res.json)
    conn = pymysql.connect(host="rds_host",user="name",password="password,database=None")
    print("Hi!!1")