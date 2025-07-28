# 🧮 Mathematical Game

![Python](https://img.shields.io/badge/language-Python-blue.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)
![Learning](https://img.shields.io/badge/learning-Project%20Based-blueviolet.svg)

## 📌 Description
**Mathematical Game** is a beginner-friendly command-line game built with Python to test users on basic arithmetic operations. It was developed as part of a learning journey to solidify core programming concepts like loops, functions, conditionals, user input handling, and global variables.

---

## 🎮 Features
- Four core math operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication
  - ➗ Division
- 5-Lives system for each game session
- 2 Points awarded for each correct answer
- Random question generation for endless practice
- Simple feedback messages to guide players

---

## 🧱 Code Structure
- `num1_generator()` / `num2_generator()`: Generate random numbers between 0 and 100.
- `addition()`, `subtraction()`, `multiplication()`, `division()`: Each function handles one operation, manages lives and score.
- `game_menu()`: Displays options and handles navigation to game modes.
- Global logic handles:
  - Input validation (partially)
  - Game over conditions
  - Score display and encouragement

---

## ▶️ How to Play
1. Run the script using Python 3.
2. Enter your name when prompted.
3. Choose an operation:
   - 1 for Addition
   - 2 for Subtraction
   - 3 for Multiplication
   - 4 for Division
4. Answer the problems displayed.
5. Earn 2 points per correct answer.
6. Lose a life per incorrect answer.
7. Game ends when you run out of lives or exit manually.

---

## 🛠️ How to Run Locally
```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/mathematical-game.git

# Step 2: Navigate into the folder
cd mathematical-game

# Step 3: Run the game
python mathematical_game.py
```
✅ Make sure Python 3 is installed: `python --version`

---

## ⚠️ Known Limitations & Pitfalls
Despite its functionality, the game currently has several limitations:
- ❌ No input validation: Entering letters or special characters will crash the game with a ValueError.
- ❌ Redundant logic: The same scoring and life mechanics are repeated in each operation function.
- ❌ No centralized score tracking: Each game mode has its own session score, and there's no cumulative or persistent high score.
- ❌ Lack of difficulty levels: All questions are based on random numbers from 0–100, which may be too hard or easy.
- ❌ Menu loops indefinitely without exit option: There's no clear way to quit the game unless the user forcefully exits the program.
- ❌ Error-prone input handling: Especially in division mode, `float(input()).strip()` used improperly can throw errors.

---

## 🚀 Future Improvements
As the developer progresses in Python knowledge, the following enhancements are planned:
- 🧠 Add Difficulty Levels (Easy, Medium, Hard)
- 🏆 High Score System with persistent storage using files
- ⏱️ Timer for each question to increase challenge
- 🧼 Input validation using try...except blocks
- 🎨 Better UI formatting using colors or even GUI (Tkinter or Pygame)
- 🔁 Centralized game loop with exit/continue options
- 📊 Cumulative scoring across sessions
- ✍️ Question explanation or hint system

---

## 📈 Learning Highlights
| Concept | Applied In |
|---------|------------|
| While loops | Game logic and input validation |
| Functions | Modular structure per operation |
| Conditionals | Correct answer checking |
| Random module | Arithmetic problem generation |
| Global variables | Score and lives tracking |
| Input handling | Basic user interaction |

---

## 🙋 Contributing
Contributions are welcome to enhance this learning project! Here's how:
1. Fork the repository
2. Clone it to your machine:
   ```bash
   git clone https://github.com/your-username/mathematical-game.git
   ```
3. Create a branch:
   ```bash
   git checkout -b feature-improve-division
   ```
4. Make your changes and commit:
   ```bash
   git commit -m "Improved division error handling"
   ```
5. Push to your GitHub:
   ```bash
   git push origin feature-improve-division
   ```
6. Submit a Pull Request

---

## 🙌 Acknowledgments
Thanks to the Python documentation and the coding community for helping shape this journey one loop at a time.

---

## 🧠 Motivation
"Struggle now, so I can succeed later."
This project was built with learning in mind. Mistakes are part of the journey!
