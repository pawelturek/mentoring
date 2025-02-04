import xml.etree.ElementTree as ET


def compare_elements(el1, el2, path="", ignore_attributes=None):
    """Recursively compares two XML elements."""
    if ignore_attributes is None:
        ignore_attributes = []

    # Check if the tags are the same
    if el1.tag != el2.tag:
        print(f"Tag mismatch at path {path}: {el1.tag} vs {el2.tag}")
        return False

    # Check if the attributes are the same, ignoring specified attributes
    attrib1 = {k: v for k, v in el1.attrib.items() if k not in ignore_attributes}
    attrib2 = {k: v for k, v in el2.attrib.items() if k not in ignore_attributes}

    if attrib1 != attrib2:
        print(f"Attribute mismatch at path {path}: {attrib1} vs {attrib2}")
        return False

    # Compare children in both elements
    children1 = list(el1)
    children2 = list(el2)

    # Compare children element by element (recursively)
    for i, (child1, child2) in enumerate(zip(children1, children2)):
        if not compare_elements(child1, child2, f"{path}/{el1.tag}[{i}]", ignore_attributes):
            return False

    # Print details of extra children if they exist, but don't treat them as errors
    if len(children1) > len(children2):
        for extra in children1[len(children2):]:
            print(f"Extra child in element at path {path}: {extra.tag} with attributes {extra.attrib}")
    elif len(children2) > len(children1):
        for extra in children2[len(children1):]:
            print(f"Extra child in element at path {path}: {extra.tag} with attributes {extra.attrib}")

    return True


def compare_xml_files(file1, file2, ignore_attributes=None):
    """Compares two XML files."""
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    root1 = tree1.getroot()
    root2 = tree2.getroot()

    return compare_elements(root1, root2, path="root", ignore_attributes=ignore_attributes)


# Example of using the compare function
file1 = 'Sites_genqa564_BH29992.xml'
file2 = 'Sites_rochesandboxr1_BH29992.xml'

ignore_attributes = ["OID", "MetaDataVersionOID", "EffectiveDate"]  # Attributes to ignore in the comparison
if compare_xml_files(file1, file2, ignore_attributes):
    print("XML files have the same structure.")
else:
    print("XML files have structural differences.")

# Example of using the compare function




