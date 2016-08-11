import json
import re
import sys
import random
from geotext import GeoText
from city_geo import city_to_state_country
from scrap import send_request

def getWords(data):
    return re.compile(r"[\w']+").findall(data)

def oldner(event, userid):
    with open('data.json', 'r') as f:
         data = json.load(f)
    flag = False
    for i in data["people"]:
        if i["userid"] == userid:
            flag = True
            with open('data.json', 'w') as f:
                 json.dump(data, f)
            return i
    if flag == False:
        killbill = {
              "count": 1,
              "search_tag": "",
              "userid": userid,
              "generated": "False",
              "flag": "",
              "city": "",
              "state": "",
              "country": "",
              }
        data["people"].append(killbill)
        with open('data.json', 'w') as f:
             json.dump(data, f)
        return killbill

def updatejson(person):
    with open('data.json', 'r') as f:
         data = json.load(f)
    for i in data['people']:
        if i['userid'] == person['userid']:
            i['city'] = person['city']
            i['state'] = person['state']
            i['country'] = person['country']
            i['count'] = i['count'] + 1
            break
    with open('data.json', 'w') as f:
         json.dump(data, f)
def updatejson_search(person):
    with open('data.json', 'r') as f:
         data = json.load(f)
    for i in data['people']:
        if i['userid'] == person['userid']:
            i['search_tag'] = person['search_tag']
            i['count'] = i['count'] + 1
            break
    with open('data.json', 'w') as f:
         json.dump(data, f)

def lambda_handler(event, userid, context):
    flag_city = False
    flag_search = False
    flag_city_this = False
    flag_search_this = False
    person = oldner(event, userid)
    c = getWords(event)
    d1 = ['i', 'live', 'in', 'please', 'hi', 'give', 'find', 'who', 'what', 'my', 'hungry', 'near', 'me', 'thank', 'you', \
            'want', 'to', 'eat', 'like','liked', 'I', 'can', 'you', 'suggest', 'of', 'is', 'are', 'near', 'there', 'some', \
            'little', 'now', 'wanna', 'want', 'at', 'on', 'in', 'near', 'area', 'next', 'and', 'how', 'about', 'or', \
            'the', 'a', 'an', 'about', 'for', 'with', 'should', 'could', 'would', 'out','time','person','year','way','day',\
            'thing','man','world','life','hand','part','child','eye','woman','place','work','week', 'doing',\
            'case','point','government','company','number','group','problem','fact','be','have','do','say',\
            'get','make','go','know','take','see','come','think','look','want','give','use','find','tell', 'telling',\
            'ask','work','seem','feel','try','leave','call','good','new','first','last','long','great','little','own','other',\
            'old','right','big','high','different','small','large','next','early','young','important','few',\
            'public','bad','same','able','to','of','in','for','on','with','at','by','from','up','about','into',\
            'over','after','beneath','under','above','the','and','a','that','I','it','not','he','as','you', \
            'this','but','his','they','her','she','or','an','will','my','one','all','would','there','their', 'talk', \
            'talking', 'love', 'loved', 'hello', 'help', 'helping', 'helped', 'pleasure', 'bye', 'goodbye', 'care', 'later', \
            'no','nothing', 'thanks', 'welcome', 'something', 'hey', 'best']
    a = ''
    for c_cmall in c:
        if c_cmall not in d1:
            a = a + c_cmall.title() + ' '
        else:
            a = a + c_cmall + ' '
    #print a
    potentiav = GeoText(a)
    b= []
    b = potentiav.cities
    #print b
    if b == [] and person["city"] == "":
        #print 'jankiap50^Sorry, please enter a valid city. ^ ^ ^ ^'
        #return
        flag_city = False
    else:
        flag = False
        if b == []:
            b.append('')
            b[0] = person['city']
            location = [[person['city'], person['state'], person['country']]]
        else:
            location = city_to_state_country("\""+b[0]+"\"")
            person['city'] = location[0][0]
            person['state'] = location[0][1]
            person['country'] = location[0][2]
            updatejson(person)
            flag_city_this = True
        flag_city = True
    #print locatio
    ############################################################################
    all_tags = []
    with open('tags.json', 'r') as f:
         data = json.load(f)

    i=0
    while i < len(data['item']):
        all_tags = all_tags + data['item'][i]['tag_query'].replace('"','').lower().split('|')
        all_tags = all_tags + data['item'][i]['tag_text'].replace('"','').lower().split('|')
        i=i+1
        #print i
    #print len(all_tags)
    ############################################################################
    search_tag = ''
    for i in c:
        if i.lower() in all_tags:
            search_tag = i
            person['search_tag'] = search_tag
            updatejson_search(person)
            flag_search = True
            flag_search_this = True
            break
    i=0
    if search_tag == '':
        while i < len(c)-1:
            d = c[i] + ' ' + c[i+1]
            if d in all_tags:
                search_tag = d
                person['search_tag'] = search_tag
                updatejson_search(person)
                flag_search = True
                flag_search_this = True
                break
            i=i+1
    #print "ST   ",search_tag, flag_search
    if search_tag == '' and person['search_tag'] != '':
        search_tag = person['search_tag']
        flag_search = True

    ############################################################################
    foo = ["Okay", 'cool', 'sure', 'indeed', 'idk', 'hmmmmm', 'thats kinda cool?', 'maybe', 'iDontKnow', 'aha!']
    if flag_search_this == False and flag_city_this == False:
        print "jankiap50^ " + random.choice(foo) + "! ^ ^ ^ ^ "
        return
    elif flag_search == True and flag_city == False:
        print "jankiap50^ Hmmm... okay. I think you are looking for " + str(search_tag) + ", please enter a valif city."
        return
    elif len(location) > 1:
        print "jankiap50^there are multiple cities with that name, please select from the following ^ ^ ^ ^ "
        return
    elif flag_search == False and flag_city == True:
        print "jankiap50^ Hmmm.... I have your location," + str(location[0][0]) + " please enter a valid search tag."
        return
    else:
        search_location = location[0]
        incoming={
            "category": search_tag,
            "city": search_location[0],
            "state": search_location[1],
            "country": search_location[2],
        }
        result = send_request(incoming)
    ############################################################################
    #print "searching for " + search_tag + " at ", search_location
    print result
    return

lambda_handler(str(sys.argv[1]), sys.argv[2], 0)
