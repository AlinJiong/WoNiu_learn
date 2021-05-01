class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print('该用户的姓名为{}'.format(self.name), end=',')
        print('该用户的年龄为{}'.format(self.age), end=',')
        print('该用户的性别为{}'.format(self.sex), end=',')


class Student(Person):
    def __init__(self, name, age, sex, college, cls):
        super().__init__(name, age, sex)
        self.college = college
        self.cls = cls

    def personInfo(self):
        super().personInfo()
        print('该用户的学校为{}'.format(self.college), end=',')
        print('该用户的班级为{}'.format(self.cls))

    def __str__(self):
        return self.name

    def study(self, Teacher):

        print('我是{},老师,{}，我终于学会了！'.format(self.__str__(), Teacher.tech()))


class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        super().__init__(name, age, sex)
        self.college = college
        self.professional = professional

    def personInfo(self):
        super().personInfo()
        print('该用户的学院为{}'.format(self.college))
        print('该用户的专业信息为{}'.format(self.professional))

    def tech(self):
        return "今天学习了unitest单元测试框架"


s1 = Student("张三", 12, '男', '计算机', 1)
s2 = Student("李四", 13, '男', '计算机', 2)
s3 = Student("王五", 14, '男', '计算机', 3)
t1 = Teacher("李六", 42, '男', '计算机', '通信工程')

s1.personInfo()
print(s1)
