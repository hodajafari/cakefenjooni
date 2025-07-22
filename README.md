# 🍰 CakeFenjooni

A simple Django-based web application for listing and managing cakes.  
This project was created as a portfolio/demo app to practice Django and GitHub workflows.

---

## 📌 Features

- Display a list of cakes (name, description, price, availability)
- Add new cakes via a form
- Static pages: About Us, Contact Us
- Basic styling with HTML & CSS

---

## ⚙️ Technologies Used

- Python 3.13
- Django 4.x
- HTML5
- CSS3
- Git & GitHub

---

## 🚀 Run Locally

```bash
# Clone the project
git clone https://github.com/hodajafari/CakeFenjooni.git
cd CakeFenjooni

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
