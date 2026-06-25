# 📦 Asset Management Dashboard

## 👋 About This Project

Hello! I'm **Akshat Gaur**, and this project was built as a hands-on learning experience to improve my skills in:

- Python
- Flask
- PostgreSQL
- HTML & CSS, JS
- Docker
- Git & GitHub

The main idea behind this project is to build an **Asset Management Dashboard** where users can securely register, log in, and manage asset-related information through a clean and simple web interface.

This project helped me understand how frontend and backend interact, how authentication works, and how data is stored and managed in a database.

---

## 🚀 Features

- ✅ User Registration (Signup)
- ✅ User Login Authentication
- ✅ Session Management
- ✅ Dashboard Interface
- ✅ Add Asset Functionality
- ✅ MySQL Database Integration
- ✅ Form Validation
- ✅ Responsive UI Design
- ✅ Git & GitHub Version Control
- ✅ Docker Support

---

## 🛠️ Technologies Used

### 🔹 Backend
- Python
- Flask Framework

Flask is used because it is lightweight, simple, and perfect for learning backend development.

---

### 🔹 Database
- PostgreSQL
- psycopg2--binary

Used to store and manage user and asset data efficiently.

---

### 🔹 Frontend
- HTML5
- CSS3

Pages:
- `signup.html` → User registration
- `login.html` → User login
- `dashboard.html` → Main dashboard
- `add_asset.html` → Add asset page

---

### 🔹 Styling
- Custom CSS

Files:
- `Login.css`
- `signup.css`

Used to improve UI/UX and make the application clean and user-friendly.

---

### 🔹 DevOps / Deployment
- Docker
- Docker Compose

Used to containerize the application so it can run anywhere without setup issues.

---

### 🔹 Version Control
- Git
- GitHub

Used for tracking changes and storing project online.

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── log.txt
│
├── static/
│   ├── Login.css
│   └── signup.css
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── add_asset.html
│
└── .gitignore
```

---

## ⚙️ How It Works

### 1️⃣ User Registration

* User signs up using the signup page
* Data is validated and stored in PostgreSQL database

---

### 2️⃣ User Login

* User logs in with credentials
* Flask verifies details and creates a session

---

### 3️⃣ Dashboard Access

* After login, user is redirected to dashboard
* Displays all asset data from database

---

### 4️⃣ Asset Management

* Users can add and manage assets
* Data is stored and retrieved from PostgreSQL

---

🐳 Docker Setup

▶️ Run the Project

docker-compose up --build

🌐 Open in Browser

http://localhost:5001

🗄️ Database Setup (First Time Only)
docker exec -it postgres_db psql -U postgres -d login_db

Create tables:
CREATE TABLE user_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    user_id VARCHAR(100) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    asset_name VARCHAR(100),
    category VARCHAR(100),
    status VARCHAR(50),
    assigned_to VARCHAR(100),
    asset_value VARCHAR(50)
);


📊 View Data
docker exec -it postgres_db psql -U postgres -d login_db

SELECT * FROM user_details;
SELECT * FROM assets;


## 🎯 What I Learned

Through this project, I learned:

* Flask backend development
* MySQL database integration
* Authentication & session management
* Frontend + backend communication
* Docker containerization
* Debugging real-world errors
* Git & GitHub workflow

---

## 🔮 Future Improvements

* Password encryption (very important upgrade)
* Asset search & filters
* Update asset feature
* Role-based access control
* Cloud deployment (Render / AWS)
* REST API conversion

---
## 💡 Personal Note

This project represents my journey of learning full-stack development. While building it, I faced multiple challenges involving database connections, authentication, project structure, and GitHub integration. Solving those issues helped me gain practical development experience and improve my problem-solving skills.

Every bug fixed during this project taught me something new, and this repository reflects my continuous learning process as a developer. 🚀

---

## 👨‍💻 Developer

**Akshat Gaur**

---

# 🚀 Asset Management Dashboard

A simple **Asset Management Dashboard** built using:

- Python
- Flask
- MySQL
- HTML
- CSS

This project allows users to register, log in, and manage assets through a clean web interface.

---

## ✨ Features

- 🔐 User Signup & Login
- 📊 Dashboard for managing assets
- 🗄️ MySQL Database Integration
- 🎨 Clean and Responsive UI
- ⚡ Fast and Easy to Use

---

## 🛠️ Technologies Used

- 🐍 Python
- 🌶️ Flask
- 🗄️ MySQL
- 🌐 HTML
- 🎨 CSS
- 🅱️ Bootstrap

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd your-repo-name

2️⃣ Install Required Packages
pip install flask mysql-connector-python


3️⃣ Setup Database
* Run SQL commands in PostgreSQL (psql or pgAdmin)
* Run the SQL file to create tables

4️⃣ Configure Database
Open app.py and update:

password = "YOUR_PASSWORD"

5️⃣ Run the Project
python app.py


6️⃣ Open in Browser
http://127.0.0.1:5001




📸 Screenshots

* Login Page
* Signup Page
* Dashboard
* Asset Management Page

(Check Screenshots folder)


⚠️ Note: This project uses Dockerized PostgreSQL. No local DB setup required if using Docker Compose.