# 导入即执行
print("******import person.py******")

# 定义一个函数
def hello():
    print("hello,i'm module.")
    
# 定义一个类,用来形容普通的人
class BasicPeople():
    # 用None给不确定的值赋值
    name = None
    gender = None
    age = None
    def sayHello(self):
        print("hello")

# 定义一个对象-实例化类
#jack = BasicPeople()

# 定义一个子类，描述中国人
class ChinesePeople():
    name = None
    gender = None
    age = None
    country = "China"
    def sayHello(self):
        print("你好，我来自中国。")

#zhangsan = ChinesePeople()