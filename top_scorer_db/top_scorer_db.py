"""
A simple python module to laod data to DB with format:
 f_name, l_name, marks
Output will be Print the highest marks and individuals
"""
from top_scorer_db.run_db_integ import *
import logging
logger = logging.getLogger(__name__)

# Within this module I will model a solution that can be used as is in any DB like Snowflake, DataBricks
def get_top_scorer_db(file_path: str, has_header: bool):
    logger.info("Processing the file in DB")
    
    # Performing ELT (In real world this would be done in orchestration tool like Airflow)
    create_tables() and load_to_stg(file_path, has_header) and load_to_main()
    
    # Performing Calculation
    project_91_calculation()
    
    
