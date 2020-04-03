class Person(object):
    """
    Returen person name with given object
    """
    def _init_(self,name):
        self.name=name

    def get_details(self):
        """
        Return strings with person name
        """
        return self.name
class Student(Person):
    """
    Return student object, using name,branch,year parameters
    """
    def _init_(self,name,branch,year):
        Person._init_(self,name)
        self.branch=branch
        self.year=year
    def get_details(self):
        retuen "{} studies {} and is in {} year.".format(self.name)
