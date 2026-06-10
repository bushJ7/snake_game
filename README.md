# 🐍 Classic Snake Game

A retro, arcade-style Snake Game built entirely in Python using Object-Oriented Programming (OOP) principles and the built-in `turtle` graphics library. 

This project was built as part of the *100 Days of Code: The Complete Python Pro Bootcamp* challenge to master game logic, coordinate systems, and event listening.

## 🎮 How to Play

The objective is simple: eat as much food as possible to grow your snake without crashing into the walls or your own tail!

* **Arrow Up (▲):** Move Up
* **Arrow Down (▼):** Move Down
* **Arrow Left (◀):** Move Left
* **Arrow Right (▶):** Move Right

---

## ✨ Features

* **Real-time Score Tracking:** Keeps track of your current score as you eat food.
* **High Score Persistence:** *(Optional feature if you built it: Saves your all-time high score to a local `data.txt` file so it persists even after closing the game).*
* **Collision Detection:** Smart detection for wall crashes and self-cannibalism (biting your own tail).
* **Responsive Controls:** Uses keyboard event listeners for smooth, real-time direction changes.

---

## 🧠 Core Programming Concepts Learned

Building this game required moving away from simple scripts and implementing structural software architecture:

1. **Object-Oriented Programming (OOP):** The project is split into clean, modular classes to manage different game components:
   * `snake.py`: Handles the creation, movement, and growth mechanics of the snake segments.
   * `food.py`: Inherits from the Turtle class to randomly spawn food on the screen whenever it gets eaten.
   * `scoreboard.py`: Manages writing the score, updating the display, and triggering the "Game Over" sequence.
2. **The Game Loop & Screen Updates:** Used `screen.tracer(0)` and `screen.update()` to refresh the screen manually, preventing the snake segments from lagging or separating during movement.
3. **Coordinate Geometry:** Applied mathematical distance formulas to detect when the snake's head was close enough to collide with food or its own tail body segments.

---

## 🛠️ Requirements & Installation

### Prerequisites
* Python 3.x installed on your machine.
* The `turtle` module (built-in standard library with Python, no extra installation required!).
