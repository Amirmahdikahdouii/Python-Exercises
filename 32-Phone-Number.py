#exercise-32
class ValueNotFound(Exception):
    """ class for raising error if input
    dosent exist"""
    pass
class irancell_num (ValueNotFound):
    def __init__(self,num,Address):
        self.num =num
        #nums = for check to understand input is correct or No.
        nums =["0901","0902","0903","0904","0905"
        ,"0930","0933","0934","0935","0936","0937"
        ,"0938","0939"]
        self.nums = nums
        self.address = Address
    def maker (self):
        while True:
            try:
                if self.num in self.nums :
                    for val in range(1000000,10000000):
                        with open(str(self.address),"a") as f:
                            f.write(str(self.num))
                            f.write(str(val))
                            f.write("\n")
                            if str(val) == "9999999":
                                f.write("The End")
                                exit(0)
                else:
                    raise ValueNotFound
            except ValueNotFound :
                print (f'{self.num} Dosent exist')
                print ("please try again")
                self.num = int(input("please enter your number: "))
                print(" ")



#Example
# a = irancell_num("0930","C:/Users/TechZone-PC/Desktop/0930.txt").maker()
