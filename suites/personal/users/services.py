import datetime
from django.db.models.functions import TruncDate


def fillZeroDates(items):
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