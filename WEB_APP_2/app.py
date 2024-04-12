from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb+srv://aasthapatel1510:aasthapatel1510@firstpro.rvzezkv.mongodb.net/?retryWrites=true&w=majority&appName=FirstPro")
db = client['Cloude']
collection = db['MNC']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    data = list(collection.find({}, {'_id': 0, 'end_of_period': 1, 'disbursed_amount': 1}))
    formatted_data = [{
        'label': item['end_of_period'].split('T')[0],  # Simplifying date format
        'value': float(item['disbursed_amount'])
    } for item in data]
    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
