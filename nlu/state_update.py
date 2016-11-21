import csv

state_user = 'state_user.csv'
delim = ','

def push_in_csv(user_id, start_state):
    with open(state_user, 'a') as csvfile:
        fieldnames = ['user_id', 'current_state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'user_id': user_id, 'current_state': start_state})

def get_current_state_user(user_id, start_state = 'st001'):
    file_su = csv.reader(open(state_user,"r"),delimiter=delim)
    for row in file_su:
        if row[0] == user_id:
            return row[1]
    # if the user is new, i.e. no record of him is found, we push a new record for that id.
    push_in_csv(user_id, start_state)
    return start_state
