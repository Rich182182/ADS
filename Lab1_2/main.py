import math
import random


class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4

    def area(self):
        a = abs(self.x2 - self.x1)
        b = abs(self.x3 - self.x4)
        h = abs(self.y3 - self.y1)
        return 0.5 * (a + b) * h

    def perimeter(self):
        a = abs(self.x2 - self.x1)
        b = abs(self.x3 - self.x4)
        c = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        d = math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        return a + b + c + d

    def __str__(self):
        return f"Трапеція(Площа={self.area():.2f}, Периметр={self.perimeter():.2f})"


class HashTable:
    def __init__(self, size, resolve_collisions=False):
        self.size = size
        self.table = [None] * size
        self.A = 0.6180339887
        self.resolve_collisions = resolve_collisions

    def hash_function(self, key):
        val = key * self.A
        fractional_part = val - int(val)
        return int(self.size * fractional_part)

    def insert(self, item):
        key = item.area()
        idx = self.hash_function(key)

        if not self.resolve_collisions:
            if self.table[idx] is None:
                self.table[idx] = item
                return True
            return False

        original_idx = idx
        i = 0
        while i < self.size:
            curr_idx = (original_idx + i) % self.size
            if self.table[curr_idx] is None or self.table[curr_idx] == "DELETED":
                self.table[curr_idx] = item
                return True
            i += 1
        return False

    def delete_by_perimeter(self, min_p, max_p):
        for i in range(self.size):
            item = self.table[i]
            if item is not None and item != "DELETED":
                if min_p <= item.perimeter() <= max_p:
                    self.table[i] = "DELETED"

    def display(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"[{i}] Порожньо")
            elif self.table[i] == "DELETED":
                print(f"[{i}] DELETED")
            else:
                print(f"[{i}] Ключ={self.table[i].area():.2f} | {self.table[i]}")


def generate_trapeze():
    y1 = random.randint(0, 10)
    y3 = random.randint(11, 20)
    x1 = random.randint(0, 5)
    x2 = random.randint(6, 15)
    x4 = random.randint(0, 5)
    x3 = random.randint(6, 15)
    return Trapeze(x1, y1, x2, y1, x3, y3, x4, y3)


def main():
    size = int(input("Введіть розмір хеш-таблиці: "))

    print("\n 1 ")
    ht1 = HashTable(size, resolve_collisions=False)
    for _ in range(size):
        ht1.insert(generate_trapeze())
    ht1.display()

    print("\n 2 ")
    ht2 = HashTable(size, resolve_collisions=True)
    for _ in range(size):
        ht2.insert(generate_trapeze())
    ht2.display()

    print("\n 3 ")
    min_p = float(input("Мін. периметр: "))
    max_p = float(input("Макс. периметр: "))
    ht2.delete_by_perimeter(min_p, max_p)
    ht2.display()


if __name__ == "__main__":
    main()