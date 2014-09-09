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

My overall goal for this package is to provide class for the various JSON
objects that the [ENCODE API](https://www.encodeproject.org/help/rest-api/)
returns. ENCODE has nice [json
schemas](https://github.com/ENCODE-DCC/encoded/tree/master/src/encoded/schemas)
that describe the different types of JSON objects that ENCODE works with. I
couldn't find any suitable tools for converting JSON schemas into Python
classes, so I took a very hacky approach and wrote a script that parses the
schemas and prints out valid Python classes. Another perhaps more elegant option
would have been to read the schemas and create the classes on the fly. However, 
I couldn't devise an implementation of this approach that was satisfactory so I
went with my hacky approach. This approach may not be tenable as ENCODE
continues to update the schemas and they presumably become more complex.
