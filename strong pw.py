user_name=input("enter the  upper case letter")
if user_name >= "A" and user_name <= "Z":
    print("it is upper case letter")
    lower_case=input("enter the lower case letter")
    if lower_case >= "a" and lower_case<= "z":
        print("it is lower case letter")
        special_char=input("enter the special_char")
        if special_char=="@" or special_char=="$" or special_char=="#":
            print("it is special character")
            numeric=input("enter the number")
            if numeric>="0" and numeric<="9":
                print("it is number")
                a=(user_name+lower_case+special_char+str(numeric))
                if len(a)==8:
                    print("it is strong password",a)
                else:
                    print("it is not strong password")
            else:
                print("it not a number")
        else:  
            print("special_char are not allowed") 
    else:
        print("lower_case not allowed")
else:
     print("upper_case are not allowed")

