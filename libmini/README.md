# libmini: Week 1 OOP Project

# Week 1 — OOP Fundamentals — Salome
[GitHub Repository](https://github.com/Sallie25/de-week1-oop-salome)

This project is a beginner-friendly exercise for practising **Object-Oriented Programming (OOP)** concepts in Python.  
It models a simple **Library System** with classes such as `Person`, `Member`, `Librarian`, `Book`, and `Library`.

---

## Learning Goals

- Define and demonstrate key OOP concepts:
  - **Class**
  - **Object / Instance**
  - **Encapsulation**
  - **Inheritance**
  - **Polymorphism**
- Apply **composition** (“has-a” relationships) in a simple model.
- Implement one **design pattern (Factory)** — *to be done next*.
- Present a short **CLI demo** — *to be done later*.

---

## 🧱 OOP Concepts Explained Simply

| Concept | Explanation | Example in this project |
|----------|--------------|--------------------------|
| **Class** | A blueprint that defines the structure and behavior of objects. | `Person`, `Book`, `Library` are all classes. |
| **Object / Instance** | A real example created from a class. | `book1 = Book("1984", "George Orwell")` |
| **Encapsulation** | Hiding internal data and exposing only what’s needed. | `Library` keeps `_catalog` and `_loans` private. |
| **Inheritance** | Allows a child class to reuse or extend a parent class. | `Member` and `Librarian` inherit from `Person`. |
| **Polymorphism** | Different classes respond to the same method name differently. | Will be shown later with `NotifierFactory`. |

---

##  Classes Implemented

- [1] `Person` — Base class with basic attributes.  
- [2] `Member` — Inherits from `Person`, represents a library member.  
- [3] `Librarian` — Inherits from `Person`, manages library functions.  
- [4] `Book` — Represents a single book (title, author, ISBN, availability).  
- [5] `Library` — Uses composition to manage books and members.  

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Sallie25/de-week1-oop-salome.git
cd de-week1-oop-salome

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate   # Git Bash on Windows
# or
.venv\Scripts\activate          # Command Prompt

# 3. (No CLI demo yet)
# For now, open libmini/models.py to view your class definitions.

