def get_tokens():
    '''
    This function returns the API key and the last used timestamp, where the download was stopped.
    This function uses the tokens.json file to store the API key and the timestamp.
    In case a file is not found, a new file is created and the user is prompted to enter the API key.
    
    Usage:
    API, timestamp = get_tokens()
    '''

    import os
    import json

    # if file not found, create a new file
    if not os.path.exists('tokens.json'):
        # prompt to enter the API key
        api_key = input('Enter your API key: ')
        with open('tokens.json', 'w') as f:
            json.dump({'ApiKey':api_key,'start':'1609459200','end':'1609459200'}, f,indent=4)

    # reading file into a dictionary
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)

    if len(tokens['ApiKey']) < 32:
        api_key = input('Enter your API key: ')
        with open('tokens.json', 'r') as f:
            tokens = json.load(f)
        tokens['ApiKey'] = api_key
        with open('tokens.json', 'w') as f:
            json.dump(tokens, f,indent=4)
    
    return tokens['ApiKey'], int(tokens['end'])