# Data Engineering Track: Pokemon Data Base

## Contents
0) Overview
1) Application Instructions
2) Files to Reference
3) Entity Relationship Diagram
4) Application Flowchart 
5) Ethical Considerations
6) Data Source Reference(s)


## Overview
This repository contains the files for **pokeDatabase**, a python application created using **data engineering** that utilizes the [*pypokedex*](https://pypi.org/project/pypokedex/1.0.0/)  library and pulls data from [*PokeAPI*](https://pokeapi.co/) to load into a SQL database. This database was utilized to create a python application that allows users to interact with the data containing the following information: 

**Pokemon**
- Abilities
- Typing(s)
- Base Stats
- Evolution Chain (if applicable)
- Moveset
- Game(s) the Pokemon can be found in

**Pokemon Moves**
- Base Stats
- Move Effect
- Move Power
- Move PP
- Move Type
- Damage Class

*Pokemon, games, moves, abilities are all assigned to their own individual ID.*


## Application Instructions (Including data engineering steps)
1. Create database in pgAdmin
   
2. Import code from ```pokemon_db_query``` to use to create tables. <br />
   *Please refer to instructions beginning at ```Line 100``` on how to import csv files to pgAdmin. You may also refer to file paths listed beginning on ```Line 100``` if problems arise and csv files must be uploaded individually.*

3. Ensure database URL is updated with correct information. <br />
    ```postgresql://<username>:<password>@<host>:<port>/<database_name>```
   
4. Open app.py with console once database has been created and populated.
   
5. Interact with prompt.   


## Files to Reference
This project focuses on the **Data Engineering Track**, where files within the repository contribute to the overall ETL process of the project, as outlined in project requirements.

- ```app.py```: pokeDatabase application, where user will interact with console to extract data from SQL database. 

- The ```application``` folder contains the data selected and pulled from PokéAPI. Every csv file corresponds to a table indicated in the ERD.
    - *Data extraction and transforming was split between group members; files within each group member's folder correspond to the data that was extracted from the member.*
      
- ```poke_erd.png```: Entity Relationship Diagram
  
- ```poke_schemata.sql```: SQL schematic used to create ERD
  
- ```pokemon_db_query.sql```: Queries used in SQL to create new database from previously generated csv files
  
- ```poke_flowchart.png```: Flowchart visualization to display routes of user and console interaction within the python application

- ```pokeDatabase_ppt.pdf```: Presentation displaying project at high level

      
## Entity Relationship Diagram
To visualize the information and the relational mapping between tables in this database, the ERD can be referenced below:

![poke_erd](https://github.com/user-attachments/assets/c3d3bcb5-808a-4a84-85d5-dae28235177f)


## Application Flowchart
To visualize the input and output flow for application interaction between user and console, the flow chart can be referenced below: 

![poke_flowchart](https://github.com/user-attachments/assets/7b9892ed-48cd-4765-a588-2b96a889d412)


## Ethical Considerations
As our project derives all data from [*PokéAPI*](https://pokeapi.co/), API documentation and guidelines were closely reviewed prior to ETL processes to honor ethical considerations for data extraction. Documentation and data use policies for APIs are important to review prior to making API calls, as there may be certain regulations for certain APIs, such as rate limiting. 

According to the documentation [*Fair Use Policy*](https://pokeapi.co/docs/graphql) of PokéAPI, as the site states that “PokéAPI is free and open to use,” this API was then used to develop the pokeDatabase python application. While the documentation did not specify an API call rate limit, the Fair Use policy additionally states developers of the API do not “tolerate denial of service attacks”. Rate limiting is set in place by many websites and networks in order to prevent denial of service (DOS) attacks. As PokéAPI did not specify a rate limit, the pokeDatabase application was made with the ethical consideration in mind that if the rate of calls exceeds a certain amount per limit, it may interfere with the usability and functionality of the database. 


## Data Source References
- PokéAPI (https://pokeapi.co/)
- Pypokedex Library (https://pypi.org/project/pypokedex/1.0.0/)


