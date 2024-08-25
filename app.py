from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to extract numbers and alphabets
def extract_numbers_and_alphabets(data):
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_lowercase = [max([x for x in alphabets if x.islower()], default=None)]
    return numbers, alphabets, highest_lowercase if highest_lowercase[0] else []

# POST /bfhl - Process and return the desired JSON response
@app.route('/bfhl', methods=['POST'])
def process_bfhl():
    try:
        req_data = request.json
        full_name = req_data.get("full_name")
        dob = req_data.get("dob")
        email = req_data.get("email")
        roll_number = req_data.get("roll_number")
        data = req_data.get("data")

        if not (full_name and dob and email and roll_number and data):
            raise ValueError("Missing required fields")

        user_id = f"{full_name.lower().replace(' ', '_')}_{dob.replace('-', '')}"
        numbers, alphabets, highest_lowercase = extract_numbers_and_alphabets(data)

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 400

# GET /bfhl - Return a hardcoded operation_code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {"operation_code": 1}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
