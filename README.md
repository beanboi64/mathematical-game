```
████████╗██╗  ██╗███████╗     ██╗   ██╗ █████╗ ██╗     ██╗     ███████╗██╗   ██╗
╚══██╔══╝██║  ██║██╔════╝     ██║   ██║██╔══██╗██║     ██║     ██╔════╝╚██╗ ██╔╝
   ██║   ███████║█████╗       ██║   ██║███████║██║     ██║     █████╗   ╚████╔╝ 
   ██║   ██╔══██║██╔══╝       ╚██╗ ██╔╝██╔══██║██║     ██║     ██╔══╝    ╚██╔╝  
   ██║   ██║  ██║███████╗      ╚████╔╝ ██║  ██║███████╗███████╗███████╗   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝       ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   
```

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
python mathgame.py
```
✅ Make sure Python 3 is installed: `python --version`

---

## 💻 Example Usage
 ```bash
***Mathematical Game***

Please enter your name: Jordan

1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice: 1

83 + 24 = 
Enter your answer: 107
Lives: 5 Score: 2
Correct! Here's 2 points!

56 + 19 = 
Enter your answer: 75
Lives: 5 Score: 4
Correct! Here's 2 points!

99 + 2 = 
Enter your answer: 105
Lives: 4 Score: 4
Wrong! The correct answer was 101

33 + 60 = 
Enter your answer: 93
Lives: 4 Score: 6
Correct! Here's 2 points!

10 + 48 = 
Enter your answer: 60
Lives: 3 Score: 6
Wrong! The correct answer was 58

15 + 81 = 
Enter your answer: 96
Lives: 3 Score: 8
Correct! Here's 2 points!

9 + 18 = 
Enter your answer: 20
Lives: 2 Score: 8
Wrong! The correct answer was 27

11 + 27 = 
Enter your answer: 38
Lives: 2 Score: 10
Correct! Here's 2 points!

20 + 34 = 
Enter your answer: 54
Lives: 1 Score: 10
Wrong! The correct answer was 54

14 + 12 = 
Enter your answer: 26
Lives: 1 Score: 12
Correct! Here's 2 points!

81 + 8 = 
Enter your answer: 91
Lives: 1 Score: 14
Correct! Here's 2 points!

35 + 49 = 
Enter your answer: 90
Lives: 0 Score: 14
Wrong! The correct answer was 84
Whoops you're out of lives!
Congrats Jordan! You scored 14 points

1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice: 
```
---

## 🧠 Learning Note

This project is part of my ongoing Python learning journey. It highlights my ability to build an interactive, logic-driven application from scratch using core programming fundamentals. Through this game, I’ve practiced and deepened my understanding of:

- 📥 **User Input**: Capturing and validating player names and numeric answers
- 🔁 **While Loops**: Controlling the game flow and repetition based on conditions
- 🧠 **Conditional Logic**: Handling correct/incorrect answers and branching outcomes
- 🧮 **Functions**: Creating reusable logic blocks for each math operation and input generation
- 📦 **Random Module**: Generating dynamic math problems with varying difficulty
- 🧱 **Basic Structuring**: Designing a clear menu and modular program layout
- ⚠️ **Error Awareness**: Identifying crashes from invalid input and logic placement

This game marks a major milestone in transitioning from syntax familiarity to logic-building and full-feature design.

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

## License

This project is licensed under the [MIT LICENSE](LICENSE) . Feel free to use, modify, and distribute BeanoGuard as needed.

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Email**: billywaynejr007@gmail.com
- **GitHub**: [beanboi64](https://github.com/beanboi64)
- **Instagram**: [krissattack0](https://www.instagram.com/krissattack0)
- **X**: [krissattacko](https://x.com/krissattack0)

---

## 🙌 Acknowledgments
Thanks to the Python documentation and the coding community for helping shape this journey one loop at a time.

---

## 🧠 Motivation
"Struggle now, so I can succeed later."
This project was built with learning in mind. Mistakes are part of the journey!
