
class Stock:

    def __init__(self,Id, StructName, Amount, Cost):
        self.StructName = StructName
        self.Id = Id
        self.Amount = Amount
        self.Cost = Cost
        
    def getID(self):
        return self.Id
    def getAmount(self):
        return self.Amount
    def getCost(self):
        return self.Cost
    def getStructName(self):
        return self.StructName
    
class Manage:
    
    def Add_Item(stock):
        filename = "DATA.txt"
        # a is write the end of txt || w is delete and write new txt
        # check if ID in DATA is equal stock.getID()
        # have to update ,dont Add
        CheckList = Manage.helperCheck()
        for i in range (0, len(CheckList)):
            checker = CheckList[i][0]

            #Check the same of product
            if int(checker) == int(stock.getID()):

                # update Amount and Cost
                CheckList[i][2] = str(int(stock.getAmount()) + int(CheckList[i][2]))
                CheckList[i][3] = str(stock.getCost())
                #print(CheckList)
                
                newCheckList = [num for elem in CheckList for num in elem]
                with open(filename, 'w') as data:
                    for i in range(0, len(newCheckList)):
                        if (i+1) % 4 == 0:
                            data.write(newCheckList[i] + "\n")
                        else:
                            data.write(newCheckList[i] + " ")
                # equal have to delete and update
                return
            
        #if the product not the same We can add it to txt    
        with open(filename, 'a') as data:
            data.write(str(stock.getID()) + " " +\
            str(stock.getStructName()) + " " +\
            str(stock.getAmount()) + " " +\
            str(stock.getCost())+'\n')

            
    def helperCheck(): 
        filename = "DATA.txt"
        with open(filename, 'r') as data:
            templist = [line.strip() for line in data]
        ListforCheck = [i.split(" ")for i in templist]
        #Change txt to array or list
        return ListforCheck
    
    def Delete_Item(ID, Amount):
        filename = "DATA.txt"
        CheckList = Manage.helperCheck()
        #print(CheckList)
        for i in range (0, len(CheckList)):
            if int(ID) == int(CheckList[i][0]):
                CheckList[i][2] = int(CheckList[i][2]) - int(Amount)
                if int(CheckList[i][2]) < 0:
                    return
                newCheckList = [num for elem in CheckList for num in elem]
                with open(filename, 'w') as data:
                    for i in range(0, len(newCheckList)):
                        if (i+1) % 4 == 0:
                            data.write(str(newCheckList[i]) + "\n")
                        else:
                            data.write(str(newCheckList[i]) + " ")
            else:
                continue
        return
    def Help_Delete_ALL(ID):
        CheckList = Manage.helperCheck()
        for i in range(0, len(CheckList)):
            checker = CheckList[i][0]
            if int(ID) == int(checker):
                del CheckList[i]
                return CheckList
    
    def Delete_ALL(ID):
        filename = "DATA.txt"
        thisList = Manage.Help_Delete_ALL(ID)
        thisList = [num for elem in thisList for num in elem]
        with open(filename, 'w') as data:
            for i in range(0, len(thisList)):
                if (i+1) % 4 == 0:
                    data.write(str(thisList[i]) + "\n")
                else:
                    data.write(str(thisList[i]) + " ")
        
    def Search_Item(ID):
        CheckList = Manage.helperCheck()
        for i in range (0, len(CheckList)):
            checker = CheckList[i][0]

            #Check the same of product
            if int(checker) == int(ID):
                return True
        return False


    def Show_Stock():
        templist = Manage.helperCheck()
        for j in range(0, len(templist)):
            print("CP: %r  ,NAME: %r  ,AMOUNT: %r  ,COST: %r  "\
                  %(templist[j][0],templist[j][1],templist[j][2],templist[j][3]))
        print("\n")
        
    def helper_quickSort(array):
        listleft = []
        listright = []
        if len(array) <= 0:
            return array

        if len(array) >= 1:
            pivot = array[0]
            for i in array[1:]:
                if i >= pivot:
                    listright.append(i)
                elif i <= pivot:
                    listleft.append(i)
        return Manage.helper_quickSort(listleft) + [pivot] + \
               Manage.helper_quickSort(listright)
    
    def Amount_Sorting():
        filename = "DATA.txt"
        index = []
        final = []
        CheckList = Manage.helperCheck()
        #print(CheckList)
        for i in range(0, len(CheckList)):
            index.append(int(CheckList[i][2]))

            
        newindex = Manage.helper_quickSort(index)
            
        for i in range(0, len(newindex)):
            for j in range(0, len(newindex)):
                if int(CheckList[j][2]) == int(newindex[i]):
                    final.append(CheckList[j])
                    
        lastCheckList = [num for elem in final for num in elem]
        with open(filename, 'w') as data:
            for i in range(0, len(lastCheckList)):
                if (i+1) % 4 == 0:
                    data.write(lastCheckList[i] + "\n")
                else:
                    data.write(lastCheckList[i] + " ")
        return
            

def main():
    while True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@  WAREHOSE MANAGEMENT SYSTEM  @@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + "\n")
        
        e = Manage.Show_Stock()
        print("---------------------------------------------------------")
        print("1: ADD, 2: Search, 3: Delete, 4: DeleteALL 5.SORT(amount)")
        print("---------------------------------------------------------")
        userinput = int(input("CHOOSE: "))
        if userinput == 1:
            CODE = int(input("ENTER CODE PRODUCT: "))
            NAME = (input("ENTER NAME: "))
            AMOUNT = int(input("ENTER AMOUNT: "))
            COST = int(input("ENTER COST: "))
            
            Manage.Add_Item(Stock(CODE, NAME, AMOUNT, COST))
        elif userinput == 2:
            ID = int(input("ENTER CODE PRODUCT: "))

            OK = Manage.Search_Item(ID)
            if OK:
                print("##################### FOUND ###################" + "\n")
            else:
                print("##################### NOT FOUND ###################" + "\n")
        elif userinput == 3:
            CODE = int(input("ENTER CODE PRODUCT: "))
            AMOUNT = int(input("ENTER AMOUNT: "))
            Manage.Delete_Item(CODE, AMOUNT)
        elif userinput == 4:
            CODE = int(input("ENTER CODE PRODUCT: "))
            Manage.Delete_ALL(CODE)
        elif userinput == 5:
            Manage.Amount_Sorting()

        
            

main()


