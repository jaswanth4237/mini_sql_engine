# Mini SQL Query Engine (Python)

## 📌 Project Overview

This project is a **simplified, in-memory SQL query engine** built from scratch using **Python**. It demonstrates how a database internally processes SQL queries by manually implementing parsing, filtering, projection, and aggregation logic.

The engine loads data from a **CSV file**, accepts **SQL-like queries via a command-line interface (CLI)**, executes them in memory, and displays results in a readable tabular format.

This project is designed for **learning purposes**, especially for understanding:

* How SQL queries work internally
* How data is filtered, selected, and aggregated
* Basic parser and execution engine design

---

## 🎯 Features Implemented

✔ Load CSV data into memory (list of dictionaries)

✔ Interactive CLI (REPL) for executing queries

✔ `SELECT *` and column-based projection

✔ `WHERE` clause with single condition

✔ Supported operators: `=`, `!=`, `>`, `<`, `>=`, `<=`

✔ String and numeric comparisons

✔ Aggregation using `COUNT(*)` and `COUNT(column)`

✔ Table-style output with headers

✔ Clear error handling for invalid queries

---

## 📂 Project Structure

```
mini-sql-engine/
│
├── data.csv        # Input CSV file (acts as a table)
├── main.py         # CLI entry point (REPL)
├── parser.py       # SQL query parser
├── engine.py       # Query execution logic
└── README.md       # Project documentation
```

---

## 🧠 Data Representation

* The CSV file is loaded using Python's `csv.DictReader`
* Each row is stored as a **dictionary**
* The table is represented as a **list of dictionaries**

Example:

```python
[
  {"id": "1", "name": "John", "age": "25", "country": "USA"},
  {"id": "2", "name": "Anna", "age": "35", "country": "India"}
]
```

---

## 🧾 Supported SQL Grammar

The engine supports a **subset of SQL**, defined below:

### ✅ SELECT

```sql
SELECT * FROM data;
SELECT name, age FROM data;
```

### ✅ WHERE (Single Condition)

```sql
SELECT name FROM data WHERE age > 30;
SELECT name FROM data WHERE country = 'India';
SELECT name FROM data WHERE country != 'USA';
```

### ✅ COUNT

```sql
SELECT COUNT(*) FROM data;
SELECT COUNT(age) FROM data;
SELECT COUNT(*) FROM data WHERE country = 'India';
```

### ❌ Not Supported

* JOINs
* Multiple tables
* Multiple WHERE conditions (AND / OR)
* UPDATE / DELETE / INSERT

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites

* Python 3.x installed

### 2️⃣ Run the CLI

```bash
python main.py
```

### 3️⃣ Example Commands

```sql
SELECT * FROM data
SELECT name,age FROM data WHERE age >= 30
SELECT COUNT(*) FROM data
exit
```

---

## ⚠️ Error Handling

The engine provides user-friendly error messages for:

* Invalid SQL syntax
* Unsupported queries
* Non-existent tables or columns
* Missing clauses (e.g., FROM)

Example:

```text
Error: Table 'daya' does not exist
Error: Only SELECT queries are supported
Error: Missing FROM clause
```

---

## 🏁 Expected Outcomes (Satisfied)

✔ Functional CLI SQL engine

✔ Correct data projection (`*` and specific columns)

✔ Accurate filtering using WHERE

✔ Correct aggregation using COUNT

✔ Clear error messages

✔ Well-documented code and grammar specification

---

## 📌 Conclusion

This project successfully demonstrates the **core principles behind SQL query execution** using simple Python constructs. It is ideal for beginners learning databases, backend development, or data engineering fundamentals.

---

## 👤 Author

**Jaswanth**

Mini SQL Engine Project
