import re
def getWords(data):
    return re.compile(r"[\w']+").findall(data)
def getWords_special_location(data):
    return re.compile(r"[\w'/.,-@]+").findall(data)
def list_cities(text):
    d1 = ['i', 'live', 'in', 'please', 'hi', 'give', 'find', 'who', 'what', 'my', 'hungry', 'near', 'me', 'thank', 'you', \
            'want', 'to', 'eat', 'like','liked', 'I', 'can', 'you', 'suggest', 'of', 'is', 'are', 'near', 'there', 'some', \
            'little', 'now', 'wanna', 'want', 'at', 'on', 'in', 'near', 'area', 'next', 'and', 'how', 'about', 'or', \
            'the', 'a', 'an', 'about', 'for', 'with', 'should', 'could', 'would', 'out','time','person','year','way','day',\
            'thing','man','world','life','hand','part','child','eye','woman','place','work','week', 'doing',\
            'case','point','government','company','number','group','problem','fact','be','have','do','say',\
            'get','make','go','know','take','see','come','think','look','want','give','use','find','tell', 'telling',\
            'ask','work','seem','feel','try','leave','call','good','first','last','long','great','little','own','other',\
            'old','right','big','high','different','small','large','next','early','young','important','few',\
            'public','bad','same','able','to','of','in','for','on','with','at','by','from','up','about','into',\
            'over','after','beneath','under','above','the','and','a','that','I','it','not','he','as','you', \
            'this','but','his','they','her','she','or','an','will','my','one','all','would','there','their', 'talk', \
            'talking', 'love', 'loved', 'hello', 'help', 'helping', 'helped', 'pleasure', 'bye', 'goodbye', 'care', 'later', \
            'no','nothing', 'thanks', 'welcome', 'something', 'hey', 'am']
    print text
    text = text.lower()
    words = getWords_special_location(text)
    text = ''
    for i in words:
        if i not in d1:
            text = text + i.title() + ' '
        else:
            text = text + i + ' '
    print text
    from geotext import GeoText
    places = GeoText(text)
    print places.cities

list_cities("I am in GANDHINAGAR and AHMEDABAD, KARACHI, New York City, How About Some in madrid?")

#from geograpy import extraction
#e = extraction.Extractor(text="I am in GANDHINAGAR and AHMEDABAD, KARACHI, New York City, How About Some in madrid?")
#e.find_entities()
#print e.places
