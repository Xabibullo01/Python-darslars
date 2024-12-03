class Workers:
    def level(self):
          raise NotImplementedError("subclasses")
     
class developer(Workers):
    def level(self):
        print("Developer")

class designer(Workers):
    def level(self):
         print("Designer")

class Guardian(Workers):
     def level(self):
          print("Guardian")
          

pt = developer()