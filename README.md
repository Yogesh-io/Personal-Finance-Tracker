# 💹 Personal Finance Tracker

A full-stack web application designed to help users log, manage, and analyze their daily financial transactions. Built with a focus on simplicity and data persistence.

## 🌟 Key Features

* **Transaction Management:** Create, Read, Update, and Delete (CRUD) your income and expenses.
* **Data Persistence:** Securely stores all financial data in a SQL database.
* **Categorization:** Tag transactions (e.g., Food, Rent, Salary) for better organization.
* **Dashboard:** A clean overview of your total balance and spending trends.
* **Responsive UI:** Styled with CSS to be user-friendly on both desktop and mobile.

---

## 🛠️ Tech Stack

* **Backend:** [Python](https://www.python.org/) & [Flask](https://flask.palletsprojects.com/)
* **Frontend:** HTML5 & CSS3 (Jinaj2 Templating)
* **Database:** SQL (SQLite or MySQL)

---

## 📁 Project Structure

```text
├── app.py              # Main application logic & routes
├── database.db         # SQL database file (if using SQLite)
├── static/
│   └── css/            # Custom stylesheets
│       └── style.css
├── index.html      # Dashboard / Transaction list

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python installed. You can check by running:

```bash
python --version

```

### 2. Installation

Clone this repository and navigate to the project folder:

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker

```

### 3. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

### 5. Run the App

```bash
flask run

```

The application will be available at: **`http://127.0.0.1:5000/`**

---

## 📊 Future Enhancements

* [ ] Add interactive charts using **Chart.js**.
* [ ] Implement **User Authentication** (Login/Sign-up).
* [ ] Monthly budget alerts and spending limits.
* [ ] Export data to CSV/Excel.

---
