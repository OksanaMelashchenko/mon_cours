import json



class JsonParser:



    def __init__(self, s):
        self.s = s

    def from_json(self):
        res = json.loads(self.s)
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



if __name__ == '__main__':
    with JsonParser('"hello"') as peretv:
        print(peretv.from_json())


if __name__ == '__main__':
    with JsonParser('{"hello": "world", "key": [1,2,3]}') as peretv:
        print(peretv.from_json())


class Point:


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

c = Point()

print(c.x, c.y)



class Rectangle(object):


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def contains(self, el):
        kx = el.x
        ky = el.y
        if (start_point.x <= kx <= end_point.x) and (start_point.y <= ky <= end_point.y):
            return print('toshka', el.x, el.y, 'prinadlegit Rectangle')
        else:
            return print('non,', 'toshka', el.x, el.y, ' ne prinadlegit Rectangle')


start_point = Point(1, 0)
end_point = Point(7, 3)
rect = Rectangle(start_point, end_point)
rect.contains(start_point)
rect.contains(Point(-1, 3))



class MyContainer(Rectangle):


    def __init__(self):
        self.items = [rect]


    def __contains__(self, item):
        if  self.items:
            return print(True)
        else:
            return print(False)

my_container = MyContainer()


start_point in my_container
Point(-1, 3) not in my_container
