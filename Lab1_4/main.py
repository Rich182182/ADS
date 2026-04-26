class Student:
    def __init__(self, surname, name, group, city, region):
        self.surname = surname
        self.name = name
        self.group = group
        self.city = city
        self.region = region

    def __str__(self):
        return f"{self.region} | {self.city} | {self.surname} {self.name}, {self.group}"


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j].region < arr[min_idx].region:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def index_sort(arr):
    n = len(arr)
    indices = list(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            s1 = arr[indices[i]]
            s2 = arr[indices[j]]
            if s2.region < s1.region or (s2.region == s1.region and s2.city < s1.city):
                indices[i], indices[j] = indices[j], indices[i]

    sorted_arr = [arr[i] for i in indices]
    for i in range(n):
        arr[i] = sorted_arr[i]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i].region <= R[j].region:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def print_array(arr):
    for s in arr:
        print(s)
    print()


def main():
    students = [
        Student("Коваленко", "Іван", "КІ-1", "Київ", "Київська"),
        Student("Шевченко", "Анна", "КІ-2", "Львів", "Львівська"),
        Student("Бойко", "Петро", "КІ-1", "Біла Церква", "Київська"),
        Student("Мельник", "Олена", "КІ-3", "Одеса", "Одеська"),
        Student("Ткаченко", "Марія", "КІ-2", "Дрогобич", "Львівська"),
        Student("Кравченко", "Олег", "КІ-1", "Харків", "Харківська")
    ]

    print("--- РІВЕНЬ 1: До сортування ---")
    arr1 = list(students)
    print_array(arr1)

    print("--- РІВЕНЬ 1: Сортування вибіркою (за областю) ---")
    selection_sort(arr1)
    print_array(arr1)

    print("--- РІВЕНЬ 2: Сортування за індексами (Область -> Місто) ---")
    arr2 = list(students)
    index_sort(arr2)
    print_array(arr2)

    print("--- РІВЕНЬ 3: Сортування низхідним злиттям (за областю) ---")
    arr3 = list(students)
    merge_sort(arr3)
    print_array(arr3)


if __name__ == "__main__":
    main()