

def datefilter(value):
    if not value:
        return ''
    return value.strftime('%Y-%m-%d')
