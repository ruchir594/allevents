import time

def convert_return(z):
    a = ''
    i=0
    for each in z:
        a = a + each[0] + '^' + each[1] + '^' + each[2] + '^' + each[3] + '^' + each[4] + '^'
        i=i+1
        if i>4:
            break
    return a

def get_per_day(a, e):
    a = a.lower()
    today = time.strftime("%d/%m/%Y")
    tmy = today.split('/')
    m = tmy[1]
    t = tmy[0]
    if m == '01':
        m = 'Jan'
    if m == '02':
        m = 'Feb'
    if m == '03':
        m = 'Mar'
    if m == '04':
        m = 'Apr'
    if m == '05':
        m = 'May'
    if m == '06':
        m = 'Jun'
    if m == '07':
        m = 'Jul'
    if m == '08':
        m = 'Aug'
    if m == '09':
        m = 'Sep'
    if m == '10':
        m = 'Oct'
    if m == '11':
        m = 'Nov'
    if m == '12':
        m = 'Dec'
    if a == 'today':
        a = t
    if a == 'tomorrow':
        a = int(t) + 1
        if a < 10:
            a = '0'+str(a)
        else:
            a = str(a)
    tq = m + ' ' + a
    #print tq
    z = []
    for each in e:
        if each[1].find(tq) != -1:
            z.append(each)
    return convert_return(z)

def sort_generation(result, res_nle):
    result = result.split('^')
    i = 0
    r = []
    while i < len(result)-1:
        r.append([result[i], result[i+1], result[i+2], result[i+3], result[i+4]])
        i=i+5
    # day wise
    if res_nle.day != []:
        a = res_nle.day[0]
        return get_per_day(a, r)
    ################################
    return convert_return(r)
