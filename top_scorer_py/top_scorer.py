"""
A simple python module to sort data with format:
 f_name, l_name, marks
Output will be Print the highest marks and individuals
"""
import sys
import logging
logger = logging.getLogger(__name__)

def get_top_scorer(file_path: str, has_header: bool):
    logger.info("Processing the file in python")
    data={}
    with open(file_path) as f:
        for line in f:
            # Removing newline since we are doing string processing
            line = line.rstrip()
            # Checking for header and skipping it in case it exists
            if has_header:
                has_header = False
                continue
            # Checking if data is parsable
            if len(line.split(',')) == 3 and line.split(',')[2].isnumeric():
                (f_name, l_name, marks) = line.split(',')
            else:
                logger.error("Malformed line " + line + "\nExiting!!")
                sys.exit(1)
            if int(marks) in data:
                data[int(marks)] = data[int(marks)] + [[f_name, l_name]]
            else:
                data[int(marks)] = [[f_name, l_name]]
        sorted_data = {k: data[k] for k in sorted(data)}
        # Printing as required
        print('\n'.join(' '.join(map(str, l)) for l in sorted_data.get(list(sorted_data)[-1])) + 
              "\nScore: " + str(list(sorted_data)[-1]))