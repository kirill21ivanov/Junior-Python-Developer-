import unittest
class CityGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]  # пустая сетка города

    def display(self):
        for row in self.grid:
            print(row)
class Tower:
    def __init__(self, x, y, range):
        self.x = x
        self.y = y
        self.range = range

    def place_on_grid(self, city_grid):
        city_grid.grid[self.x][self.y] = 1 # установка башни на сетку

    def visualize_coverage(self, city_grid): # визуалка башни
        for i in range(max(0, self.x - self.range), min(city_grid.size, self.x + self.range + 1)):
            for j in range(max(0, self.y - self.range), min(city_grid.size, self.y + self.range + 1)):
                city_grid.grid[i][j] = 2
class Test(unittest.TestCase):  # Юниты, чтобьы просто проверить))

    def test_1(self):
        city = CityGrid(size=5)
        tower = Tower(x=2, y=2, range=1)
        tower.place_on_grid(city)
        tower.visualize_coverage(city)
        city.display()

    def test_2(self):
        city = CityGrid(size=5)
        tower = Tower(x=4, y=4, range=1)
        tower.place_on_grid(city)
        tower.visualize_coverage(city)
        city.display()

    def test_3(self):
        city = CityGrid(size=7)
        tower = Tower(x=6, y=6, range=1)
        tower.place_on_grid(city)
        tower.visualize_coverage(city)
        city.display()

    def test_4(self):
        city = CityGrid(size=5)
        tower = Tower(x=1, y=1, range=1)
        tower.place_on_grid(city)
        tower.visualize_coverage(city)
        city.display()

    def test_5(self):
        city = CityGrid(size=5)
        tower = Tower(x=0, y=2, range=1)
        tower.place_on_grid(city)
        tower.visualize_coverage(city)
        city.display()

if __name__ == '__main__': # запуск 
    unittest.main()
