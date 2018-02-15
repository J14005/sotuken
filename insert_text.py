#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import csv
if __name__ == '__main__':
    #データベース接続
    connect = MySQLdb.connect(host='127.0.0.1', db='sotuken', user='root', passwd='teikyo', charset='utf8')
    #ハンドル
    cursor = connect.cursor()
    f = open("AbeShinzo.csv","r",encoding='utf-8')#shimamuradai  AbeShinzo  watanabe_miki
    reader = csv.reader(f)

    i = 0
    temp = []
    for line in reader:
        temp.append(line)
        i += 1

    #インサート
    j = 1
    for rage in range(0,200):#正規表現を仕様　区切り文字で区切ってSQLに入れるようにプログラムする
        sql = 'insert into jiminto3 (bango,name,text) values (%s,%s,%s)'
        cursor.execute(sql,(j,"AbeShinzo",temp[j]))
        connect.commit()
        j += 1

    f.close()
    # データベースから切断
    cursor.close()
    connect.close()
