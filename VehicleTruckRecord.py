# UID: Unique Truck ID
# chkoutCtr: Counter to keep track of entry and exit
# Left: Left Node for Tree
# Right: Right Node for Tree

# Class TruckNode : Represents a structure for a Unique truck. It will populate Uid and Counter
class TruckNode:
    def __init__(self, Uid=None):
        self.Uid = Uid 
        self.chkoutCtr = 0
        
# Class BSTNode will consists of all the methods needed for our problem statement. 
# We are using the python inheritance property to inherit the Trucknode in below class
class BSTNode(TruckNode):
    # Initialising BSTNode with Uid, Counter, Left and Right. Left and Right will provide the base for tree
    # Each tree node will be represented by Unique ID
    def __init__(self, Uid=None):
        super().__init__(Uid) 
        self.left = None
        self.right = None

    # This function will be used to read UIDs from input files and feed the tree. 
    # It will first try to search the UID in tree, if found will update the counter else will add the UID - logn
    def _readTruckRec(self, Uid=None):
        if not self.Uid:
            self.Uid = Uid
            return

        if self.Uid == Uid:
            if(self.chkoutCtr/2<limit):
                self.chkoutCtr+=1
            else:
                print("vehicle id "+ str(self.Uid) +" no longer available for service")
            return

        if Uid < self.Uid:
            if self.left:
                self.left._readTruckRec(Uid)
                return
            self.left = BSTNode(Uid)
            return

        if self.right:
            self.right._readTruckRec(Uid)
            return
        self.right = BSTNode(Uid)

    # This method will check the status of a Truck. It will do a search in the tree to find the UID status -logn
    def _checkTruckRec(self, Uid):
#         Uid = TruckNode(Uid)
        if Uid == self.Uid:
            if(self.chkoutCtr==0):
                return(print("Vehicle id" + str(self.Uid) + " just reached the warehouse"))
                
            if(self.chkoutCtr%2==1):
                return(print("Vehicle id " +str(self.Uid)+ " entered " +str(self.chkoutCtr)+ " time into the system. It is currently fulfilling an open order"))
                
            if(self.chkoutCtr%2==0):
                return(print("Vehicle id " +str(self.Uid)+ " entered " +str(self.chkoutCtr)+ " time into the system. It just completed an order"))
              

        if Uid < self.Uid:
            if self.left is not None:
                self.left._checkTruckRec(Uid)
                return
        if self.right is not None:
            return self.right._checkTruckRec(Uid)
            return   
        return(print("Vehicle id " +str(Uid)+ " did not come to the warehouse today"))

    # This method will traverse the complete tree and print the output- n    
    def _printTruckRec(self,Uids):
        global print_TN_counter 
        if self.left is not None:
            self.left._printTruckRec(Uids) 
        if self.Uid is not None:
              Uids.append(str((self.Uid))+", "+str(self.chkoutCtr))
#             print(str(self.Uid)+", "+str(self.chkoutCtr))        
        if self.right is not None:
            self.right._printTruckRec(Uids)
        return(Uids)

    # This function will be used to input UIDs  
    # It will first try to search the UID in tree, if found will update the counter else add the UID
    def _updateTruckRec(self, Uid):
        if not self.Uid:
            self.Uid = Uid
            return

        if self.Uid == Uid:
            if(self.chkoutCtr/2<limit):
                self.chkoutCtr+=1
                print("Vehicle Id" ,self.Uid ,"record updated")
                return
            else:
                print("vehicle id "+ str(self.Uid) +" no longer available for service")
            return

        if Uid < self.Uid:
            if self.left:
                self.left._updateTruckRec(Uid)
                return
            self.left = BSTNode(Uid)
            print("Vehicle Id" ,Uid ,"record updated")
            return

        if self.right:
            self.right._updateTruckRec(Uid)
            return
        self.right = BSTNode(Uid)
        print("Vehicle Id" ,Uid ,"record updated")
        return
        
        
    # Getting the sum for divident and remainder of checkcounter by 2    
    def calculateSum(self):  
        sum_E=sum_O = sumRight = sumLeft = 0;  

            #Check whether tree is empty  
        if(self == None):  
            print("Tree is empty");  
            return 0
        
        # Calculate the sum of nodes present in left subtree 
        else:
            if(self.left != None):  
                sumLeft = self.left.calculateSum()

            #Calculate the sum of nodes present in right subtree  
            if(self.right != None):  
                sumRight = self.right.calculateSum()

            sum_all[0] = sum_all[0] + int((self.chkoutCtr)/2)
            sum_all[1] = sum_all[1] + (self.chkoutCtr)%2
                
        return(sum_all)
    
    # Refer the function definition from question
    def _printOrderStatus(self, targetorders):
        global sum_all
        sum_all = [0,0]
        sum_all = self.calculateSum()
        print("The following status of", targetorders," orders:") 
        print("Open Orders:", sum_all[1])
        print("Closed Orders:",sum_all[0])
        print("Yet to be fulfilled:",targetorders - sum(sum_all) )
    
    # Checking the chckcounter threshold with respect frequency
    def _highFreqTrucks_Uids(self, frequency,Uids): 
        if self.left is not None:
            self.left._highFreqTrucks_Uids(frequency,Uids)
        if self.Uid is not None:
            if(self.chkoutCtr>frequency):
#                 print(str(self.Uid)+", "+str(self.chkoutCtr))
                Uids.append(str((self.Uid))+", "+str(self.chkoutCtr))
                
        if self.right is not None:
            self.right._highFreqTrucks_Uids(frequency,Uids)
#         return("No such vehicle present in the system")
        return(Uids)
    
    def _maxDeliveries(self,Uids):
        if self.left is not None:
            self.left._maxDeliveries(Uids)
        if (self.Uid is not None):
            if(int(self.chkoutCtr/2)==limit):
                Uids.append(self.Uid)
        if self.right is not None:
            self.right._maxDeliveries(Uids)
        return(Uids)
    
    def _availTrucks(self,Uids):
        if self.left is not None:
            self.left._availTrucks(Uids)
        if (self.Uid is not None):
            if(int(self.chkoutCtr%2)==0):
                if(int(self.chkoutCtr/2)<limit):
                    Uids.append(self.Uid)
        if self.right is not None:
            self.right._availTrucks(Uids)
        return(Uids)

## Other functions
def print_out(command):
    print("-----------------------------------------------")
    print("-------------",command,"---------------")


import os
import sys


def main():
    input_filename = os.getcwd()+"/"+'inputPS2.txt'
#     input_filename = 'inputPS2_20k.txt'
    prompt = os.getcwd()+"/"+'promptsPS2.txt'
    with open(input_filename, 'r') as file:
        for i,line in enumerate(file):
            if(i==0):
                global limit
                limit = int(line.strip())
            if(i==1):

                bst = BSTNode((int(line.strip())))
            if(i>1):

                 bst._readTruckRec((int(line.strip())))
   
    with open(prompt, 'r') as file:
        for i,line in enumerate(file):
#             print(i,line.strip(),(line.split(":")))
            if(line.find('printTruckRec'))==0:
                print("\n")
                print_out(line.strip())
                print_TD_OP = bst._printTruckRec([])
                print("Total number of vehicles entered in the warehouse: ",len(print_TD_OP))
                print(*print_TD_OP, sep="\n")
            if(line.find('checkTruckRec'))==0:
                print_out(line.strip())
                Uid_input = int((line.split(":"))[1])
                bst._checkTruckRec(Uid_input) 
                print("\n")
            if(line.find('printOrderStatus'))==0:
                print_out(line.strip())
                Uid_input = int((line.split(":"))[1])
                bst._printOrderStatus(Uid_input)    
            if(line.find('highFreqTrucks'))==0:
                print_out(line.strip())
                Uid_input = int((line.split(":"))[1])
                highfreq_op = bst._highFreqTrucks_Uids(Uid_input,[]) 
                if(highfreq_op):
                    print("Vehicles that moved in/out more than", Uid_input ,"times are:")
                    print(*highfreq_op, sep="\n")
                else:
                    print("No such vehicle present in the system")
            if(line.find('maxDeliveries'))==0:
                print_out(line.strip())
                print("maxDeliveries:",limit)
                max_deliveries_UIDs = bst._maxDeliveries([])
                print(len(max_deliveries_UIDs),"Vehicle Ids did their maximum deliveries:")
                print(*max_deliveries_UIDs,sep = "\n")
            if(line.find('availTrucks'))==0:
                print_out(line.strip())
                avail_trucks = bst._availTrucks([])
                print( len(avail_trucks),"Vehicle Ids that are currently available to deliver supplies:")
                print(*avail_trucks,sep = "\n")
            if(line.find('updateTruckRec'))==0:
                print_out(line.strip())
                Uid_input = int((line.split(":"))[1])
                bst._updateTruckRec(Uid_input)
        return
    
    
orig_stdout = sys.stdout
filename = os.getcwd()+"/"+"outputPS2.txt"
f = open(filename, 'w')
sys.stdout = f

main()

sys.stdout = orig_stdout
f.close()

