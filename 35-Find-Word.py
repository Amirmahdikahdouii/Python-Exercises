#Exercise_35
class WrongError (Exception):
    pass
class Check (WrongError):
    def Find(self):
        a = input("please Enter Your File Address ")
        try:
            with open (a) as f:
                l = f.readlines()
            count = 0
            b = input("please Enter Your Word That You looking For: ")
            wordCount = 0
            for val in l :
                if "free" in val.lower():
                    count += 1
                if b in val :
                    wordCount += 1
            print ("----------------------------")
            print (f" {b} in Text: {wordCount} Times!")
            try:
                if count > 0 :
                    raise WrongError 
            except WrongError as WR:
                print (f""" WrongWord Error    
---------------------------            
We Have Found \'Free\' 
in your File {count} Times!
---------------------------""")
        except:
            print("Oops file Doesnt Found, please Try Again")
            self.Find()


a= Check()
a.Find()
