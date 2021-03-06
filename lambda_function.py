import json
import re
import sys
import random, time, csv
sys.path.insert(0, './head')
from geotext import GeoText
from city_geo import city_to_state_country
from scrap import send_request
from scrap import send_request_coord
from crf_location import crf_exec
from google_geocord import get_coord
from nle import local_tagger
from nlg import sorting

def getWords(data):
    return re.compile(r"[\w']+").findall(data)
def getWords_special_location(data):
    return re.compile(r"[\w'/.,-@]+").findall(data)
def get_random_event_list(all_tags):
    blob = ''
    i = 0
    while i < 10:
        ev = random.choice(all_tags)
        if blob.find(ev) == -1:
            blob = blob + ev + ' \n '
            i = i + 1
        else:
            i = i
    return blob[:-1]
def oldner(userid):
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
              "latitude": -1,
              "longitude": -1,
              "timestamp": int(round(time.time() * 1000))
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
            i['latitude'] = person['latitude']
            i['longitude'] = person['longitude']
            i['count'] = i['count'] + 1
            i['timestamp'] = int(round(time.time() * 1000))
            break
    with open('data.json', 'w') as f:
         json.dump(data, f)

def clearjson(person):
    with open('data.json', 'r') as f:
         data = json.load(f)
    for i in data['people']:
        if i['userid'] == person['userid']:
            i['city'] = ''
            i['state'] = ''
            i['country'] = ''
            i['latitude'] = -1
            i['longitude'] = -1
            i['count'] = i['count']
            i['search_tag'] = ''
            i['timestamp'] = int(round(time.time() * 1000))
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
            i['timestamp'] = int(round(time.time() * 1000))
            break
    with open('data.json', 'w') as f:
         json.dump(data, f)

def agefy(person):
    userid = person['userid']
    current_time = int(round(time.time() * 1000))
    if current_time - person['timestamp'] > 36000000:
        clearjson(person)
    return oldner(userid)

def push_in_csv(event, userid):
    timestamp = int(round(time.time() * 1000))
    date = time.strftime("%m/%d/%Y")
    with open('allevents_user_data.csv', 'a') as csvfile:
        fieldnames = ['userid', 'event', 'timestamp', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'userid': userid, 'event': event, 'timestamp': timestamp, 'date': date})

def push_out_csv(event, userid):
    timestamp = int(round(time.time() * 1000))
    date = time.strftime("%m/%d/%Y")
    with open('allevents_user_data_response.csv', 'a') as csvfile:
        fieldnames = ['userid', 'event', 'timestamp', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'userid': userid, 'event': event, 'timestamp': timestamp, 'date': date})

def lambda_handler(event, userid, context):

    push_in_csv(event, userid)

    if event.lower() == 'wash_element':
        person = oldner(userid)
        clearjson(person)
        blowed = "jankiap50^ We cleared your element. Forgot you state and history. "
        push_out_csv(blowed, userid)
        print blowed
        return
    if event.lower() == 'display_element':
        person = oldner(userid)
        blowed = "jankiap50^ Here is your element: " + json.dumps(person)
        push_out_csv(blowed, userid)
        print blowed
        return

    lust = getWords_special_location(event)
    #################################################################################
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
            'no','nothing', 'thanks', 'welcome', 'something', 'hey', 'am', 'month','year','week','day','hour','minute','min','second', \
            'months','years','weeks','days','hours','minutes','mins','seconds','time', 'today', 'tomorrow', 'am', 'pm',\
            'january', 'febuary', 'marth', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december', \
            'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','km', 'kilometer', 'kilometers', 'meter', 'm',\
            'cm', 'kms', 'miles', 'yards', 'feet', 'feets','evening', 'morning', 'afternoon', 'noon', 'night',\
            'trying', 'looking']
    #d1 = []
    kiss = ''
    bang = ''
    bump_last = ['.', ',', ';', ':', '(', ')', '?', '!']
    for c_cmall in lust:
        if c_cmall[-1] not in bump_last:
            if c_cmall not in d1:
                kiss = kiss + c_cmall.title() + ' '
                bang = bang + c_cmall.title() + ' '
            else:
                kiss = kiss + c_cmall + ' '
                bang = bang + c_cmall + ' '
        else:
            if c_cmall not in d1:
                kiss = kiss + c_cmall[:-1].title() + ' '
                bang = bang + c_cmall[:-1].title() + ' ' + c_cmall[-1] + ' '
            else:
                kiss = kiss + c_cmall[:-1] + ' '
                bang = bang + c_cmall[:-1] + ' ' + c_cmall[-1] + ' '
    #################################################################################
    a = crf_exec(bang, 0)
    i=0
    data_ayrton=[]
    b=[]
    drop_char = ['.', ',', ';']
    for i in a:
        if i[0][-1] in drop_char:
            j = i[0][:-1]
        else:
            j = i[0]
        data_ayrton.append([str(j), str(i[1]), str(i[2]), str(i[3])])
        b.append([str(j), str(i[3])])
    c = data_ayrton
    data_ayrton=[]
    i=0
    p_loc = ''
    p_loc_ref = []
    for atom in c:
        if atom[2][-3:] == 'LOC' and atom[0] not in p_loc_ref:
            p_loc = p_loc + atom[0] + ' '
            p_loc_ref.append(atom[0])
            data_ayrton.append(p_loc)
            p_loc = ''
        i = i + 1
    #############################################################################
    # getting the coordinates of the city. We already have potential cities in
    # data_ayrton from NER, or b[] from UN CSV, or person[city]
    #############################################################################
    flag_city = False
    flag_search = False
    flag_city_this = False
    flag_search_this = False
    person = oldner(userid)
    person = agefy(person)
    c = getWords(event)
    potentiav = GeoText(kiss)
    b= []
    b = potentiav.cities
    b = b
    #print b
    #print data_ayrton
    #print person
    if b == [] and person["latitude"] == -1 and data_ayrton == []:
        #print 'jankiap50^Sorry, please enter a valid city. ^ ^ ^ ^'
        #return
        flag_city = False
    elif b != []:
        flag = False
        if b == []:
            b.append('')
            b[0] = person['city']
            coord = [person['latitude'], person['longitude']]
        else:
            location = city_to_state_country("\""+b[0]+"\"")
            if location != []:
                person['city'] = location[0][0]
                person['state'] = location[0][1]
                person['country'] = location[0][2]
                coord = get_coord(person['city'] + ',' + person['state'] + ',' + person['country'])
            else:
                person['city'] = b[0]
                coord = get_coord(b[0])
            person['latitude'] = coord[0]
            person['longitude'] = coord[1]
            updatejson(person)
            flag_city_this = True
        flag_city = True
    elif data_ayrton != []:
        coord = get_coord(data_ayrton[0])
        person['city'] = data_ayrton[0]
        person['latitude'] = coord[0]
        person['longitude'] = coord[1]
        updatejson(person)
        flag_city = True
        flag_city_this = True
    else:
        b.append('')
        b[0] = person['city']
        coord = [person['latitude'], person['longitude']]
        flag_city = True
    #print coord
    #############################################################################
    # All the tags from allevents.in that must be matched are here.
    #############################################################################
    all_tags = []
    with open('tags.json', 'r') as f:
         data = json.load(f)

    i=0
    while i < len(data['item']):
        all_tags = all_tags + data['item'][i]['tag_text'].replace('"','').lower().split('|')
        all_tags = all_tags + data['item'][i]['tag_query'].replace('"','').lower().split('|')
        i=i+1
    ############################################################################
    i=0
    while i < len(all_tags):
        if all_tags[i][0] == ' ':
            all_tags[i] = all_tags[i][1:]
            i=i-1
        i=i+1
    #print all_tags
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
    if search_tag == '':
        from w2v import matcher
        latent_match = matcher(c,0)
        if latent_match != 'jankiap50':
            search_tag = latent_match
            person['search_tag'] = search_tag
            updatejson_search(person)
            flag_search = True
            flag_search_this = True
    #print "ST   ",search_tag, flag_search
    if search_tag == '' and person['search_tag'] != '':
        search_tag = person['search_tag']
        flag_search = True
    ############################################################################
    #print 'a', a
    res_nle = local_tagger.ner(event, a)
    ############################################################################
    foo = ["Okay", 'cool', 'sure', 'indeed', 'idk', 'hmmmmm', 'thats kinda cool?', 'maybe', 'iDontKnow', 'aha!']
    query_event = ['event', 'events', 'show', 'shows', 'what', 'type']
    if flag_search_this == False and flag_city_this == False:
        blowed = "jankiap50^ " + random.choice(foo) + "! ^ ^ ^ ^ "
        for each in query_event:
            if each in c:
                blowed = "jankiap50^ " + get_random_event_list(all_tags)
        push_out_csv(blowed, userid)
        print blowed
        return
    elif flag_search == True and flag_city == False:
        blowed = "jankiap50^ Hmmm... okay. I think you are looking for " + str(search_tag) + ", please enter a valid city."
        push_out_csv(blowed, userid)
        print blowed
        return
    #elif len(location) > 1:
    #    print "jankiap50^there are multiple cities with that name, please select from the following ^ ^ ^ ^ "
    #    return
    elif flag_search == False and flag_city == True:
        blowed = "jankiap50^ Hmmm.... I have your location, " + str(person['city']) + ", please enter an event type like... \n " + get_random_event_list(all_tags)
        push_out_csv(blowed, userid)
        print blowed
        return
    #print search_tag, location
    '''incoming={
        "category": str(search_tag),
        "city": "Ahmedabad",
        "state": "GJ",
        "country": "IN"
    }
    result = send_request(incoming)
    print result'''
    coord[0] = round(coord[0], 7)
    coord[1] = round(coord[1], 7)
    #print coord
    incoming={
        "category": str(search_tag),
        "latitude": coord[0],
        "longitude": coord[1],
        "radius": 10
    }
    result = send_request_coord(incoming)
    ############################################################################
    #print "searching for " + search_tag + " at ", search_location
    result=result.encode('ascii', 'ignore')
    result = sorting.sort_generation(result, res_nle)
    result=result.encode('ascii', 'ignore')
    #print type(result)
    push_out_csv(str(result), userid)
    print str(result)
    return

lambda_handler(str(sys.argv[1]), sys.argv[2], 0)
