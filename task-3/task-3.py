import random
import unittest

class CityGrid:
    def __init__(self, rows, cols, block_percentage=30):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]  # 0 не блок, 1 блок
        self.block_percentage = block_percentage

        self.randomly_block_cells()

    def randomly_block_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.randint(1, 100) <= self.block_percentage:
                    self.grid[row][col] = 1

    def display_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def visualize_coverage(self):
        for row in self.grid:
            print(" ".join(map(lambda x: "*" if x == 2 else str(x), row)))
            
    def place_tower(self, row, col, radius):
        for i in range(max(0, row - radius), min(self.rows, row + radius + 1)):
            for j in range(max(0, col - radius), min(self.cols, col + radius + 1)):
                self.grid[i][j] = 2

    def optimize_tower_placement(self, radius):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 0:
                    self.place_tower(row, col, radius)
                    print(f"Башня находится -  ({row}, {col})")

class Test(unittest.TestCase):  # Юниты, чтобьы просто проверить))
    def test_1(self):
        city = CityGrid(5, 5)
        city.optimize_tower_placement(1)
        city.visualize_coverage()

    def test_2(self):
        city = CityGrid(5, 5)
        city.optimize_tower_placement(1)
        city.visualize_coverage()

    def test_3(self):
        city = CityGrid(5, 5)
        city.optimize_tower_placement(1)
        city.visualize_coverage()

    def test_4(self):
        city = CityGrid(5, 5)
        city.optimize_tower_placement(1)
        city.visualize_coverage()

    def test_5(self):
        city = CityGrid(5, 5)
        city.optimize_tower_placement(1)
        city.visualize_coverage()

if __name__ == '__main__': # запуск 
    unittest.main()