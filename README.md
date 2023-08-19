# WSD_lab_Q4

Lab Ex.4: Write an XML file and validate the file using XSD

Question: Employee Information XML Validation
You are tasked with creating an XML validation program to manage
employee information for a company. The program will involve creating
an XML document containing employee details, defining an XML schema
to validate the structure and constraints of the data, and performing XML
validation against the schema. The goal is to ensure that the employee data
adheres to the defined format and constraints.

Create:
1. The "employees.xml" file containing the employee data.
2. The "employee_schema.xsd" file containing the XML schema.
3. The "xml_validate.py" source code used for XML validation.

Steps:
Task 1: Create an XML Document 
Create an XML document named "employees.xml" that includes  information for at least three employees. Each employee should have the  following details: 
Personal Information: 
First Name 
Last Name 
Date of Birth (in the format YYYY-MM-DD) 
Gender (Male/Female) 
Employment Information: 
Position 
Salary
Contact Information: 
Email 
Phone Number

Task 2: Define XML Schema 
Create an XML schema (XSD file) named "employee_schema.xsd" to  define the structure and constraints for the employee data. The schema  should include the following requirements: 
• The root element should be named "employees". 
• Inside the "employees" element, there should be multiple  "employee" elements, each with the following attributes: o "id" (an integer value that uniquely identifies the employee). • Each "employee" element should contain nested elements for  personal information, employment information, and contact  information, adhering to the structure outlined above. 
Implement appropriate data types and constraints for each element, such  as restricting the gender values to "Male" or "Female" and ensuring valid  email formats.

Task 3: Perform XML Validation 
Write a program (in a programming language of your choice, preferably python) to perform XML validation against the created XML document  and the defined XML schema. The program should: 
• Load the XML document and XML schema. 
• Create an XML schema object. 
• Validate the XML document against the schema. 
• Display whether the XML document is valid or not. 
• If the document is not valid, provide a list of validation errors,  including the line and column numbers where each error occurs. 
Feel free to use relevant libraries or frameworks available in your chosen  programming language to assist in XML parsing and schema validation.
