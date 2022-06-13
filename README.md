# hp_assignment
HP assignment to build a solution to parse files of various formats into a tabular structure, to be used to load to relational database.

**Execution steps:**

To execute, please run in below format:

main.py <input_file> <output_file_path> <file_format> <delimiter_if_txt_format>

Examples:

main.py C:/Users/703232480/PycharmProjects/pythonProject/json.txt C:/Users/703232480/PycharmProjects/pythonProject json
main.py C:/Users/703232480/PycharmProjects/pythonProject/text.txt C:/Users/703232480/PycharmProjects/pythonProject txt ,


**Assumptions:**

1. This solution accepts three formats - text (txt), json and xml.
2. Provided xml file seems to be incomplete and hence was not tested. A random xml structure has been taken from google for testing purpose, the same is uploaded in this repository for reference.
