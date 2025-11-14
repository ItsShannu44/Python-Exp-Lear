def greet(self):
    print(f"Hello {self.name}")

Student=type('student',(object,),{'greet':greet, 'name':'XYZ'})
