from selenium import webdriver
#driver = webdriver.Chrome(executable_path=r'venv\\Scripts\\chromedriver.exe')



# todo other things



#driver.get('http://www.wp.pl')

class Animal:
    def __init__(self):
        pass
    def who(self):
        print('who you')


class Dog(Animal):
    def __init__(self, name='azor', age=3):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} is {self.age} years old."

azor = Dog(age='5')
azor.who()
print(azor.name)
print(azor)