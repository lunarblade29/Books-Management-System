# 📚 Book Management System

## 📖 Overview
The **Book Management System** is a Flask-based web application that allows faculty members to submit book requests, which are stored in an Excel file. It also provides a functionality to download the stored book request data as an Excel file.

## 🚀 Features
- 📄 **User-Friendly Book Request Form**: Faculty can submit book requests via a web form.
- 📊 **Data Storage in Excel**: Requests are automatically saved in a local Excel file (`book_requests.xlsx`).
- 📥 **Download Book Requests**: Users can download the stored data with a single click.
- 🎨 **Attractive UI**: Designed with Bootstrap for a clean and modern look.
- 🔧 **Easy Deployment**: Can be hosted on PythonAnywhere for remote access.

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap, JavaScript (SweetAlert for alerts)
- **Database**: Excel (Pandas for handling data)

## 📂 Project Structure
```
Book-Management-System/
│-- static/
│   ├── script.js (Handles form submission alerts)
│-- templates/
│   ├── index.html (Main UI for book request form)
│-- app.py (Flask application logic)
│-- book_requests.xlsx (Data storage for book requests)
│-- requirements.txt (Required dependencies)
│-- README.md (Project documentation)
```

## 🎯 How to Run Locally
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Book-Management-System.git
cd Book-Management-System
```
### 2️⃣ Install Dependencies
Make sure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python app.py
```
The application will run at `http://127.0.0.1:5000/`.

## 🌐 Deploying on PythonAnywhere
1. Upload the project files to PythonAnywhere.
2. Set up a Flask web app on PythonAnywhere.
3. Configure the working directory and WSGI file.
4. Restart the web app, and share the live URL!

## 🖼️ Screenshots
| Book Request Form | Download Button |
|------------------|----------------|
| ![Form Screenshot](assets/form.png) | ![Download Screenshot](assets/download.png) |

## ✨ Future Enhancements
- 🔍 **Search and Filter Requests**
- 📧 **Automated Email Confirmation for Faculty**
- 📑 **Admin Panel for Managing Requests**

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to fork this repository and contribute! 🚀

## 📩 Contact
For any queries, reach out to **your.email@example.com**.

