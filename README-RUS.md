# Junior-Python-Developer- Русская версия задания

Тестовое задание
на должность младшего разработчика Python


Представьте, что телекоммуникационная компания работает над проектированием эффективной схемы сети 7G для нового города. Город можно представить в виде сетки, где некоторые кварталы перекрыты и не могут иметь башен, в то время как другие могут. Цель состоит в том, чтобы обеспечить максимальное покрытие при минимальном количестве вышек.

Задача 1: Представление сетки
Создайте класс CityGrid, который может представлять город в виде сетки N x M. Во время инициализации класса заблокированные блоки размещаются случайным образом с охватом >30% (мы можем изменить этот параметр).

Задача 2: Покрытие вышек
Каждая вышка имеет фиксированный диапазон R (в блоках), в пределах которого она обеспечивает покрытие. Это покрытие представляет собой квадрат с башней в центре.
Реализуйте метод в классе CityGrid для размещения башни и визуализации ее покрытия.

Задача 3: Задача оптимизации
Разработайте алгоритм размещения минимального количества вышек таким образом, чтобы все незагороженные блоки находились в зоне действия как минимум

Задача 4: Надежность канала связи
Представьте, что данные передаются между вышками. Для простоты предположим, что каждая вышка может напрямую связываться с любой другой вышкой в пределах своей досягаемости.
Разработайте алгоритм для поиска наиболее надежного пути между двумя башнями. Надежность пути уменьшается с увеличением количества переходов (связей от башни к башне). Таким образом, путь с меньшим количеством переходов более надежен.

Задача 5: Визуализация
Реализуйте функции для визуализации CityGrid, включая заблокированные блоки, башни, зоны покрытия и пути передачи данных.
Используйте любую библиотеку построения графиков на Python по вашему выбору, например matplotlib или seaborn.

Бонусные задания (необязательно):
Расширьте задачу оптимизации: теперь башни имеют определенную стоимость, а у вас ограниченный бюджет. Измените свой алгоритм, чтобы максимально увеличить охват, оставаясь при этом в рамках бюджета.

Рассмотрите различные типы вышек с разной дальностью действия и стоимостью. Как это изменило бы ваш подход к оптимизации?