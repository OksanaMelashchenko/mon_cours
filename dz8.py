import json

class Student:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        d = {}
        d['first_name'] = self.first_name
        d['last_name'] = self.last_name
        return print(d)


student = Student('John', 'Doe')
student.info()


class Storage:
    def __init__(self):
        self.fruits_list = []

    def add(self, fruits):
        self.fruits_list.append(fruits)

    def get(self, el):
        self.fruits_list.sort()
        k = []
        l1 = [c for c in el]
        l3 = len(l1)
        if l3 == 0:
            if len(self.fruits_list) < 5:
                return print(self.fruits_list)
            else:
                return print(self.fruits_list[0:5])
        for i in self.fruits_list[0:6]:
            l2 = [h for h in i]
            s = 0
            for f in range(l3):
                if l1[f] == l2[f]:
                    s = s + 1
                    continue
                else:
                    break
            if s == l3:
                k.append(i)
                continue
        return print(k)


fruits_storage = Storage()

fruits_storage.add('plum')
fruits_storage.add('apple')
fruits_storage.add('peach')
fruits_storage.add('apricot')
fruits_storage.add('pineapple')

fruits_storage.get('')
fruits_storage.get('a')
fruits_storage.get('p')
fruits_storage.get('abc')
fruits_storage.add('pear')
fruits_storage.get('')


class Course(Student):
    def __init__(self, curs):
        self.curs = curs

    def add_student(self, object1):
        f = {}
        f['name'] = self.curs
        f['students'] = [{'first_name': student.first_name, 'last_name': student.last_name}]
        print('f=', f)
        return f


python_basic = Course('Python basic')

python_basic.add_student(Student('Jane', 'Doe'))
