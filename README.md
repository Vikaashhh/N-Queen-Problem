# ♟️ Day 77 — GFG 160 Days DSA Challenge
### 👑 Problem: N-Queen Problem (Backtracking)
### 📌 Problem Statement:
Place n queens on an n x n chessboard such that no two queens threaten each other—meaning no two can share the same row, column, or diagonal.

## 🧠 Approach:
✅ Utilized a classic Backtracking Algorithm.
✅ Maintained three key sets:

rows → To track occupied rows

diagonals (r - c) → For main diagonals

anti_diagonals (r + c) → For anti-diagonals

✅ When a valid spot is found, place the queen and recursively solve for the next column. If not feasible, backtrack and try other configurations.

## 📈 Performance Metrics:
Test Cases Passed: 10 / 10

Accuracy: 100%

Points Earned: 8 / 8

Time Taken: 0.08 sec 🧩

## 🔍 Why It Matters:
This problem is a cornerstone of backtracking and constraint satisfaction problems. Solving it helps solidify concepts like:

Recursive state exploration

Efficient constraint pruning

Elegant use of hash sets for conflict detection

## ✨ Key Learnings:
Backtracking isn’t just about brute force—it's about exploring smartly and cutting off bad paths early. 🧠
Also, this builds a strong foundation for solving complex problems like Sudoku, Word Search, and Graph Coloring.

## 🏷️ Hashtags:
#gfg160 #geekstreak2025 #Day77
#nqueen #backtracking #dsa
#interviewquestions #framesbyvikash #madewithlogic #python

