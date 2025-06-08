# 📝 Flask Guestbook App

A beginner-friendly Flask project that demonstrates:

- Multi-page routing
- Template inheritance with Jinja2
- Form handling (GET & POST)
- Basic CSS styling
- In-memory data storage

This is Part 3 of a tutorial series on building web apps with Flask.

---

## 🚀 Demo

- 🏠 **Home Page** – A welcome message
- 📖 **Guestbook Page** – Users can leave their name and a message
- 🎨 **Styled UI** – Uses `static/style.css` for basic formatting
- 🔄 **Reset Route** – Clears all guestbook entries for testing

---

## 📁 Project Structure
<pre><code>flask-guestbook/
├── app.py # Main Flask application
├── static/ # Static files (CSS, JS, images)
│     └── style.css # Styling for form and layout
└── templates/ # Jinja2 HTML templates
│     └──  base.html # Shared base template
│     └── home.html # Home page content
│     └── guestbook.html # Guestbook form and entries </code></pre>
---

## 💡 How It Works

- Routes:
  - `/` – Home
  - `/guestbook` – View and submit entries
  - `/reset` – (Bonus) Clears all messages

- Templates:
  - `base.html` provides the layout
  - Other pages extend `base.html` using `{% extends %}`

- Styling:
  - Basic form and navigation styling in `style.css`

---

## 🛠️ Getting Started

### 1. Install Dependencies

```bash
pip install Flask
```

### 2. Run the App
```bash
python app.py
```

### 3. Open in Browser
```bash
Go to http://127.0.0.1:5000
```

## 📦 Features
✅ Clean template structure

✅ Dynamic routing with url_for

✅ Form validation with required fields

✅ Auto-redirect on submission to prevent resubmission

✅ Reset functionality for demo/testing

## 📚 Next Steps
Connect to SQLite or another database

Add user sessions and flash messages

Deploy to Heroku or Render

## 📄 License
MIT – Free to use, modify, and distribute.

## 🙋‍♀️ Author
Made with ❤️ by Ajita Gupta
<br>
Follow the tutorial series on Medium
