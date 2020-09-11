class RegexEngine:

    def __init__(self, x):
        self.x = x
    
    
    def check_string(self):
        if self.x[0] == "" and self.x[1] == "":
            print(True)
            
        elif self.x[0] == self.x[1]:
            print(True)
            
        elif self.x[0] == "." and self.x[1]:
            print(True)
            
        elif self.x[0] == "" and self.x[1]:
            print(True)
            
        elif self.x[0] and self.x[1] == "":
            print(False)
        else:
            print(False)
        
            


my_string = RegexEngine(input().split("|"))
my_string.check_string()