class Cat:
    def mews(self):
        print('meow!')
class Lion(Cat):
    def bark(self):
        print('raaar!')

leo = Lion()
leo.mews()