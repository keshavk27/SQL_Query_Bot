# 🤖 SQL Query Bot

An AI-powered SQL chatbot that allows users to interact with SQL databases using natural language. Instead of writing SQL queries manually, users can ask questions in plain English, and the application generates, executes, and explains SQL queries automatically using a Large Language Model.

---

## 🚀 Features

- 💬 Chat with your SQL database using natural language
- 🧠 AI-generated SQL queries using Groq LLM
- 🗄️ Supports both:
  - SQLite databases
  - MySQL databases
- 📊 Displays query results in an easy-to-read format
- 🔄 Maintains conversation history
- ⚡ Fast response generation with Groq
- 🎨 Clean Streamlit interface
- 🛡️ Safe SQL execution through LangChain SQL Agent

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain
- LangChain Community
- SQLAlchemy

### Database
- SQLite
- MySQL

### LLM
- Groq API

---

## 📂 Project Structure

```
SQL_Query_Bot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── sqlite_database.db     # Sample SQLite database
├── README.md
└── ...
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/keshavk27/SQL_Query_Bot.git

cd SQL_Query_Bot
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## 💡 Example Queries

Some example questions you can ask:

```
Show all students.
```

```
List employees with salary greater than 50000.
```

```
What is the average marks of students?
```

```
Count the total number of records.
```

```
Show the top 5 highest-paid employees.
```

```
Which department has the maximum number of employees?
```

---

## 🧠 How It Works

1. User enters a question in natural language.
2. LangChain SQL Agent sends the prompt to the Groq LLM.
3. The LLM generates the appropriate SQL query.
4. The SQL query is executed on the selected database.
5. Results are returned and displayed in the Streamlit interface.



## 🔒 Supported Databases

- ✅ SQLite
- ✅ MySQL

---

## 📦 Dependencies

- streamlit
- langchain
- langchain-community
- langchain-groq
- sqlalchemy
- pymysql
- python-dotenv

---

## Future Improvements

- PostgreSQL support
- Microsoft SQL Server support
- Database schema visualization
- SQL query explanation
- Query history export
- Authentication
- Docker deployment
- Multi-user support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 👨‍💻 Author

**Keshav Kumar**

GitHub: https://github.com/keshavk27

---

## ⭐ If you found this project useful, consider giving it a star!