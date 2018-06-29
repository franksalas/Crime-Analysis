import googlemaps
import gmaps
import requests
import numpy as np

def block_split(df):
    '''
    split blockrange col values
    then give median value as a string
    '''
    first = df.BlockRange.str.split(pat='-',expand=True)[0].astype('int')
    second = df.BlockRange.str.split(pat='-',expand=True)[1].astype('int')
    med = np.ceil((second + first)/2).astype('int')
    med = med.astype('str')
    street = df.StreetName
    #res = med + " " + street
    return med


def gm_geocode(address,API_KEY):
    loc = '{}, Houston, TX'.format(address)
    gmaps = googlemaps.Client(key=API_KEY)
    r = gmaps.geocode(loc)
    lat_lng = tuple(r[0]['geometry']['location'].values())
    full_add = r[0]['formatted_address']
    return lat_lng, full_add



def get_geocode(loc,key):
    '''input address and api key
    return tuple with lat and long'''
    address = '{}, Houston, TX'.format(loc)
    pa = {'address': address, 'key':key}
    URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(URL,params=pa)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e) # not 200
    js_obj = response.json()
    if js_obj['status'] == 'OK':
        gps = tuple(js_obj['results'][0]['geometry']['location'].values())
        return gps
    elif js_obj['status'] =='OVER_QUERY_LIMIT':
        return np.nan
    else:
        print(js_obj['status'])
        return js_obj['status']

