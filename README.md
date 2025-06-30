# Stakeholder Outreach Project

## Overview
The Stakeholder Outreach Project is a web application designed to manage and engage with various stakeholders across different sectors. It provides functionalities for importing/exporting stakeholder data, viewing detailed stakeholder profiles, and editing stakeholder information.

## Features
- Import and export stakeholder data via CSV files
- View detailed stakeholder profiles
- Edit stakeholder information
- Manage stakeholder engagement status

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Abudi-seid10/Outreach-Directory.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stakeholder-outreach
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Access the application at `http://127.0.0.1:8000/`

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact Abudi at Abduseid28@gmail.com.
