#!/usr/bin/env python3
import sys
import collections
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grade():
        if sys.argv[1]=='teacher':
            grade=sys.argv[2]
            output=collections.defaultdict(list)
            for x in ['A','B','C','D']:
                output[x]=grade.count(x)
            print(output)
        elif sys.argv[1]=='student':
            grade=sys.argv[2]
            output=collections.defaultdict(list)
            output['Pass']=0
            for x in ['A','B','C']:
                output['Pass']+=grade.count(x)
            output['Fail']=grade.count('D')
            print(output)
        else:
            print('Enter the job of given person:')
            get_grade(input())


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

if __name__=='__main__':
    print(Person.get_grade())
