import json

data = {}

data["convotype"] = 0
data["inConvo"] = False
data["answerToLove"] = ""
data["answerToLeader"] = ""
data["peopleInHouse"] = ["Forrest", "Miles", "Jaycee", "Isaac", "Hobbes"]
data["who_is_talking"] = ""

with open('data.txt','w') as outfile:
    json.dump(data, outfile)
