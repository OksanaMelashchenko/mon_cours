import os
import os.path
import json



class FileStorage:
    @staticmethod
    def load_from_file(path):
        if os.path.isfile(path):
            size = os.path.getsize(path)
            isempty = size
            if isempty != 0:
                return FileStorage


    def add_file(self, path):
        if os.path.isfile(path):
            with open(path, 'r') as f:
                data = f.read()
                print(data)
        else:
            with open(path, 'a+') as f:
                data = f.read()
                f.write(data)
        return FileStorage(**json.load(file_path))




storage = FileStorage()

class App:
    menu_items = None

    def __init__(self, storage):
         self.group_curs = []

    def add_curs(self, data):
        with open(file_path, 'a+') as f:
            self.group_curs.append(data.split())
            f.write(data + '\n')


    def vse_curs(self):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = f.read()
                print(data)


    def run(self):
        print('''оберіть дію.
                    1- додати курс, 
                    2 - показати всі курси
                    3 - вийти з програми \n''')



if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))


while True:
    app.run()
    f = input('введіть дію:  ')
    if f == '1':
        print('введіть назву курсу')
        app.add_curs(input())
    elif f == '2':
        print('перелік  курсів')
        app.vse_curs()
    elif f == '3':
        break
    else:
        print('дія обрана невірно')