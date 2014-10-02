import json
import re
import requests
import urlparse
import warnings

HEADERS = {'accept': 'application/json'}
ROOT_URL = 'https://www.encodeproject.org'
SHORT_URL_PATTERN = re.compile('^/.*/.*/$')

def _parse_attr_string(s):
    """
    Parse string from ENCODE. If possible, return an ENCODERecord object, float,
    int, etc. If not, just return a string representation.

    Parameters
    ----------
    s : str
        String from ENCODE. Can be a short URL (e.g. /human-donors/ENCDO000AAE/)
        or some other kind of string.

    Returns
    -------
    out : some object
        If s matches SHORT_URL_PATTERN, an ENCODERecord object will be returned
        (but it's attributes will not be fetched to prevent unnecessary calls to
        ENCODE). Otherwise, a float, int, or string will be returned.

    """
    if SHORT_URL_PATTERN.match(s):
        out = ENCODERecord(s, fetch=False)
    else:
        if '.' in s:
            try:
                out = float(s)
            except ValueError:
                out = str(s)
        else:
            try:
                out = int(s)
            except ValueError:
                out = str(s)
    return out

def query(url):
    """Query ENCODE API and return dict with results"""
    response = requests.get(url, headers=HEADERS)
    response_json_dict = response.json()
    if response.status_code != 200:
        warnings.warn('Response status {} from '
                      'ENCODE'.format(response.status_code))
        return None
    else:
        return response_json_dict

def search(term, limit=25):
    """This searches the ENCODE database for the phrase term"""
    url = urlparse.urljoin(ROOT_URL, 'search/?searchTerm={}'.format(term))
    url += '&format=json&frame=object&limit={}'.format(limit)
    response_json_dict = query(url)
    if res:
        if len(response_json_dict['@graph']) == 0:
            return []
        else:
            out = []
            for d in response_json_dict['@graph']:
                out.append(ENCODERecord(d['uuid'], json_dict=d))
            return out
    else:
        return None

def fetch(identifier):
    """
    Fetch object from ENCODE

    Parameters
    ----------
    identifier : str
        ENCODE accession, short URL (e.g. /human-donors/ENCDO000AAE/), or 
        long URL (e.g.) https://www.encodeproject.org/biosample/ENCBS000AAA/.

    Returns
    -------
    obj : some object
        If identifier is successfully fetched from ENCODE, obj will be the 
        object that corresponds to identifier (e.g. Biosample, Donor, etc.).
        If the identifier can't be fetched, obj will be None.

    """
    e = ENCODERecord(identifier)
    if e.json_dict is None:
        return None
    else:
        return e

class ENCODERecord(object):
    def __init__(self, identifier, json_dict={}, fetch=True):
        self._identifier = identifier
        self.fetched = False
        assert type(json_dict) == dict
        self.json_dict = json_dict
        if self.json_dict != {}:
            self._populate()
            self.fetched = True
        if fetch:
            self.fetch()
    
    def __getattr__(self, name):
        if not self.fetched:
            self.fetch()
        if hasattr(self, name):
            return self.name
        else:
            raise AttributeError
    
    def fetch(self):
        """Fetch object from ENCODE and populate attributes"""
        # Long URL. If the first 30 characters are the ENCODE URL, we'll try to
        # submit the identifier as the URL.
        if self._identifier[0:30] == 'https://www.encodeproject.org/':
            self._query_url = self._identifier

        # Short URL.
        elif '/' in self._identifier:
            self._query_url = urlparse.urljoin(ROOT_URL, self._identifier)
            self._query_url = urlparse.urljoin(self._query_url, '?frame=object')

        # Assume we have an accession or a UUID.
        else:
            self._query_url = urlparse.urljoin(ROOT_URL, self._identifier)
            self._query_url = urlparse.urljoin(self._query_url, '?frame=object')

        response = requests.get(self._query_url, headers=HEADERS)
        if response.status_code == 200:
            self.json_dict = response.json()
        else:
            self.json_dict = None

        self._populate()
        self.fetched = True

    def _populate(self):
        """Set various attributes"""
        for k in self.json_dict:
            if type(k) == unicode:
                k = str(k)

            val = self.json_dict[k]

            if type(val) == str or type(val) == unicode:
                self.__dict__[k] = _parse_attr_string(val)
            elif val == [] or val == {}:
                pass
            elif (type(val) == list and 
                  set([type(x) for x in val]) == set([unicode])):
                self.__dict__[k] = [_parse_attr_string(x) for x in
                                    val]
            else:
                self.__dict__[k] = str(val)
