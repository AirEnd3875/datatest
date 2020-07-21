import urllib

import urllib2

__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

register_openers()

def upload(fileName):

    datagen, headers = multipart_encode({"file": open("C:\\Users\\user\\Desktop\\%s" % fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "123.67ab5f00d86977e776b1ce3701e030f4.YsIdpYDmgYiplrgSrcJhbvi3VrBsNJYKW4Njj8w.4qPSLA",
        "path": "/apps/ResourceSharing/%s"%fileName
    }
    encodeargs = urllib.urlencode(args)
    url = baseurl + encodeargs

    print(url)

    request = urllib2.Request(url, datagen, headers)
    result = urllib2.urlopen(request).read()
    print(result)

upload("tempPics.zip")