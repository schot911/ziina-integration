from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZIINA_API_URL = 'https://api.ziina.com/v1'  # Базовый URL API Ziina
ZIINA_API_KEY = 'your_ziina_api_key'  # Ваш API ключ Ziina

@app.route('/create-invoice', methods=['POST'])
def create_invoice():
    data = request.json
    email = data.get('email')
    amount = data.get('amount')
    description = data.get('description')

    if email and amount and description:
        invoice_response = create_ziina_invoice(email, amount, description)
        return jsonify(invoice_response), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400

def create_ziina_invoice(email, amount, description):
    url = f'{ZIINA_API_URL}/invoices'
    headers = {
        'Authorization': f'Bearer {ZIINA_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'email': email,
        'amount': amount,
        'currency': 'AED',  # Предполагаем, что валюта - AED
        'description': description
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(port=5000)
