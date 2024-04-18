class person:
    def __init__(self, name, age, gender) :
     self.name = name
     self.age = age 
     self.gender = gender

    def introduce(self):
        print(f'hi there i am {self.name},at {self.age}, and i am {self.gender} .')

pd =person('stanley', 20,'male')

pd.introduce()







