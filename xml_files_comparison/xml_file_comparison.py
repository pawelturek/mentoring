import xml.etree.ElementTree as ET

# ANSI escape sequences for red and green
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'


def compare_elements(e1, e2, path="", ignored_attributes=None):
    # Initialize ignored_attributes if not provided
    ignored_attributes = ignored_attributes or set()

    # Compare the tag names
    if e1.tag != e2.tag:
        print(f"Different tags at {path}: {e1.tag} != {e2.tag}")

    # Compare the number of children
    if len(e1) != len(e2):
        print(f"Different number of children at {path}: {len(e1)} != {len(e2)}")

    # Compare attributes, but ignore specified attributes
    e1_attrib = {k: v for k, v in e1.attrib.items() if k not in ignored_attributes}
    e2_attrib = {k: v for k, v in e2.attrib.items() if k not in ignored_attributes}

    if e1_attrib != e2_attrib:
        print(f"Different attributes at {path}:")
        # Print attribute differences one line under the other
        for attr in e1_attrib:
            if attr in e2_attrib:
                if e1_attrib[attr] != e2_attrib[attr]:
                    print(f"{RED}{attr}: {e1_attrib[attr]}{RESET}")
                    print(f"{GREEN}{attr}: {e2_attrib[attr]}{RESET}")
            else:
                # Attribute in e1 but not in e2
                print(f"{RED}{attr}: {e1_attrib[attr]}{RESET}")
        for attr in e2_attrib:
            if attr not in e1_attrib:
                # Attribute in e2 but not in e1
                print(f"{GREEN}{attr}: {e2_attrib[attr]}{RESET}")

    # Compare the text content
    if e1.text != e2.text:
        print(f"Different text at {path}: {e1.text} != {e2.text}")

    # Recursively compare each child element
    compare_children(e1, e2, path, ignored_attributes)


def compare_children(e1, e2, path, ignored_attributes):
    children1 = list(e1)
    children2 = list(e2)

    max_len = max(len(children1), len(children2))

    # Compare children one by one
    for i in range(max_len):
        # Check if children exist at index i in both XMLs
        child1 = children1[i] if i < len(children1) else None
        child2 = children2[i] if i < len(children2) else None

        child_path = f"{path}/{child1.tag if child1 else child2.tag}"

        if child1 is None:
            print(f"\n{RED}Child missing at {child_path}. Parent element data:\n{RESET}")
            print_element(e1, path)  # Print parent element data from the first XML
            print(f"{GREEN}Child missing at {child_path}. Parent element data:\n{RESET}")
            print_element(e2, path)  # Print parent element data from the second XML
        elif child2 is None:
            print(f"\n{GREEN}Child missing at {child_path}. Parent element data:\n{RESET}")
            print_element(e2, path)  # Print parent element data from the second XML
            print(f"{RED}Child missing at {child_path}. Parent element data:\n{RESET}")
            print_element(e1, path)  # Print parent element data from the first XML
        else:
            # Compare the children recursively
            compare_elements(child1, child2, child_path, ignored_attributes)


def print_element(element, path):
    """
    Helper function to print out the element's full tag, attributes, and text content for comparison.
    """
    attrib_str = " ".join([f'{key}="{value}"' for key, value in element.attrib.items()])
    print(f"{path} <{element.tag} {attrib_str}> {element.text.strip() if element.text else ''}</{element.tag}>")


def compare_xml_files(file1, file2, ignored_attributes=None):
    # Parse the XML files
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # Get the root of both trees
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # Start comparing from the root elements
    compare_elements(root1, root2, ignored_attributes=ignored_attributes)


# Example usage:
file1 = 'Sites_genqa564_BH29992.xml'
file2 = 'Sites_rochesandboxr1_BH29992.xml'

# Specify the attributes you want to ignore during comparison
ignored_attributes = {}

compare_xml_files(file1, file2, ignored_attributes)










