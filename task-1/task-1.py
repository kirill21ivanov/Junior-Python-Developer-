import random
import unittest

class CityGrid:
    def __init__(self, rows, columns, blockage_rate=0.3):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]  # 0 - свободно, 1 -  блок
        self.blockage_rate = blockage_rate

        self.generate_grid() # гинерируем

    def generate_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if random.random() < self.blockage_rate:
                    self.grid[row][col] = 1  # блокированный блок

    def display_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
class Test(unittest.TestCase):  # Юниты, чтобьы просто проверить))

    def test_1(self):
        rows = 5
        columns = 5
        city = CityGrid(rows, columns)
        city.display_grid()

    def test_2(self):
        rows = 4
        columns = 4
        city = CityGrid(rows, columns)
        city.display_grid()

    def test_3(self):
        rows = 5
        columns = 6
        city = CityGrid(rows, columns)
        city.display_grid()

    def test_4(self):
        rows = 6
        columns = 6
        city = CityGrid(rows, columns)
        city.display_grid()

    def test_5(self):
        rows = 1
        columns = 1
        city = CityGrid(rows, columns)
        city.display_grid()

if __name__ == '__main__':
    unittest.main()
