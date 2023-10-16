"""
Creting the runner for different modes    
Mode-1
- Using Python:
    Params- File Name, Has Header
- Using Database:
    Params- File Name, Has Header
"""

import sys
import argparse
import logging
from top_scorer_py.top_scorer import get_top_scorer
from top_scorer_db.top_scorer_db import get_top_scorer_db
logging.basicConfig(level=logging.INFO)
logger= logging.getLogger(__name__)

def arg_parser():
    """
    Method to parse the input argumets
    :return Params for the Module
    """

    logger.info("Parsing arguments")
    parsed_args= argparse.ArgumentParser()
    parsed_args.add_argument("-m", "--mode", help= "What mode we want to run this program, Python or Database", required=True)
    parsed_args.add_argument("-f", "--file", help= "File input for processing", required=True)
    parsed_args.add_argument("--has_header", help= "Does file has a header", default= True, type=bool)  
    return parsed_args

def main():
    """_summary_
    """
    parser= arg_parser()
    args= parser.parse_args()
    logger.info("Trying to run the program")
    mode= args.mode
    if mode not in ['Python', 'Database']:
        logger.error("No valid mode provided")
        parser.print_help()
        sys.exit(1)    
    logger.info("Running in the mode: " + mode)
    if mode == 'Python': 
        get_top_scorer(args.file, args.has_header)
    else:
        get_top_scorer_db(args.file, args.has_header)


if __name__ == "__main__":
    main()
    
