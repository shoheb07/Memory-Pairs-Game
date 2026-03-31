# Memory-Pairs-Game
A Memory Pairs Game (also called Concentration) is a simple Python game where players flip cards and try to find matching pairs.


A simple and fun Memory Matching Game built using Python. The goal is to flip cards and find all matching pairs in the least number of moves.



🎯 Features

- 🎲 Randomized board every time you play
- 🔄 Flip two cards per turn
- ✅ Matching logic with instant feedback
- 📊 Move counter to track performance
- 🧩 Easy-to-understand console interface



🛠️ Tech Stack

- Language: Python
- Libraries Used:
  - "random" (for shuffling cards)
  - "time" (for delay effect)



▶️ How to Run

1. Install Python (3.x recommended)
2. Save the file as:
   memory_game.py
3. Run the game:
   python memory_game.py



🎮 How to Play

1. The game board is a grid (default: 4×4).
2. Each number appears exactly twice.
3. Select two positions per turn:
   - Enter row and column (0-based index).
4. If the cards match:
   - They remain revealed ✅
5. If they don’t match:
   - They flip back ❌
6. Continue until all pairs are matched.



🧪 Example Board

 X  X  X  X
 X  X  X  X
 X  X  X  X
 X  X  X  X

---

📁 Project Structure

memory-pairs-game/
│── memory_game.py
│── README.md


⚙️ Customization

You can change the board size by modifying:

play_game(size=4)

Examples:

- "size=4" → Easy
- "size=6" → Medium
- "size=8" → Hard


🚀 Future Improvements

- 🖥️ GUI version (Tkinter / Pygame)
- ⏱️ Timer and leaderboard
- 👥 Multiplayer mode
- 🎨 Card themes (colors/images instead of numbers)
- 🔊 Sound effects


🤝 Contribution

Contributions are welcome!
Feel free to fork this repo and improve the game.


📜 License

This project is open-source and free to use.


👨‍💻 Author

Shoheb Mulla 
