import requests
import json

def local_cmd_testing():
    example = ["I am near Bandra in Mumbai. ",\
    "I am in gandhinagar.",\
    "I am in Gandhinagar. ",\
    "I am from ahmedabad - any business events?",\
    "where is party tonight?",\
    "what's happening this weekend?",\
    "tell me about events in Udaipur this Sunday",\
    "Hey is there any event happening in next one hour in my city?",\
    "Hey where is the this eChai Demo Day happening?",\
    "Any sports events?",\
    "Calvin haris in india",\
    "What's the ticket price for Sunidhi Concert?",\
    "any workshop for this weekend in ahmedabad",\
    "Which is the most popular music event in ahmedabad",\
    "Free events this weekend",\
    "Suggest me events for singles",\
    "Are there any yoga classes ?",\
    "Sunburn early bird tickets / offers",\
    "Events for Children",\
    "Any treks to North India?/",\
    "Events for Women",\
    "Where to go this weekend/ Sunday / Monday",\
    "Marathons in ahmedabad",\
    "Send me address of Startups Saturday",\
    "Hey at what time Wow Saturday starts?",\
    "Getaways near Ahmedabad",\
    "Can you suggest me any exhibitions related to engineering?",\
    "parties tonight",\
    "weekend activity",\
    "any concerts this sunday?",\
    "Events related to Networking",\
    "free couple passes?",\
    "parties this valentine's day",\
    "Find me an event partner",\
    "you can try your luck in Networking section from the app",\
    "When is the movie Warcraft releasing?/",\
    "Fairs/Carnivals in Ahmedabad", '']
    for each_ex in example:
        print '-------------------------'
        print each_ex
        id = 104
        special_query = 0
        if special_query == 0:
            each_ex = unicode(each_ex, "utf-8")
            '''parsedEx = parser(each_ex)
            full_pos = get_postagging(parsedEx)
            full_dep = get_dependency(parsedEx)
            full_ents = get_ner(each_ex,parsedEx)'''
            r = requests.get("http://ec2-54-200-198-248.us-west-2.compute.amazonaws.com:5940/?message="+each_ex)
            #print r.status_code
            #print r.headers
            #print r.text
            parsedEx = json.loads(r.text)
            full_pos = parsedEx['full_pos']
            full_dep = parsedEx['full_dep']
            full_ents = parsedEx['full_ents']
            #full_pos = conver_pos(full_pos)
            #full_dep = conver_dep(full_dep)
            print (each_ex, full_pos, full_dep, full_ents, id)
        else:
            print special_query

'''from spacy.en import English
parser = English()'''
local_cmd_testing()
