import pymysql


# establish a connection to the local server
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Concludersi1912',
    db='portofolioprojects' #the name of database in mysql workbench
)

try:
    with connection.cursor() as cursor:
        # Retrieve all column names from the table
        cursor.execute("SHOW COLUMNS FROM Nashville_Housing;")
        columns_info = cursor.fetchall()  # get the info of all columns
        print("column:", columns_info)  
        
        columns = [row[0] for row in columns_info]  # extract the column names

        # Generate and execute an update query for each column
        for col in columns:
            sql = f"""
            UPDATE Nashville_Housing ##name of the table in mysql workbench 
            SET {col} = NULL
            WHERE {col} = '';
            """
            cursor.execute(sql)

    # Commit changes to the database
    connection.commit()

finally:
    # Close the connection
    connection.close()
