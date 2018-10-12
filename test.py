class Test():
      def __init__(self, name):
        self.__name = name
      def __private_method(self):
        return "Boo"
      def public_method(self):
        print(self.__name)
        return self.__private_method()
     
x = Test("testtest")

print(x.public_method())
