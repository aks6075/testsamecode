import json
import os
import pymysql
import logging
import sys
from datetime import datetime
import boto3


def lambda_handler(event, context):
    data = open('safe.txt', 'r').readlines()
    print(data)
    
    print("Hi!!2")