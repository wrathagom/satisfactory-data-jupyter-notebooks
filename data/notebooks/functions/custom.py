# Borrowed from here: https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
  
def format_number(num):
    """Format numbers in a human-friendly way"""
    if num >= 1_000_000:
        return f'{num/1_000_000:.1f}M'
    elif num >= 1_000:
        return f'{num/1_000:.1f}K'
    else:
        return f'{num:.0f}'
      
def list_endpoints():
    endpoints = ['getAssembler', 'getBelts', 'getCables', 'getExtractor', 'getFoundry',
    'getGenerators', 'getHypertube', 'getLifts', 'getManufacturer', 'getStorageInv', 'getConstructor',
    'getStorageInv', 'getPackager', 'getPipes', 'getPower', 'getRefinery', 'getSmelter', 'getSplitterMerger', 'getTrainRails']

    return endpoints