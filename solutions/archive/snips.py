# TODO
class GeneralTree:
    """Generic tree node."""
    def __init__(self, data, children=None):
        self.data = data
        self.children=[]
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, GeneralTree)
        self.children.append(node)

    def __repr__(self):
        return self.data

    def prettyprint(self, count=0):
        space = '    '
        space = space * count
        if count==0:
            print(self.data)
        else:
            print(space, self.data)
        count+=1
        for i in self.children:
            i.prettyprint(count)


    def search(self, query):
        if query == self.data:
            print(self.data)
            return
        else:
            for i in self.children:
                i.search(query)

    def search_with_structure(self, query,node=None):
        if node is None:
            newnode = GeneralTree(self.data)
        else:
            newnode=node
        if query == self.data:
            newnode.prettyprint()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return 'what!'
        else:
            for i in self.children:
                x =copy.deepcopy(newnode)
                x.add_child(GeneralTree(i.data))
                i.search_with_structure(query, x)



def playing2():
    root = 'the roots'
    subnode1 = 'ATCQ'
    subnode3 = 'Jay Rock'
    asdfasdf = DLL()
    asdfasdf.push('shit!!!')
    test_tree = GeneralTree(root,
                            [GeneralTree(subnode3),
                             GeneralTree(subnode1,[GeneralTree('People Under the Stairs'), GeneralTree('Atmosphere'),GeneralTree('Slum Village')]),
                             GeneralTree('Travis Scott', [GeneralTree('Mos Def')]),
                             GeneralTree('Wu Tang', [GeneralTree('Cappadonna')])
                             ])
    # print(test_tree)
    test_tree.prettyprint()
    print('~ '*20)
    test_tree.search_with_structure('Cappadonna')



def playing(etree_root):
    """takes in element xml.etree.ElementTree.Element | ET.parse(XML_file).getroot()"""
    # global type_elems
    # global dll_list
    level += 1
    print("-----------------inside of 'playing', level: {}--------------".format(level))
    x = ET.tostring(etree_root)
    y = Node(x)
    for subnode in etree_elem:
        # iter_count += 1
        new_dll = copy.deepcopy(dll)
        new_dll.push(subnode)
        if 'type' in subnode.attrib.keys():
            type_elems.append(subnode)  # list of elements with 'type' in it
            dll_list.append(new_dll)  # list of DLLs
        else:
            if len(subnode) >= 1:
                # iter_count += 1
                get_parent_of_type(subnode, level, new_dll)

    return iter_count, type_elems, dll_list


# make rdbs schema out of py



# def bullocks():
#     counting = DLL()
#     counting.push(1)
#     counting.push(2)
#     counting.push(3)
#     counting.push(4)
#     counting.push(5)
#
#     print('here we go!')
#     # counting.listprint(counting.head)
#     print(counting.getlen())
#     print(len(counting))
#     # print(type(counting.head.next))
#     # print(counting.head.next.next)

g = list(tree.iter())

from xml.dom import minidom

root = minidom.parse(status_schema_path).documentElement
print(root)
print(root.childNodes)
print(type)
a = root.childNodes
print(a)

c = 1
for i in a:
    c += 1
    print(type(i))
    print(i)
    print('~')
    try:
        print(i.getAttribute)
    except:
        pass
    print('~')
    try:
        print(i.items())
    except:
        pass
print(c)

quit()

# generic_rough_draft_schema= files[4]
# generic_rough_draft_path = os.path.join(path, generic_rough_draft_schema)
# rough_draft_tree = ET.parse(generic_rough_draft_path, parser=None)
# status_schema_tree = rough_draft_tree
# root = rough_draft_tree.getroot()

# # sample_status = files[5]
# sample_status_path = os.path.join(path, sample_status)
# sample_status_tree = ET.parse(sample_status_path, parser=None)
# root = sample_status_tree.getroot()

#######################################
#   manually iterate through entire tree
#   61 elements in tree - total
#   7 elements in root - first lever
# 61 elements total
# 23 elements with TYPE
# 8 elements with built in type
# 15 global type
#######################################

# print(ET.tostring(child))
# print(child.tag)
# print(attr)
# print('TYPE OF ELEMENT: ', type_of_element)
# print('THIS IS THE DATA TYPE: ', attr_type)
# print('- ')
# print(ET.tostring(child))
# print(child.tag)
# print(attr)
# print('TYPE OF ELEMENT: ', type_of_element)
# print('THIS IS THE DATA TYPE: ', attr_type)
# print('ATTR NAME NAME: ', attr_name )
# print('- ')
####################

# for elem in elems_with_global_types:
#     global_type = elem.attrib['type']
#     print('------->', global_type)
#     for i in tree.iter():
#         tag_type = i.tag.split('}')[1]
#         if 'TYPESOFLOSS' in i.attrib.values(): #and 'type' not in i.attrib.values():
#             if tag_type== 'complexType' or tag_type == 'simpleType':
#                 print(i.tag.split('}')[1])
#                 print('number of children: ', len(i))
#                 print(i.attrib)
#                 print(ET.tostring(i))
#                 print(' ')

# for elem in elems_with_global_types:
#     global_type= elem.attrib['type']
#     print('--------------> type: ', elem.attrib['type'])
#     for node in tree.iter():
#         tag_type = node.tag.split('}')[1]
#         if global_type in node.attrib.values():
#             # if tag_type == 'complexType' or tag_type == 'simpleType':
#             print(tag_type)
#             print('number of children: ', len(node))
#             print(node.attrib)
#             print(node.tag)
#             print(ET.tostring(node))
#             print(' ')

this_table = 'test table'
these_columns = [
    'DOB DATETIME',
    'tile VARCHAR(225)',
    'due_data DATE', 'description TEXT'
]

def snips():
    pass
    # manual iter()
    """
    c = 0
    alL_elements = 0
    for child in root:
        attr = child.attrib
        element_name = child.tag.split('}')[1]
        element_list.append(element_name)
        num_child = len(child)

        # create iterators for metadata/validation
        if element_name not in unique_elements.keys():
            unique_elements[element_name] = 1
        else:
            unique_elements[element_name] += 1

        # print('# ' * 15)
        # print('ELEMENT NAME: ', element_name)
        # print(child.tag)
        # print(attr)
        # print('# of children: ', len(child))

        alL_elements += 1
        c += 1
        print('FIRST LEVEL-------------')
        if num_child >= 1:
            print(child)
            print('# of children: ', len(child))
            print('   SECOND LEVEL-------------')
            for child1 in child:
                num_child1 = len(child1)
                print('   -', child1)
                print('    ', '# of children: ', len(child1))
                alL_elements += 1
                if num_child1 >= 1:
                    print('      THIRD LEVEL-------------')
                    for child2 in child1:
                        print('      -', child2)
                        print('       ', '# of children: ', len(child2))
                        num_child2 = len(child2)
                        alL_elements += 1
                        if num_child2 >= 1:
                            print('         FOURTH LEVEL-------------')
                            for child3 in child2:
                                print('         -', child3)
                                print('          ', '# of children: ', len(child3))
                                num_child3 = len(num_child3)
                                alL_elements += 1
                                if num_child3 >= 1:
                                    print('            FIFTH LEVEL-------------')
                                    for child4 in child3:
                                        print('         -', child4)
                                        print('          ', '# of children: ', len(child4))
                                        num_child4 = len(num_child4)
                                        alL_elements += 1
        print(' ')
    print('counted elements: ', alL_elements)

    # print('for loop count result', c)
    print('\nunique elements/counts')
    for i, j in unique_elements.items():
        print(i, ' : ', j)
    """
    # # get repeating list of types
    # for child in status_schema_tree.iter():
    #     if 'type' in attr.keys():
    #         r = attr['type']
    #         if r not in list_of_types:
    #             list_of_types.append(r)
    #         # create UNIQUE list of built in data types & global types
    #         if r.startswith('xs:'):
    #             if r not in built_in_types:
    #                 built_in_types.append(r)
    #         # create UNIQUE list of global(custom) types
    #         else:
    #             global_types.append(r)
    #         if r not in type_count.keys():
    #             type_count[r] = 0
    #         else:
    #             type_count[r] += 0

    # try:
    #     ################################# THESE ARE ALL TYPES
    #     r = attr['type']
    #     attr_name = attr['name']
    #     # print(r)
    #     print('THIS IS THE ELEMENT NAME: ', attr_name)
    #     print("element/tag type: ",child.tag.split('}')[1])
    #
    #     print(ET.tostring(child))
    #     print(' ')
    #     # create list of ATTRIBUTES that have a type
    #     all_attrs_w_type.append(attr)
    #
    #     # get repeating list of types
    #     if r not in list_of_types:
    #         list_of_types.append(r)
    #     # create UNIQUE list of built in data types & global types
    #     if r.startswith('xs:'):
    #         if r not in built_in_types:
    #             built_in_types.append(r)
    #     # create UNIQUE list of global(custom) types
    #     else:
    #         global_types.append(r)
    #     if r not in type_count.keys():
    #         type_count[r] = 1
    #     else:
    #         type_count[r] += 1
    # except Exception as ex:
    #     pass

    # SEE ALL FIELDS
    # print('FIELD WITH BUILT IN DATA TYPES')
    # for i in all_attrs_w_type:
    #     if i['type'].startswith('xs:'):
    #         print(i)
    # print('')
    # print('')
    # print('FIELDS WITH GLOBAL DATA TYPES')
    # for i in all_attrs_w_type:
    #     if i['type'].startswith('xs:'):
    #         pass
    #     else:
    #         print(i)

    # empty_elem = 0
    # for elem in status_schema_tree.iter():
    #     elem_num_child = len(elem)
    #     # if elem_num_child == 0:
    #     #     element_name = elem.tag.split('}')[1]
    #     #     # print('ELEMENT: ', element_name)
    #     #     j = ET.tostring(elem)
    #     #     print(j)
    #     #     empty_elem += 1
    #     if elem_num_child == 1:
    #         j = ET.tostring(elem)
    #         print(elem.attrib)
    #         print(j)
    # print('EMPTY ELEMS: ', empty_elem)

# this will get me
# a list with all DI types and Custom Types
# an iterator that will give me everything that has that global type in it

def firstpass():
    print('--inside firstpass--')
    #############################
    #         sample files      #
    #############################
    path, dirs, files = next(os.walk(xsds_dir))

    # status_schema = files[0]
    status_schema = files[4]
    status_schema_path = os.path.join(path, status_schema)
    tree = ET.parse(status_schema_path, parser=None)
    root = tree.getroot()

    c1 = []
    c2 = []
    c3 = []

    elems_with_bi_types = []
    elems_with_global_types = []
    elems_simple = []
    elems_with_base = []
    ##############################################################
    ##############################################################
    #
    #       how to get all values & attributes / header
    #
    c = 0
    for node in tree.iter():
        tag = node.tag
        tag = tag.split('}')[1]             # type: str
        # elems w/ built-in types
        if 'type' in node.attrib.keys():
            c += 1
            if node.attrib['type'].startswith('xs:'):
                elems_with_bi_types.append(node)
            else:
                # elems w/ global types
                elems_with_global_types.append(node)
        # elems simple
        if tag == 'simpleType':
            elems_simple.append(node)
            c += 1
        # elems w/ base / restriction
        if 'base' in node.attrib.keys():
            elems_with_base.append(node)
            c += 1
    temp_list= elems_with_bi_types+elems_with_global_types+elems_simple+elems_with_base

    # for i in tree.iter():
    #     if i not in temp_list:
    #         c+=1
    #         print(c)
    #         print(ET.tostring(i))
    #         print(i.attrib)
    #         print(len(i))
    #         print(' ')
    # print('built in types')
    # for i in elems_with_bi_types:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('global in types')
    # for i in elems_with_global_types:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('simple elems')
    # for i in elems_simple:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('elems with base')
    # for i in elems_with_base:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))

    for i in tree.iter():
        if 'TYPESOFLOSS' in i.attrib.values() and 'type' not in i.attrib.values():
        # if 'phoneExt20' in i.attrib.values():
            print(i.tag.split('}')[1])
            print('number of children: ', len(i))
            print(i.attrib)
            print(i.tag)
            print(i)
            print(ET.tostring(i))
            print(' ')

    for elem in elems_with_global_types:
        global_type= elem.attrib['type']
        print('--------------> type: ', elem.attrib['type'])
        for node in tree.iter():
            tag_type = node.tag.split('}')[1]
            if global_type in node.attrib.values():
                # if tag_type == 'complexType' or tag_type == 'simpleType':
                print(node.tag.split('}')[1])
                print('number of children: ', len(node))
                print(node.attrib)
                print(node.tag)
                print(' ')

        print('____________________')

    # get all elements with base


def somethingelse():
    pass
    # for i in tree.iter():
    #     if i not in temp_list:
    #         c+=1
    #         print(c)
    #         print(ET.tostring(i))
    #         print(i.attrib)
    #         print(len(i))
    #         print(' ')
    # print('built in types')
    # for i in elems_with_bi_types:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('global in types')
    # for i in elems_with_global_types:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('simple elems')
    # for i in elems_simple:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
    # print(' ')
    # print('elems with base')
    # for i in elems_with_base:
    #     print(ET.tostring(i))
    #     print(i.attrib)
    #     # print(len(i))
# figure out what needs to be a header and what needs to be value




print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11')
asdfasdfasdf = DoublyLinkedList()
asdfasdfasdf.push('abc')
asdfasdfasdf.push('helllo')
asdfasdfasdf.push('god help me')
asdfasdfasdf.push('oooop')
asdfasdfasdf.push('324')
asdfasdfasdf.listprint(asdfasdfasdf.head)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11')
