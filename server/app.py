from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from supabase import create_client, Client
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/get', methods=['GET'])
def get():
    response = supabase.table('Flask Test').select('*').execute()
    return jsonify(response.data)

if __name__ == '__main__':
    app.run(debug=True)