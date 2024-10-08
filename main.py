import os
import concurrent.futures

from flask import Flask, request, jsonify, Response

from src.database_connector.postgres_connector import PostgresConnector

app = Flask(__name__)

@app.route('/db_setup', methods=['POST'])
def db_setup_endpoint():
    data = request.json
    db_pass = data.get('db_pass')

    os.environ['DB_PASS'] = db_pass

    # Process the data as needed
    response = {
        'status': 'success',
        'data_received': os.environ['DB_PASS']
    }
    return jsonify(response), 200

@app.route('/add_sca_player_ids_to_existing_shots', methods=['POST'])
def db_setup_endpoint():
    data = request.json

    postgres_connector = PostgresConnector()
    postgres_connector.open_connection_cursor("premier_league_stats")

    # Process the data as needed
    response = {
        'status': 'success'
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)