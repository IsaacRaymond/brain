import json

data = {}

data["convotype"] = 0
data["inConvo"] = False
data["answerToLove"] = ""
data["answerToLeader"] = ""

with open('data.txt','w') as outfile:
    json.dump(data, outfile)