import xmlschema as xml
xml_file = "Q4\employees.xml"
xsd_file = "Q4\employee_schema.xsd"

XML_SCHEMA = xml.XMLSchema(xsd_file)

if XML_SCHEMA.is_valid(xml_file):
    print("The XML file is vaild against the XSD schema.")
else:
    print("Sorry, XML file is not well formed or valid against the XSD schema")
    print(XML_SCHEMA.validate(xml_file))