class ClassTest:
    def instance_method(self): # instance method takes self as the first parameter, which refers to the instance of the class
        print(f"Called instance_method of {self}")

        @classmethod
        def class_method(cls): # class method takes cls as the first parameter, which refers to the class itself
            print(f"Called class_method of {cls}")

        @staticmethod
        def static_method(): # static method does not take any parameters, not even cls or self
            print("Called static_method")

ClassTest.class_method() # Output: Called class_method of <class '__main__.ClassTest'>
ClassTest.static_method() # Output: Called static_method