import json
import os
import sys
import pandas as pd
import xml.etree.ElementTree as et


def parse_txt_file(input_file, delimiter, output_file_path):
    '''

    :param input_file: Input file to be parsed
    :param delimiter: Separator for the input text file
    :param output_file_path: Path where the parsed output file will be written to
    :return: None
    '''

    df = pd.read_csv(input_file, sep=delimiter, header=0)
    output_file_basename = '{}_parsed.txt'.format(os.path.basename(input_file).split('.')[0])
    output_file = os.path.join(output_file_path, output_file_basename)
    df.to_csv(output_file, sep='\t', index=False)


def parse_json_file(input_file, output_file_path):
    '''

    :param input_file: Input file to be parsed
    :param output_file_path: Path where the parsed output file will be written to
    :return: None
    '''

    with open(input_file, 'r') as input_file_descriptor:
        json_data = input_file_descriptor.read()
    json_data = json_data.replace("'", '"')

    df = pd.DataFrame()
    for each_json in json_data.split('\n'):
        each_json_dict = json.loads(each_json)
        temp_df = pd.DataFrame([each_json_dict.values()], columns=each_json_dict.keys())
        df = pd.concat([df, temp_df])

    df = df.explode('product')
    df = pd.concat([df, df['product'].apply(pd.Series)], axis=1)
    df = df.drop(columns='product')
    output_file_basename = '{}_parsed.txt'.format(os.path.basename(input_file).split('.')[0])
    output_file = os.path.join(output_file_path, output_file_basename)
    df.to_csv(output_file, sep='\t', index=False)


def parse_xml_file(input_file, output_file_path):
    '''

    :param input_file: Input file to be parsed
    :param output_file_path: Path where the parsed output file will be written to
    :return: None
    '''

    root_node = et.parse(input_file).getroot()
    elements_list = []
    for item in root_node:
        temp_d = {}
        for element in item:
            temp_d[element.tag] = element.text
        elements_list.append(temp_d)

    df = pd.DataFrame(elements_list, columns=elements_list[0].keys())
    output_file_basename = '{}_parsed.txt'.format(os.path.basename(input_file).split('.')[0])
    output_file = os.path.join(output_file_path, output_file_basename)
    df.to_csv(output_file, sep='\t', index=False)


if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file_path = sys.argv[2]
    file_format = sys.argv[3]

    delimiter = ''
    if file_format == 'txt':
        delimiter = sys.argv[4]

    if file_format == 'txt':
        parse_txt_file(input_file, delimiter, output_file_path)
    if file_format == 'json':
        parse_json_file(input_file, output_file_path)
    if file_format == 'xml':
        parse_xml_file(input_file, output_file_path)
