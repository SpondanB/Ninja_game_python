# 🥷 Ninja Game – Python & Pygame

A 2D action-platformer built using **Python** and the **Pygame** library. This project was created as a hands-on way to learn game development fundamentals while building a complete, interactive game with a custom level editor.

---

## 📌 Project Overview
**Ninja Game** is a small but fully functional game project that demonstrates how to:
- Use the `pygame` framework effectively
- Structure a game project cleanly
- Implement a level editor and external map loading
- Manage assets, scripts, and game logic modularly

The project emphasizes **learning-by-building**, making it ideal for beginners transitioning into intermediate game development with Python.

---

## 🎮 Features
- Real-time 2D gameplay using Pygame
- Custom **level editor** for creating maps visually
- JSON-based map storage and loading
- Organized asset and script management
- Modular code structure for scalability

---

## 📁 Project Structure
```text
Ninja_game_python/
│
├── game.py            # Main game file (playable game)
├── editor.py          # Level editor for designing maps
├── map.json           # Sample map created using the editor for testing
│
├── data/              # Game assets (sprites, sounds, tiles, maps, etc.)
│
├── scripts/           # Core game logic and helper modules
│   ├── clouds.py
│   ├── particle.py
│   ├── entities.py
│   ├── spark.py
│   ├── tilemap.py
│   └── utils.py
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Pygame

Install Pygame:
```bash
pip install pygame
```

---

## ▶️ Running the Game
To start the game:
```bash
python game.py
```

---

## 🛠️ Using the Level Editor
To launch the level editor:
```bash
python editor.py
```

- Design levels visually
- Save maps as `.json` files
- Load the generated maps directly into the main game

This workflow separates **content creation** from **game logic**, mirroring real-world game development practices.

---

## 🧠 Learning Objectives
This project helped reinforce the following concepts:

- Game loops and frame-based updates
- Event handling and user input
- Collision detection and movement systems
- External data-driven level design
- Code modularization and maintainability

---

## 📈 Skills Demonstrated
- Python programming
- Pygame-based rendering and input handling
- Basic game architecture design
- JSON data handling
- Tooling (custom editor development)

---

## 🏷️ Portfolio Note
This project was intentionally designed as a **learning-focused game**, showcasing foundational skills in:
- 2D game development
- Engine-like tooling (level editor)
- Clean project organization

It is well-suited for inclusion in:
- Game development portfolios
- Python project showcases
- Academic or self-learning repositories

---

## 📄 Future Improvements
- Improve physics and collision handling
- Add sound effects and background music

---

**Author:** Spondan Bandyopadhyay

---
