def set_loader(path):
    '''
    Load lines in text file as a set(). 
    '''
    keyFile = path
    keySet  = set()
    try:
        with open(keyFile, "r", encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                if len(line) > 0:
                    keySet.add(line)
    except:
        print('No list loaded to set().')
    return keySet


def dict_loader(path):
    '''
    Load lines in text file as a dict(). 
    '''
    keyFile = path
    keyDict = dict()
    try:
        with open(keyFile, "r", encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                if len(line) > 0:
                    keyDict[line]=''
    except:
        print('No list loaded to dict().')
    return keyDict

