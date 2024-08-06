from connector import set_connection
import pandas as pd

with open('queries/ddl.sql') as f:
    query=f.read()

with set_connection() as dc:
    dc.execute(query)
    tables = [
        'Country', 
        'Team', 
        'Player', 
        'League', 
        'Player_Attributes', 
        'Team_Attributes', 
        'Match'
    ]
    
    for table in tables:                
        df = pd.read_csv(f'source/{table}.csv')
        dc.query(f"""
            insert into {table}
            select *
            from df
        """)