import datetime
from django.db.models.functions import TruncDate


def fiil_zero_dates(items):
    items = list(items)
    dates = [x.get('date') for x in items]
    counts = [x.get('count') for x in items]
    
    new_items = []
    y = 0

    for d in (datetime.datetime.today() - datetime.timedelta(days=x) for x in range(0,30)):
        fd = datetime.datetime.date(d)
        if fd not in dates:
            new_items.append({'date': fd, 'count': 0})
        else:
            new_items.append({'date': fd, 'count': counts[y]})        
            y += 1

    return new_items

def generate_code(last_code):
    code_length = len(last_code)
    increment = int(last_code) + 1
    new_code = str(increment).zfill(code_length)    
    return new_code

def get_initials(full_name):
    name_list = full_name.split()
    initials = ""
    for name in name_list:
        initials += name[0].upper()
    return initials