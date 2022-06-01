import csv

def write_into_csv(info_list):
    with open ('student_info.csv','a',newline='') as csv_file:
        writer= csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["name","age","contact_number", "email"])

        writer.writerow(info_list)





if __name__ == '__main__':
    condition =True

    while(condition):
        student_info =input("Enter some Student information  in the following  format(Name age  contact email):")



        #split

        student_info_list= student_info.split(' ')
        print("\n Entered  information is -\n Name: {}\n age: {} \n contactno: {}\n email: {} ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is Entered information correct (yes/no):")


        if(choice_check =="yes"):
            write_into_csv(student_info_list)

            condition_check=input("Enter (yes/no) if you want to enter information for another student ")
            if  condition_check =="yes":
                condition =True
            elif condition_check == "no":
                condition =False
        elif choice_check =="no":
                print("\n Please re-enter the values")
