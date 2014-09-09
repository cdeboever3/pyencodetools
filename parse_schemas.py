import json
import os
import pdb
import urlparse

# Schemas we don't want to parse,
IGNORE = ['access_key.json', 'mixins.json', 'namespaces.json']

def make_link_dict(dy='.'):
    """Make dict that maps titles to class names"""
    import glob
    d = {}
    files = glob.glob(os.path.join(dy, '*'))
    files = [x for x in files if os.path.split(x)[1] != 'namespaces.json']
    for fn in files:
        name = os.path.splitext(os.path.split(fn)[1])[0]
        f = open(fn)
        j = json.load(f)
        f.close()
        class_name = make_class_name(j['title'])
        d[name] = class_name
    return d

def make_class_name(title):
    words = title.split()
    for i,w in enumerate(words):
        words[i] = words[i][0].upper() + words[i][1:]
    return ''.join(words)

LINKTO = make_link_dict('/Users/cdeboever/git_repos/ENCODE-DCC/'
                        'encoded/src/encoded/schemas')

def make_classes(out, dy):
    import glob
    lines = []
    lines.append('from base import EncodeObject\n')
    fns = glob.glob(os.path.join(dy, '*'))
    for fn in fns:
        if os.path.split(fn)[1] not in IGNORE:
            lines += parse_schema(fn)
            lines[-1] = lines[-1] + '\n'
    f = open(out, 'w')
    f.write('\n'.join([x.expandtabs(4) for x in lines]) + '\n')
    f.close()

def parse_schema(fn):
    f = open(fn, 'r')
    d = json.load(f)
    f.close()
    lines = []
    # d['title'] is the class name
    class_name = make_class_name(d['title'])
    lines.append('class {}(EncodeObject):'.format(class_name))
    lines.append('\tdef __init__(self, accession, fetch=True):')
    lines.append('\t\tEncodeObject.__init__(self, accession)')
    lines.append('\t\tif fetch:')
    lines.append('\t\t\tself.fetch()\n')

    lines.append('\tdef _populate(self):')
    lines.append('\t\td = self.json_dict')

    # We'll pull attributes from d['properties'], d['calculated_props'], and
    # d['facets']. I need to check facets still.
    for k in ['properties', 'calculated_props']:#, 'facets']:
        if d.has_key(k):
            for kk in d[k].keys():
                t = parse_attr(kk, d[k][kk])
                if t:
                    lines += t

    # We'll assert that d['required'] exist.

    return lines

def parse_link_to(name, d):
    """Parse a linkTo from the schema"""
    lines = []
    # If the linkTo is a list, then the object can be of different types.
    if type(d['linkTo']) == list:
        for link in d['linkTo']:
            lines.append('\t\t\tif d[\'{}\'] == {}:'.format(name, LINKTO[link]))
            lines.append('\t\t\t\tself.{} '.format(name) + 
                         '= {}(d[\'{}\'], fetch=False)'.format(LINKTO[link], 
                                                               name))
    else:
        link = LINKTO[d['linkTo']]
        lines.append('\t\t\tself.{}.append({}'
                     '(t, fetch=False))'.format(name, link))
    return lines

def parse_string(name, d):
    """Parse attribute of type 'string'"""
    lines = []
    lines.append('\t\tif \'{}\' in d.keys():'.format(name))
    if d.has_key('linkTo'):
        lines += parse_link_to(name, d)
    else:
        lines.append('\t\t\tself.{0} = d[\'{0}\']'.format(name))
    return lines

# TODO: working here. Need to link this up for the object arrays.
# def parse_link_to_for_dict(name, d):
#     """Parse a linkTo that comes from an array attribute"""
#     lines = []
#     # If the linkTo is a list, then the object can be of different types.
#     if type(d['linkTo']) == list:
#         for link in d['linkTo']:
#             lines.append('\t\t\tif d[\'{}\'] == {}:'.format(name, LINKTO[link]))
#             lines.append('\t\t\t\tself.{} '.format(name) + 
#                          '= {}(d[\'{}\'], fetch=False)'.format(LINKTO[link], 
#                                                                name))
#     else:
#         link = LINKTO[d['linkTo']]
#         lines.append('\t\t\tself.{}.append({}'
#                      '(t, fetch=False))'.format(name, link))
#     return lines
# 
# def parse_string_for_dict(name, d):
#     """Parse object of type 'string' that comes from an array attribute"""
#     lines = []
#     lines.append('\t\tif \'{}\' in d.keys():'.format(name))
#     if d.has_key('linkTo'):
#         lines += parse_link_to(name, d)
#     else:
#         lines.append('\t\t\tself.{0} = d[\'{0}\']'.format(name))
#     return lines

def parse_array(name, d):
    """Parse attribute of type 'array'"""
    lines = []
    lines.append('\t\tif \'{}\' in d.keys():'.format(name))
    # If it's an array and the items type is object, I'll make a dict to store
    # the different stuff. Unfortunately, these items are just as complex as the
    # typical attributes so we have to do some work to parse them.
    if d['items']['type'] == 'object':
        lines.append('\t\t\tself.{} = {{}}'.format(name))
        lines.append('\t\t\tfor t in d[\'{}\']:'.format(name))

        for kk in d['items']['properties'].keys():
            lines += ['debug']
            lines.append()
            # TODO: Need to link this up to the methods above.

    else:
        lines.append('\t\t\tself.{} = []'.format(name))
        lines.append('\t\t\tfor t in d[\'{}\']:'.format(name))

        # If there is a linkTo, then this is an array of objects.
        if d['items'].has_key('linkTo'):
            link = LINKTO[d['items']['linkTo']]
            lines.append('\t\t\t\tself.{}.append({}'
                         '(t, fetch=False))'.format(name, link))
        elif d['items']['type'] == 'integer':
            lines.append('\t\t\t\tself.{}.append(int(t))'.format(name))
        elif d['items']['type'] == 'string':
            lines.append('\t\t\t\tself.{}.append(t)'.format(name))
    return lines

def parse_integer(name, d):
    """Parse attribute of type 'integer'"""
    lines = []
    lines.append('\t\tif \'{}\' in d.keys():'.format(name))
    lines.append('\t\t\tself.{0} = int(d[\'{0}\'])'.format(name))
    return lines

def parse_list(name, d):
    """Parse attribute of type 'list'"""
    lines = []
    if set(d['type']) == set(['number', 'string']):
        lines.append('\t\t\ttry:')
        lines.append('\t\t\t\tself.{0} = float(d[\'{0}\'])'.format(name))
        lines.append('\t\t\texcept ValueError:')
        lines.append('\t\t\t\tself.{0} = d[\'{0}\']'.format(name))
    elif set(d['type']) == set(['null', 'string']):
        lines.append('\t\t\ttry:')
        lines.append('\t\t\t\tself.{0} = d[\'{0}\']'.format(name))
        lines.append('\t\t\texcept ValueError:')
        lines.append('\t\t\t\tself.{0} = None'.format(name))
    return lines

def parse_attr(name, d):
    lines = []
   
    # These are attributes that I don't think are useful for now.
    if name in ['schema_version', 'status']:
        return None
    
    # Accession is special.
    elif name == 'accession':
        lines.append('\t\t# ENCODE accession')
        lines.append('\t\tself.accession = d[\'accession\']')
        
    else:
        # TODO: For now, I'm leaving title and description here. I'll probably
        # move them into documentation or something eventually and not litter
        # the code with comments.

        # Take care of title and description.
        if d.has_key('title') and d.has_key('description'):
            lines.append('\t\t# {}: {}'.format(d['title'], d['description']))
        elif d.has_key('title'):
            lines.append('\t\t# {}'.format(d['title']))
        elif d.has_key('description'):
            lines.append('\t\t# {}'.format(d['description']))
        # Some things have comments.
        if d.has_key('comment'):
            lines.append('\t\t# {}'.format(d['comment']))

        # If there is no type, I'll treat it like a string
        if not d.has_key('type'):
            lines += parse_string(name, d)
        elif d['type'] == 'integer':
            lines += parse_integer(name, d)
        elif d['type'] == 'string':
            lines += parse_string(name, d)
        elif d['type'] == 'array':
            lines += parse_array(name, d)
        # There is only one thing currently that has a list for its type. I'll
        # just handle this one specifically but I may have to make this more
        # general in the future.  tricky to parse but I can just account for
        # them directly.
        elif type(d['type']) == list:
            lines += parse_list(name, d)

    if d.has_key('enum'):
        lines.append('\t\tassert self.{} in {}'.format(name, str(d['enum'])))
    
    return lines

def main():
    make_classes('pyencodetools/classes.py', 
                 'submodules/encoded/src/encoded/schemas/')

if __name__ == '__main__':
    main()
