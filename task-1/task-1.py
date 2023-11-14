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
      
class Test(unittest.TestCase):  # Юниты, чтобьы просто проверить))

    def test_1(self):
        city = CityGrid(4, 4)
        city.display_grid()

    def test_2(self):
        city = CityGrid(5, 5)
        city.display_grid()

    def test_3(self):
        city = CityGrid(5, 6)
        city.display_grid()

    def test_4(self):
        city = CityGrid(2, 2)
        city.display_grid()

    def test_5(self):
        city = CityGrid(1, 0)
        city.display_grid()

if __name__ == '__main__': # запуск 
    unittest.main()
