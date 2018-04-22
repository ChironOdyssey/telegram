# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:50:54 2018

@author: resha
"""

import pandas as pd


# CREATE MOCK DATA
imagelist = [
'https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
'http://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg',
'https://www.cesarsway.com/sites/newcesarsway/files/styles/large_article_preview/public/Natural-Dog-Law-2-To-dogs%2C-energy-is-everything.jpg?itok=Z-ujUOUr',
'https://news.nationalgeographic.com/content/dam/news/2017/06/23/domestic-dogs-gallery/01-domestic-dog-gallery.ngsversion.1520573409565.adapt.1900.1.jpg'
]
df =  pd.DataFrame({'image_id':[1,2,3,4,5],'image_url':imagelist})
df['dataset_id'] = '1A'
df['labels'] =  'dog,cat'


# SAVE TO TELEGRAM FEED
df.to_json('../mvp_telegram/input_images.json')

print(df)