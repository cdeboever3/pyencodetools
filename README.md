pyencodetools
=============

Python wrapper for ENCODE (Encyclopedia of DNA Elements) API and tools for
working with the data.

# How to Use


# Developing

If you want to work on the source code, start by initializing and updating the 
ENCODE submodule:

	git submodule init
	git submodule update

## Strategy

My overall goal for this package is to provide a nice Python interface for the
[ENCODE API](https://www.encodeproject.org/help/rest-api/). I have created a
general class `EncodeRecord` that wraps results from GET requests to the API.
My plan is to add parses for various types of data returned from ENCODE to make
the information more useful.  For instance, rather than just setting a
"culture_harvest_date" as a string, I can convert is to a datetime object that
is more useful within Python.
