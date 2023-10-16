# Prject-91
This is a simple module written to process a small file by two ways
- Native Python
- Database

and produce output in a pre-defined format.

This project uses internal in-memory DB, but the pattern can be repeated for other paid for enterprise db's.

###Run the code
- Python Mode- python run_project_91.py -m Python -f <Path to your file>
e.g.
```
INFO:__main__:Parsing arguments
INFO:__main__:Trying to run the program
INFO:__main__:Running in the mode: Python
INFO:top_scorer_py.top_scorer:Processing the file in python
Sipho Lolo
George Of The Jungle
Score: 78
```

- Database Mode: python run_project_91.py -m Database -f <Path to your file>
e.g. 
```
INFO:__main__:Parsing arguments
INFO:__main__:Trying to run the program
INFO:__main__:Running in the mode: Database
INFO:top_scorer_db.top_scorer_db:Processing the file in DB
INFO:top_scorer_db.run_db_integ:Creating the tables if they do not exist.
Sipho Lolo
George Of The Jungle
Score: 78
```


####Work to be done
- Add test cases
- Fix logger for Database mode
- Add more error handling, DQ checks in DB mode
- Integrate with Snowflake