pyencodetools
=============

Python wrapper for ENCODE (Encyclopedia of DNA Elements) API and (eventually)
tools for working with the data.

## Installation

Clone this repository and change into the repo directory. Run 

	python setup.py install

or 

	python setup.py develop

if you want to work on the source code.

## Usage

### Starting with an ENCODE identifier

If you have an ENCODE identifier such as a

 * long URL: https://www.encodeproject.org/biosample/ENCBS000AAA/
 * short URL: /biosample/ENCBS000AAA/
 * accession: ENCBS000AAA
 * UUID: 56e94f2b-25ac-4c58-9828-f63b66220999

you can query the ENCODE API as follows:

	import pyencodetools as pet
	res = pet.fetch('ENCBS000AAA')

`fetch` can take as input different identifiers and query the ENCODE API.
`fetch` returns an `ENCODERecord` object with attributes that correspond to the
keys of the JSON response dict from ENCODE. You can also instantiate an object
directly:

	res = pet.ENCODERecord('56e94f2b-25ac-4c58-9828-f63b66220999')

### Search

You can search the ENCODE API as follows:

	search_res = pet.search('bone chip')

`search_res` will be a list of `ENCODERecord` objects that match the search
term. There is a default limit on the numer of results returned that can be
changed:

	search_res = pet.search('bone chip', limit=10)

#### Advanced Search

If you want to search using ENCODE's search parameters, begin your search term
with '?'. For instance, the following query returns all DNAse experiments in
human (up to a limit of 1,000 experiments):

	search_res = pet.search('?type=experiment&assay_term_name=DNase-seq&replicates.library.biosample.donor.organism.scientific_name=Homo%20sapiens', limit=1000)

You can see how these types of queries are constructed by looking at the
[ENCODE API documentation](https://www.encodeproject.org/help/rest-api/) or by
going to one of the ENCODE data pages (such as the [Assays
page](https://www.encodeproject.org/search/?type=experiment) and applying some
of the filters on the left side of the page. As you apply the filters, the URL
will update with the appropriate search term.

## Development

If you want to work on the source code, start by initializing and updating the 
ENCODE submodule:

	git submodule init
	git submodule update

### Strategy

My overall goal for this package is to provide a nice Python interface for the
[ENCODE API](https://www.encodeproject.org/help/rest-api/). I have created a
general class `EncodeRecord` that wraps results from GET requests to the API.
My plan is to add parsers for various types of data returned from ENCODE to make
the information more useful.  For instance, rather than just setting a
"culture_harvest_date" as a string, I can convert is to a datetime object that
is more useful within Python.
