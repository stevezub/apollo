from __future__ import print_function

import json
import urllib2

print('Loading function')

#response = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json?api_key=9P958dHQayN8QP-pQVJs')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    response = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/TROW.json?api_key=9P958dHQayN8QP-pQVJs',timeout = 10)
    resobjects = json.loads(response.read())
    return "$"+str(resobjects['dataset']['data'][1][4])
    #data = resobjects['data']
    #return data[5]
    #return html  # Echo back the first key value
    #raise Exception('Something went wrong')
