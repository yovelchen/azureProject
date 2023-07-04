from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import Error

app = Flask(_name_)

@app.route('/data', methods=['POST'])
def process_data():
    try:
        data = request.json

        name = data.get('name')
        age_value = data.get('age_value')
        time = data.get('time')

        # Database connection details
        db_host = '10.0.2.4'  # Replace with your actual host
        db_port = '5432'  # Replace with your actual port
        db_name = 'flask_db'  # Replace with your actual database name
        db_user = 'postgres'  # Replace with your actual username
        db_password = 'Azureuser123'  # Replace with your actual password

        # Create a connection
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )

        # Create a cursor
        cur = conn.cursor()

        # Execute the INSERT statement
        insert_query = "INSERT INTO your_table (name, age_value, time) VALUES (%s, %s, %s)"
        cur.execute(insert_query, (name, age_value, time))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        response = {
            'status': 'success',
            'name': name,
            'age_value': age_value,
            'time': time,
            'database_status': 'Data inserted successfully'
        }
        return jsonify(response)

    except psycopg2.Error as e:
        response = {
            'status': 'error',
            'message': 'Database error',
            'error_details': str(e)
        }
        return jsonify(response), 500

if _name_ == '_main_':
    app.run(host='0.0.0.0', port="8080")