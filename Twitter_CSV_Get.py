#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv
import tweepy

CONSUMER_KEY    = 'AcNwWTbXxHWhIoAJBuHLIbns2'
CONSUMER_SECRET = 'KCxAYCK8737Z56ctLamXlPXjAnawIt5nHFNJG6SXjt6wZ5BBgw'
ACCESSS_TOKEN   = '915051361112174592-9jntPFhTtO5VwoKtdRPs43UFvzyNfF0'
ACCESS_SECRET   = 'WmUrQM1JiH2sUTdVbFnVCQW80fNDifIdS1VeYfmopeuvw'

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESSS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    num = 1
    data = []
    with open("nakamurahiro3.csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f, lineterminator='\n')

        for status in api.user_timeline(screen_name="nakamurahiro3",count=200):
            writer.writerow([status.text])
            data.append(num)
            num += 1
