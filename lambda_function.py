import json
import re
import sys
from geotext import GeoText
from city_geo import city_to_state_country
from scrap import send_request

def getWords(data):
    return re.compile(r"[\w']+").findall(data)

def lambda_handler(event, userid, context):
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
    b = potentiav.cities
    #print b
    location = city_to_state_country("\""+b[0]+"\"")
    #print location
    ############################################################################
    all_tags = []
    with open('tags.json', 'r') as f:
         data = json.load(f)

    i=0
    while i < len(data['item']):
        all_tags = all_tags + data['item'][i]['tag_query'].replace('"','').lower().split('|')
        i=i+1
    #print len(all_tags)
    ############################################################################
    search_tag = ''
    for i in c:
        if i.lower() in all_tags:
            search_tag = i
            break
    i=0
    if search_tag == '':
        while i < len(c)-1:
            d = c[i] + ' ' + c[i+1]
            if d in all_tags:
                search_tag = d
                break
            i=i+1
    #print search_tag
    ############################################################################
    if len(location) > 1:
        print "there are multiple citied with that name, please select from the following"
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

lambda_handler(sys.argv[1], sys.argv[2], 0)
