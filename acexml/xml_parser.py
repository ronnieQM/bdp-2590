import sys
import os
import warnings
import logging

import xml.etree.ElementTree as ET


class Database:
    def __init__(self, tables=[], name=None):
        self.name = name
        self.tables = tables

    def __repr__(self):
        return "This database is called '{}'. It has the tables: {}".format(self.name, self.tables)


class Table:
    def __init__(self, fields):
        fields = []


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
        self.elem_count = count
        self.list_of_types = types
        self.built_in_types = []
        self.custom_types = []
        self.elems = tags
        self.restrictions = restrictions
        self.texts = texts
        self.annotation = []
        self.file = file

    def get_unique_elems(self):
        elems = self.elems
        elems = list(set(elems))
        return elems

    def __repr__(self):
        file = os.path.basename(self.file)
        unique_types = self.get_unique_elems()
        str_ = """
        file = {}
        number of elements: {}
        types: {}
        unique types: {}
        custom types: {}
        restrictions = {}
        annotations ={}
        """.format(file,
                   self.elem_count,
                   self.list_of_types,
                   unique_types,
                   self.custom_types,
                   self.restrictions,
                   self.annotation)


class xElement:
    """An extension of the xml.etree.ElementTree class element.

    contains original xml.etree.ElementTree class from which this class instance was derived.

    len = number of element subelements
    """

    def __init__(self, etreeElement, tag, parent=None, attrib={}):
        if not isinstance(attrib, dict):
            raise TypeError("attrib must be dict, not {} ".format(attrib.__class__.__name__))
        self.tag = tag
        self.parent = None
        self.children = []
        self.attrib = {**attrib}
        self.data_type = None

        self.indicators = []

        self.text = None
        self.keys = None
        self.etree = etreeElement

        self.iscumstomtype = None

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
        return "<{}, {}>".format(self.__class__.__name__, self.tag)

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

    def print_all_sub_elements(self):
        for i in self.children:
            print(i)
            if len(i.children) != 0:
                i.print_all_sub_elements()

    def pretty_print(self, count=0):
        tabs = '  '
        for i in self.children:
            print(i)
            count = count + 1
            tabs = tabs * count
            print(tabs, '|')
            print(tabs, i)
            if len(i.children) >= 1:
                i.pretty_print(count)

    # def iscustomtype(self):
    #     if self.data_type


def subelement(parent, etreeElement):
    xelement = parent.makeelement(etreeElement)
    print('-' * 60)
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

    def __init__(self, xelement=None):
        self.root = xelement  # first node

    def getroot(self):
        return self._root


# --------------------------------------------------------------------

def get_etree(xml_file_path):
    logging.info('inside xml2db.get_tree')
    etree = ET.parse(xml_file_path, parser=None)
    root = etree.getroot()
    return etree, root


def construct_xelem(elem, parent=None):
    node = elem
    tag = node.tag
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
    xelem = xElement(node, tag, parent, attrib)
    # - - - - - - - - - - - - - - - - - - - -
    xelem.hastype = hastype
    xelem.data_type = data_type
    xelem.keys = keys
    xelem.text = text
    xelem.complextype = complextype
    return xelem


def build_xtree(etree_elem, parent=None, level=1, elem_count=1):
    """takes in element xml.etree.ElementTree.Element | ET.parse(XML_file).getroot()"""
    logging.info("-----------------inside of 'build_xtree, level: {}--------------".format(level))
    # logging.debug('  '+ str(elem_count))
    level += 1
    elem_count += 1
    elem = etree_elem
    if parent is None:
        xelem = construct_xelem(etree_elem)
        # xTree = xElementTree(xelem)
    else:
        xelem = parent

    for sub_elem in elem:
        elem_count += 1
        sub_xelem = construct_xelem(sub_elem)
        sub_xelem.parent = xelem
        xelem.add_child(sub_xelem)
        if len(sub_elem) >= 1:
            build_xtree(sub_elem, sub_xelem, level, elem_count)
    return xelem


# -------------------------------------------------------------------------------------------------------------------


def generate_db_schema(xml_file_path, database_name=None):
    _, root = get_etree(xml_file_path)

    # -----------------------------------------------------------------------s\
    tables = ['StandardStatusExports', 'Contacts', 'Phones']
    db_name = 'bd_work'
    database = Database(tables, db_name)
    # -----------------------------------------------------------------------s\
    x = build_xtree(root)
    database = x

    return database
