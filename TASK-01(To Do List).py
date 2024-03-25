import os
def start_up():
    print("************* DAILY DIARY **************")
    print("****************************************")
    print("")
    print("|S.No|","\t\t","|TASKS|")
    print("")    
    for i in range(len(Task)):
        print(index[i],"\t\t",Task[i])
    print("****************************************")    
    print("****************************************")    
    print("ADD TASk: Enter 1")
    print("REMOVE TASK: Enter 2")
def Task_adder(Task,Task_list):
    Task_list.append(Task)
def Task_remover(index,Task_list):
    del Task_list[index-1]
Task=[]
index=[]
while True:
    os.system('cls')
    index=[]
    for i in range(len(Task)):
       index.append(i+1)
    start_up()
    while True:
        user_input=input("Enter for add or remove tasks: ")
 
        if user_input== "1":
            a=input("Enter the task: ")    
            Task_adder(a,Task)
            break
        elif user_input== "2":
            while True:
                b=int(input("Enter the index of task: "))
                if (b<0 or b>len(Task)):
                    print("Invalid Input")
                else:
                    Task_remover(b,Task)
                    break
            break    
        else:
            print("Invalid Input")
            continue        
    
               
