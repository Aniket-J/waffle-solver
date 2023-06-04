import csv

class WordleGame:
    def __init__(self):
        self.grid_size = 0
        self.grid_letters = []
        self.grid_colors = []

    def get_user_input(self):
        # Prompt for grid size
        while self.grid_size not in [3, 5, 7, 9]:
            try:
                self.grid_size = int(input("Enter the grid size (3, 5, 7, or 9): "))
            except ValueError:
                print("Invalid input. Please enter a valid grid size.")

        # Prompt for grid letters and colors
        print("Enter the letters for the grid (use comma-separated values):")
        for _ in range(self.grid_size):
            row = input().split(",")
            if len(row) != self.grid_size:
                print(f"Invalid input. Each row should contain {self.grid_size} values.")
                return
            self.grid_letters.append(row)

        print("Enter the colors for the grid (use comma-separated values, 1 for no color, 2 for yellow, 3 for green):")
        for _ in range(self.grid_size):
            row = input().split(",")
            if len(row) != self.grid_size:
                print(f"Invalid input. Each row should contain {self.grid_size} values.")
                return
            self.grid_colors.append(row)

        # Save user input to CSV file
        self.save_user_input()

    def save_user_input(self):
        with open("user_input.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.grid_size])
            writer.writerows(self.grid_letters)
            writer.writerows(self.grid_colors)

# Create an instance of the WordleGame class
game = WordleGame()
# Prompt the user for input
game.get_user_input()
