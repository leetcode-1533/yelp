
import json
#import util
import collections
import numpy as np
import csv


resultFile = open("businesses.csv",'w')
wr = csv.writer(resultFile, delimiter='|')


# creates biz_hash
biz_cat = {}
#categoryOptsDict = util.Counter()

x=0

#jsonIn = '../yelp_dataset/yelp_academic_dataset_business.json'
jsonIn = '/Users/mvm/Documents/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json'

dataArray = []

y = 0
with open (jsonIn) as data_file:
    for line in data_file:

        x = x+1

        if x % 10000 == 0:
            print x

        obj = json.loads(line)
        
        businessId = obj['business_id'].encode('utf-8','replace')
        name = obj['name'].encode('utf-8','replace')
        fullAddress = obj['full_address'].replace('\n', ' ')
        city = obj['city']
        state = obj['state']
        latitude = obj['latitude']
        longitude = obj['longitude']
        open1 = obj['open']
        if(state == "NV" and open1):
            wr.writerow([businessId,name,fullAddress,city,state,latitude,longitude])
       # dataArray.append([businessId,name,fullAddress,city,state,latitude,longitude])

#print dataArray[0]
#print dataArray[1]
#allData = np.asarray(dataArray)
#np.savetxt('../bizData.csv',dataArray, delimiter = ",")


