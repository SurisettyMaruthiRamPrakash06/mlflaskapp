import pandas as pd
screen_time=[4,6,5]
stu_name=['asad','karthik','chintu']
id = [1,2,3]
my_dict={"id":id,"screen_time":screen_time,"stu_name":stu_name}
print(my_dict)
df=pd.DataFrame(my_dict)
print(df)