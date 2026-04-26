class Student:
    def __init__(self, surname, course, student_id, avg_grade, citizenship):
        self.surname = surname
        self.course = course
        self.student_id = student_id
        self.avg_grade = avg_grade
        self.citizenship = citizenship


class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if not self.root:
            self.root = Node(student)
            return
        curr = self.root
        while True:
            if student.student_id < curr.student.student_id:
                if not curr.left:
                    curr.left = Node(student)
                    break
                curr = curr.left
            elif student.student_id > curr.student.student_id:
                if not curr.right:
                    curr.right = Node(student)
                    break
                curr = curr.right
            else:
                break

    def traverse_bfs(self):
        if not self.root:
            return
        queue = [self.root]
        print(f"{'ID':<6} | {'Прізвище':<12} | {'Курс':<4} | {'Бал':<4} | {'Громадянство'}")
        print("-" * 50)
        while queue:
            curr = queue.pop(0)
            s = curr.student
            print(f"{s.student_id:<6} | {s.surname:<12} | {s.course:<4} | {s.avg_grade:<4} | {s.citizenship}")
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        print()

    def search_criteria(self, course, min_grade, citizenship):
        res = []
        if not self.root:
            return res
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            s = curr.student
            if s.course == course and s.avg_grade >= min_grade and s.citizenship == citizenship:
                res.append(s)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return res

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, root, key):
        if not root:
            return root
        if key < root.student.student_id:
            root.left = self._delete_node(root.left, key)
        elif key > root.student.student_id:
            root.right = self._delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_node = self._get_min(root.right)
            root.student = min_node.student
            root.right = self._delete_node(root.right, min_node.student.student_id)
        return root

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete_by_criteria(self, course, min_grade, citizenship):
        to_delete = [s.student_id for s in self.search_criteria(course, min_grade, citizenship)]
        for key in to_delete:
            self.delete(key)


def main():
    tree = BinaryTree()

    students = [
        Student("Коваленко", 2, 500, 85, "Україна"),
        Student("Шевченко", 3, 300, 95, "Україна"),
        Student("Бойко", 3, 700, 92, "Україна"),
        Student("Мельник", 1, 200, 95, "Польща"),
        Student("Ткаченко", 3, 400, 91, "Україна"),
        Student("Кравченко", 3, 600, 98, "Україна"),
        Student("Олійник", 4, 800, 88, "Україна")
    ]

    for st in students:
        tree.insert(st)

    print("--- Дерево після створення ---")
    tree.traverse_bfs()

    course = int(input("Введіть курс для пошуку: "))
    min_grade = int(input("Введіть мінімальний бал: "))
    citizenship = input("Введіть громадянство: ")

    found = tree.search_criteria(course, min_grade, citizenship)
    print("\n--- Результат пошуку ---")
    if not found:
        print("Студентів не знайдено.")
    else:
        for s in found:
            print(f"{s.student_id:<6} | {s.surname:<12} | {s.course:<4} | {s.avg_grade:<4} | {s.citizenship}")

    print("\n--- Видалення знайдених вузлів ---")
    tree.delete_by_criteria(course, min_grade, citizenship)

    print("\n--- Дерево після видалення ---")
    tree.traverse_bfs()


if __name__ == "__main__":
    main()