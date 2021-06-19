#exercise-34
class copy():
    def __init__(self,FileAddress,NewAddress):
        self.address = FileAddress
        self.new = NewAddress
    def CopyFile(self):
        while True:
            #if file dosent exist,while loop can input again
            try:
                f = open(self.address)
                break
            except:
                print("oOps file dosent found,please check your input and try again")
                self.address = input("please enter address: ")
                continue
        f = open(self.address)
        copy = f.read()
        with open (self.new,"a") as c:
            c.write(copy) 
        print("Done!")


# Example
# a = copy("C:/Users/TechZone-PC/Desktop/930.txt","F:/copy.txt").CopyFile()

