# -*- coding: utf-8 -*-
import feedparser
print("RSSfeedを取得したいURLを入力してください。")
url = raw_input()
fdp = feedparser.parse(url)
for  entry in fdp[ 'entries' ]:
    print "Title: ", entry[ 'title' ]
    print "URL: ", entry[ 'link' ]
    print "Description: ", entry[ 'description' ]
    print "Date: ", entry[ 'updated' ]
                
