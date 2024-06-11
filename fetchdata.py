import sqlite3

def fetch_feedback_data(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    
    try:
        # Execute the query to fetch data from the Feedback table
        curr.execute("SELECT * FROM Feedback")
        
        # Fetch all rows from the executed query
        rows = curr.fetchall()
        
        # Print the table data
        print("Table Data:")
        for row in rows:
            print(row)
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the cursor and connection
        curr.close()
        conn.close()

# Path to your Cases.db file
db_path = 'Cases.db'

# Fetch and display data from the Feedback table
fetch_feedback_data(db_path)

