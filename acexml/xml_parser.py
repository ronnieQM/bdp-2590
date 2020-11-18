import sys
import os
import warnings
import logging

import xml.etree.ElementTree as ET

class Rows:
    def __init__(self, database, table, rows=None):
        if rows is None:
            rows = []
        belongs_to_database = database
        belongs_to_table = table
        rows = rows

    def getrows(self):
        return self.rows


# --------------------------------------------------------------------

class XSD_Breakdown:
    def __init__(self):
        self.file = None
        self.elem_count = 0
        self.types = []
        self.custom_types = {}
        self.elems_with_attrs = []
        self.elements_with_type = []
        self.elements_with_attrs = []
        self.elem_names = []
        self.restrictions = []
        self.annotations = []
        self.simple_elements = []
        self.max_occurs = []
        self.restriction_types=[]

    # def get_unique_elems(self):
    #     elems = self.elems
    #     elems = list(set(elems))
    #     return elems

    def showall(self):
        text = """
file = {}
number of elements: {}
types of elements: {}

all data types: {}


custom data types: {}


simple elements: {}

max occurs: {}
        """.format(self.file, self.elem_count, self.elem_names, self.types,
                   list(self.custom_types.keys()), self.simple_elements, self.max_occurs)
        return text


class xElement:
    """An extension of the xml.etree.ElementTree class element.

    contains original xml.etree.ElementTree class from which this class instance was derived.

    len = number of element subelements
    """

    def __init__(self, etreeElement, tag, simple_tag, parent=None, attrib={}):
        if not isinstance(attrib, dict):
            raise TypeError("attrib must be dict, not {} ".format(attrib.__class__.__name__))
        self.tag = tag
        self.simple_tag = simple_tag
        self.parent = None
        self.children = []
        self.attrib = {**attrib}
        self.data_type = None

        self.indicators = []

        self.text = None
        self.keys = None
        self.et_element = etreeElement

        self.iscumstomtype = None
        self.max_occurs = None

    def isroot(self):
        if self.parent is None:
            return True
        return False

    def add_child(self, subelement):
        """Add *subelement* to the end of this element.
        """
        # self._assert_is_element(subelement)
        self.children.append(subelement)

    def extend(self, elements):
        return None

    def findall(self):
        # TODO
        return None

    def find(self):
        # TODO
        return None

    def set(self, key, value):
        self.attrib[key] = value

    def keys(self):
        """Get list of attribute names.
              Names are returned in an arbitrary order, just like an ordinary
              Python dict.  Equivalent to attrib.keys()
              """
        return self.attrib.keys()

    def __repr__(self):
        return "<{}, {} at {}>".format(self.__class__.__name__, self.tag, id(self))

    def __len__(self):
        return len(self.children)

    def makeelement(self, etreeElement):
        return self.__class__(etreeElement)

    def hastype(self):
        if self.data_type is None:
            return False
        return True

    def findroot(self):
        if self.parent is None:
            return self
        else:
            x = self.parent.findroot()
            return x

    def withattrs(self):
        return str(self.simple_tag + ' | ' + str(self.attrib))

    def print_simple(self):
        print(self.simple_tag, '|', self.attrib)

    def print_all(self, names=False,count=0):
        if count ==0:
            if names is True:
                if 'name' in self.attrib.keys():
                    print(self.simple_tag, ' | ', self.attrib['name'])
                else:
                    print(self.simple_tag, ' | ')
            else:
                print(self)
        count+=1

        if names is True:
            for i in self.children:
                if 'name' in i.attrib.keys():
                    print(i.simple_tag, '|', i.attrib['name'])
                else:
                    print(i.simple_tag, ' | ')
                if len(i.children) != 0:
                    i.print_all(names,count)
        else:
            for i in self.children:
                print(i)
                if len(i.children) != 0:
                    i.print_all(count=count)

    def pretty_print(self, attrs=False, count=0):
        spaces = '     '
        v = '│'
        c = '├──'
        e = '└──'
        spaces = spaces * count
        if count ==0:
            if attrs is True:
                attrib = self.attrib
            else:
                attrib = ''
            print(self.simple_tag, attrib)
            if not self.children:
                print('MESSAGE: element has not children, nothing pretty_print')
                return
        # if count ==0:
        #     if atters is True:
        #         attrib = self.attrib
        #     else:
        #         attrib = ''
        #     if not self.children:
        #         print('MESSAGE: element has not children, nothing pretty_print')
        #         print(self.simple_tag, attrib)
        #         return
        # if count ==0 and not self.isroot():
        #     print(self.simple_tag, attrib)

        count += 1
        for i in self.children:
            if attrs is True:
                attrib = i.attrib
            else:
                attrib = ''
            if count == 1:
                if i != self.children[-1]:
                    print(c, i.simple_tag, attrib)
                else:
                    print(e, i.simple_tag, attrib)
            else:
                if i != self.children[-1]:
                    print(v + spaces + c, i.simple_tag, attrib)
                else:
                    print(v + spaces + e, i.simple_tag, attrib)
            i.pretty_print(attrs, count)

    def iter(self):
        yield self
        for i in self.children:
            yield from i.iter()
    # def print_parents(self):


    def get_parents(self, count=0):
        if count==0:
            yield self
            yield self.parent
        else:
            yield self.parent
        if self.parent is not None:
            for i in self.parent.get_parents(count=1):
                if i is not None:
                    yield i

def subelement(parent, etreeElement):
    xelement = parent.makeelement(etreeElement)
    print('-' * 60)
    print('hi')
    print(type(xelement))
    parent.add_child(xelement)
    return element


# --------------------------------------------------------------------

class xElementTree:
    """An XML element hierarchy.
    This class also provides support for serialization to and from
    standard XML.
    *element* is an optional root element node,
    *file* is an optional file handle or file name of an XML file whose
        contents will be used to initialize the tree with.
    """

    def __init__(self, xelement=None, etree_root=None):
        if not xelement.isroot():
            logging.warning('LOOKS LIKE THIS ELEMENT IS NOT A ROOT')
        self.root = xelement  # first node
        self.etree_root = etree_root
        self.length = 0
        self.breakdown = None
        self.file = None

    def getroot(self):
        return self._root

    def pretty_print(self, atters=False):
        self.root.pretty_print(atters, count=0)

    def print_all(self, names=False):
        self.root.print_all(names)

    def get_breakdown(self):
        if self.breakdown is None:
            bd = build_breakdown(self)
            return bd
        else:
            return self.breakdown

    def iter(self):
        # assert self.root is node None
        # print(self.root)
        return self.root.iter()

    def __len__(self):
        return self.length
    # def get_count(self):
    #     count=1
    #     for i in self.root.children:
    #         count +=1
    #         if len(i) >=1:


# --------------------------------------------------------------------

def get_etree(xml_file_path):
    logging.info('inside xml2db.get_tree')
    etree = ET.parse(xml_file_path, parser=None)
    root = etree.getroot()
    return etree, root


def construct_xelem(elem, parent=None):
    node = elem
    # print(node)
    tag = node.tag
    simple_tag = node.tag.split('}')[1]
    max_occurs = None
    if tag == 'complexType':
        complextype = True
    else:
        complextype = False
    attrib = node.attrib
    keys = node.attrib.keys()
    if 'type' in node.attrib.keys():
        hastype = True
        data_type = node.attrib['type']
        if node.attrib['type'].startswith('xs:'):
            pass
            # logging.debug('node starts with xs')
        else:
            pass
            # TODO
            # append to xsd_breakdown.custometypes
            # logging.debug('node does NOT starts with xs')
    else:
        data_type = []
        hastype = False
    text = node.text
    xelem = xElement(node, tag, simple_tag, parent, attrib)
    # - - - - - - - - - - - - - - - - - - - -
    if 'maxOccurs' in node.attrib.keys():
        max_occurs = node.attrib['maxOccurs']
    # - - - - - - - - - - - - - - - - - - - -
    xelem.max_occurs = max_occurs
    xelem.hastype = hastype
    xelem.data_type = data_type
    xelem.keys = keys
    xelem.text = text
    xelem.complextype = complextype
    return xelem


def build_xtree(etree_elem, parent=None, level=1, elem_count=1):
    """takes in xml.etree.ElementTree.Element root element| ET.parse(XML_file).getroot()"""
    logging.debug("-----------------inside of 'build_xtree, level: {}--------------".format(level))
    elem = etree_elem
    level += 1
    if parent is None:
        logging.info('inside of build_xtree')
        xelem = construct_xelem(etree_elem)
        xTree = xElementTree(xelem, etree_root=etree_elem)
    else:
        xTree = None
        xelem = parent
    for sub_elem in elem:
        elem_count += 1
        sub_xelem = construct_xelem(sub_elem)
        sub_xelem.parent = xelem
        xelem.add_child(sub_xelem)
        if len(sub_elem) >= 1:
            _, _, elem_count = build_xtree(sub_elem, sub_xelem, level, elem_count)
    logging.debug('elem count:   ' + str(elem_count))
    if parent is None:
        xTree.length = elem_count
    return xTree, xelem, elem_count


# -------------------------------------------------------------------------------------------------------------------
def to_string(xelem):
    return ET.tostring(xelem.et_element)
# -------------------------------------------------------------------------------------------------------------------
def build_breakdown(xtree):
    """parses through XML document and returns summary statistics"""
    logging.info('building XML breakdown')
    # assert that it's infact a xtree instance
    # OR an xml path
    breakdown = XSD_Breakdown()

    c = 0
    type_list = []
    custom_types = {}
    xelems_with_type = {}
    xelems_with_attrs = []
    simple_elems = []
    elem_names = []
    attributes = []
    restrictions = []
    restriction_types=[]
    annotations = []
    max_occurs = []
    for xelem in xtree.iter():
        et_element = xelem.et_element
        elem_name = et_element.tag.split('}')[1]
        elem_names.append(elem_name)
        # logging.debug(ET.tostring(et_element))
        # -------------------------------
        attrs = et_element.attrib
        if len(attrs) >= 1:
            attributes.append(attributes)
            xelems_with_attrs.append(xelem)
        # -------------------------------
        if 'type' in et_element.attrib.keys():
            type_ = et_element.attrib['type']
            if type_ not in xelems_with_type:
                xelems_with_type[type_] = []
            xelems_with_type[type_].append(xelem)
            type_list.append(type_)
            if type_.startswith('xs:'):
                pass
                # TODO
                # check if built in type is NOT in convert dictionary
            else:
                if type_ not in custom_types.keys():
                    custom_types[type_] = xelem
        # -------------------------------
        if elem_name == 'annotation':
            annotations.append(xelem)
            # print(elem_name)
        # -------------------------------
        if elem_name == 'element':
            simple_elems.append(xelem)
        if 'maxOccurs' in et_element.attrib.keys():
            max_occurs.append(xelem)
        if elem_name == 'restriction':
            restrictions.append(xelem)
            restriction_types.append(xelem.attrib['base'])



        c += 1
    # ----------------------------------
    breakdown.file=xtree.file
    breakdown.elem_count = c
    breakdown.types = list(set(type_list))
    breakdown.elem_names = list(set(elem_names))
    breakdown.custom_types = custom_types
    breakdown.elements_with_type = xelems_with_type
    breakdown.elements_with_attrs = xelems_with_attrs
    breakdown.annotations = annotations
    breakdown.simple_elements = simple_elems
    breakdown.max_occurs = max_occurs
    breakdown.restrictions=restrictions
    breakdown.restriction_types = list(set(restriction_types))
    # ----------------------------------
    logging.info('finished building breakdown')
    # for i, j in xelems_with_type.items():
    #     print(len(j),i,':', '\n',j)
    # for i in elem_names:
    #     print(i)
    return breakdown


# -------------------------------------------------------------------------------------------------------------------

def get_xtree(xml_file_path):
    """ abstraction of the the build_tree function which takes in an xml file path and returns
        an xtree class which contains the root node.
    """
    _, root = get_etree(xml_file_path)
    xtree, xroot, elem_count = build_xtree(root)
    xtree.file = xml_file_path
    return xtree


def generate_db_schema(xsd_file_path, database_name=None):
    if database_name is None:
        db_name = 'FOOBAR_DB_PLEASE_RENAME'
    _, root = get_etree(xsd_file_path)

    # dev -----------------------------------------------------------------------
    tables = ['StandardStatusExports', 'Contacts', 'Phones']
    columns = ['name', 'office', 'age', 'job_title']

    # -----------------------------------------------------------------------/dev
    return

def scan_xml(xml_file):
    pass


class DataBase:
    def __init__(self):
        self.name=None
        self.tables=[]

    def to_string(self):
        string = 'TODO'
        return string


class Table:
    def __init__(self,name, columns,parent, child):
        self.name=name
        self.columns=columns
        self.child_elem=parent
        self.parent_elem=child

    def to_string(self):
        text="""
        table: {}
        columns: {}
        *table_elem: {}
        *max_occurs_elem:{}
        """.format(self.name, self.columns, self.child_elem.withattrs(),self.parent_elem.withattrs())
        return text
