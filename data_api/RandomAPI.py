from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

def generate_loan():
    return {
        "loan_id": fake.unique.random_number(digits=5),
        "borrower": {
            "id": fake.unique.random_number(digits=5),
            "name": fake.name(),
            "email": fake.email()
        },
        "loan_amount": round(random.uniform(100000, 1000000), 2),
        "interest_rate": round(random.uniform(2, 5), 2),
        "term": random.choice([15, 30]),
        "securitized": random.choice([True, False])
    }

@app.route('/api/loans', methods=['GET'])
def get_loans():
    loans = {"loans": [generate_loan() for _ in range(random.randint(1, 10))]}
    return jsonify(loans)

if __name__ == "__main__":
    app.run(debug=True)