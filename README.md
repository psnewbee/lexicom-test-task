# Build project
```docker compose build```

# Launch containers (in detach mode)
```docker compose up -d```

## [Swagger endpoint](http://localhost:8000/docs)


# Solutions for test case #2

## [Solution #1](SQL Query)
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name LIKE short_names.name || '.%';


## [Solution #1](SQL Query)
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE LEFT(full_names.name, POSITION('.' in full_names.name) - 1) = short_names.name

	 
## [Solution #2](python script)
##--------------------------------------------------------------------------##
import psycopg2

def update_fullname_table():
    conn = psycopg2.connect(
        database="db",
        user="user",
        password="password",
        host="postgres",
        port="5432"
    )

    cursor = conn.cursor()

    select_query_shortnames = '''
        SELECT name, status
        FROM short_names
        ORDER BY name ASC
    '''
    
    cursor.execute(select_query_shortnames)
    shortnames_rows = cursor.fetchall()

    select_query_fullnames = '''
        SELECT name, status
        FROM full_names
        ORDER BY name ASC
    '''

    cursor.execute(select_query_fullnames)
    fullnames_rows = cursor.fetchall()

    counter = 0
    full_name, _ = fullnames_rows[counter][0].split('.')
    
    for short_name, status in shortnames_rows:
        
        if short_name == full_name:
            fullnames_rows[counter] = (fullnames_rows[counter][0], status)
            
            if counter != len(fullnames_rows) - 1:
                counter += 1
                full_name, _ = fullnames_rows[counter][0].split('.')
    
    
    truncate_query = '''
        TRUNCATE TABLE full_names
    '''

    cursor.execute(truncate_query)

    insert_query_fullname_updated = '''
        INSERT INTO full_names (name, status)
        VALUES (%s, %s)
    '''

    cursor.executemany(insert_query_fullname_updated, fullnames_rows)
 
    conn.commit()
    cursor.close()
    conn.close()
##--------------------------------------------------------------------------##
