class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self,toWhom):
        print(f"hello, {toWhom}. I am {self.name}")

rtan = Person("르탄")
rtan.sayhello("병관")