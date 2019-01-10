

# 定义一个函数
def hello():
    print("hello,i'm module.")
    

# 定义一个类,用来形容普通的人
class BasicPeople():
    def __init__(self, name=None, age=None ,gender = None):
        self.name = name
        self.age = age
        self.gender = gender
    
    def sayHello(self):
        print("hello")
    
    def say(self):
        print("My name is {0}".format(self.name))

# 定义一个对象-实例化类
#jack = BasicPeople()

# 定义一个子类，描述中国人
class ChinesePeople(BasicPeople):
    def sayHello(self):
        print("你好，我来自中国。")

if __name__ == '__main__':
    print("******person.py******")


