from connector import set_connection

with open('queries/create_views.sql', 'r') as f:
    with set_connection() as dc:
        dc.execute(f.read())
