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
            if i>4:
                break
        if i == 0:
            a = 'Sorry, no event of this type has been found in your area. ^ ^ ^ ^ ^'
        return a

    except requests.exceptions.RequestException:
        return 'HTTP Request failed'

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
