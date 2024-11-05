# Identity Reconciliation API

This project is an API designed for managing contact information and reconciling multiple identities to maintain user anonymity across multiple purchases. The service consolidates multiple contacts with different email addresses and phone numbers under a unified profile.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages (listed in `requirement.txt`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/prashanth759/Identity-Reconciliation.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd Identity-Reconciliation
    ```

3. **Set Up a Virtual Environment**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **On Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **On macOS and Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Install dependencies**:
    ```bash
    pip install -r requirement.txt
    ```

5. **Configure MySQL Credentials**:
   - Open `app.py`.
   - Enter your MySQL username and password by replacing the placeholders:
     ```python
     DB_USER = 'ENTER YOUR MYSQL USERNAME'
     DB_PASSWORD = 'ENTER YOUR MYSQL PASSWORD'
     ```

### Running the Application

1. **Start the application**:
   - In the command prompt or terminal, run:
     ```bash
     python app.py
     ```

2. **Testing the API**:
   - Open a separate terminal or Bash session to test the `/identify` endpoint:
     ```bash
     curl -X POST http://127.0.0.1:5000/identify -H "Content-Type: application/json" -d '{"email": "srisaiprashanthreddy@gmail.com", "phoneNumber": "9381735282"}'
     ```

## Author

- [N SRI SAI PRASHANTH REDDY](https://github.com/prashanth759)
