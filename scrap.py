import httplib, urllib, base64, requests, json
import sys

def send_request(incoming):
    try:
        response = requests.post(
            url="https://api.allevents.in/events/list",
            headers={
                "Ocp-Apim-Subscription-Key": "9534780eb2f04a21a8a8e6f633fb7afa",
            },
            data=incoming,
        )
        content=response.content
        content=json.loads(content)
        i = 0
        a = ''
        while i < len(content['data']):
            a = a + content['data'][i]['eventname'] + '^' + \
                    content['data'][i]['start_time_display'] + '^' + \
                    content['data'][i]['venue']['full_address'] + '^' + \
                    content['data'][i]['thumb_url'] + '^' + \
                    content['data'][i]['share_url'] + '^'
            i=i+1
            if i>3:
                break
        if i == 0:
            a = 'jankiap50^Sorry, no event of this type has been found in your area. ^ ^ ^ ^'
        return a

    except requests.exceptions.RequestException:
        return 'HTTP Request failed'

def send_request_coord(incoming):

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '9534780eb2f04a21a8a8e6f633fb7afa',
    }

    params = urllib.urlencode({
        # Request parameters
        'category': 'football',
    })

    try:
        conn = httplib.HTTPSConnection('api.allevents.in')
        conn.request("POST", "/events/geo/?latitude=23.022505&longitude=72.5713621&radius=10&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        content=json.loads(data)
        i = 0
        a = ''
        while i < len(content['data']):
            a = a + content['data'][i]['eventname'] + '^' + \
                    content['data'][i]['start_time_display'] + '^' + \
                    content['data'][i]['venue']['full_address'] + '^' + \
                    content['data'][i]['thumb_url'] + '^' + \
                    content['data'][i]['share_url'] + '^'
            i=i+1
            if i>3:
                break
        if i == 0:
            a = 'jankiap50^Sorry, no event of this type has been found in your area. ^ ^ ^ ^'
        return a
        conn.close()
    except Exception as e:
        return("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################
'''incoming={
    "category": "football",
    "city": "Ahmedabad",
    "state": "GJ",
    "country": "In",
}

incoming={
    "category": sys.argv[1],
    "city": sys.argv[2],
    "state": sys.argv[3],
    "country": sys.argv[4],
}
'''
#print send_request(incoming)
###############################################################################
