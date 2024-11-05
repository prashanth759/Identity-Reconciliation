from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
DB_USER = 'ENTER YOUR MYSQL USERNAME'
# Here if any symbol in the password example: prashant@1234 there please enter prashanth%401234
DB_PASSWORD = 'ENTER YOUR MYSQL PASSWORD'# URL-encoded password
# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USER}:{DB_PASSWORD}@localhost/contacts_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(20))
    email = db.Column(db.String(100))
    linkedId = db.Column(db.Integer, db.ForeignKey('contact.id'))
    linkPrecedence = db.Column(db.Enum('primary', 'secondary'))
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deletedAt = db.Column(db.DateTime)

# Create all tables
with app.app_context():
    db.create_all()

# Define the /identify endpoint
@app.route('/identify', methods=['POST'])
def identify():
    data = request.get_json()
    email = data.get('email')
    phone_number = data.get('phoneNumber')

    # Check if the input is valid
    if not email and not phone_number:
        return jsonify({"error": "Email or phone number must be provided."}), 400

    # Search for existing contacts by email or phone number
    existing_contact = None
    if email:
        existing_contact = Contact.query.filter_by(email=email).first()
    if not existing_contact and phone_number:
        existing_contact = Contact.query.filter_by(phoneNumber=phone_number).first()

    if existing_contact:
        # If found, create a secondary contact entry
        secondary_contact = Contact(
            phoneNumber=phone_number,
            email=email,
            linkedId=existing_contact.id,
            linkPrecedence='secondary'
        )
        db.session.add(secondary_contact)
        db.session.commit()
        
        # Prepare the response
        response = {
            "primaryContactId": existing_contact.id,
            "emails": [existing_contact.email],
            "phoneNumbers": [existing_contact.phoneNumber],
            "secondaryContactIds": [secondary_contact.id]
        }
        return jsonify(response), 200
    else:
        # If no existing contact, create a new primary contact
        new_contact = Contact(
            phoneNumber=phone_number,
            email=email,
            linkPrecedence='primary'
        )
        db.session.add(new_contact)
        db.session.commit()

        # Prepare the response for a new contact
        response = {
            "primaryContactId": new_contact.id,
            "emails": [new_contact.email],
            "phoneNumbers": [new_contact.phoneNumber],
            "secondaryContactIds": []
        }
        return jsonify(response), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
