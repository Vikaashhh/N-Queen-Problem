class Solution:
    def nQueen(self, n):
        result = []

        # Helper function jo recursively queen ko board par place karega
        def solve(col, current, diagonals, anti_diagonals, rows):
            # Agar humne saare columns fill kar diye (base case)
            if col == n:
                result.append(current[:])  # Valid configuration mil gaya
                return

            for row in range(1, n + 1):  # 1-based indexing for row
                # Check karo agar is row mein, diagonal ya anti-diagonal par queen already hai
                if (
                    row in rows
                    or (row - col) in diagonals
                    or (row + col) in anti_diagonals
                ):
                    continue  # Agar threat hai toh skip karo

                # Safe position mili hai, place queen
                current.append(row)
                rows.add(row)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Recursively next column mein queen place karo
                solve(col + 1, current, diagonals, anti_diagonals, rows)

                # Backtrack: queen hatao and try next option
                current.pop()
                rows.remove(row)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        # Initial call
        solve(0, [], set(), set(), set())
        return result
