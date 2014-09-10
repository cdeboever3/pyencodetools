import json
import requests
import urlparse

HEADERS = {'accept': 'application/json'}
ROOT_URL = 'https://www.encodeproject.org'

def search(term, limit=25):
    # This searches the ENCODE database for the phrase "bone chip"
    url = urlparse.urljoin(ROOT_URL, 'search/?searchTerm={}'.format(term))
    url += '&format=json&frame=object&limit={}'.format(limit)

    response = requests.get(url, headers=HEADERS)
    response_json_dict = response.json()
    if response.status_code != 200:
        return None
    elif len(response_json_dict['@graph']) == 0:
        return []
    else:
        out = []
        for d in response_json_dict['@graph']:
            c = class_conversion(d['@type'][0])
            out.append(c(d['uuid'], json_dict=d))
        return out

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
    e = EncodeObject(identifier)
    if e.json_dict is None:
        return None
    else:
        return class_conversion(e.json_dict['@type'][0])(identifier,
                                                       json_dict=e.json_dict)

class EncodeObject(object):
    def __init__(self, identifier, json_dict={}, fetch=False):
        self.identifier = identifier
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
        """
        Fetch object from ENCODE

        Parameters
        ----------
        identifier : str
            ENCODE accession, short URL (e.g. /human-donors/ENCDO000AAE/), or 
            long URL (e.g.) https://www.encodeproject.org/biosample/ENCBS000AAA/

        Returns
        -------
        obj : some object
            If identifier is successfully fetched from ENCODE, obj will be the 
            object that corresponds to identifier (e.g. Biosample, Donor, etc.).
            If the identifier can't be fetched, obj will be None.

        """
        # Long URL. If the first 30 characters are the ENCODE URL, we'll try to
        # submit the identifier as the URL.
        if self.identifier[0:30] == 'https://www.encodeproject.org/':
            self.query_url = self.identifier

        # Short URL
        elif '/' in self.identifier:
            self.query_url = urlparse.urljoin(ROOT_URL, self.identifier)
            self.query_url = urlparse.urljoin(self.query_url, '?frame=object')

        # Assume we have an accession.
        else:
            self.query_url = urlparse.urljoin(ROOT_URL, self.identifier)
            self.query_url = urlparse.urljoin(self.query_url, '?frame=object')

        response = requests.get(self.query_url, headers=HEADERS)
        if response.status_code == 200:
            self.json_dict = response.json()
        else:
            self.json_dict = None

        self._populate()
        self.fetched = True
        
    def _populate(self):
        """This should be implemeted in subclasses"""
        pass

