import pandas as pd
stu_marks=pd.Series([25,56,45,23,67])
print("student marks")
print(stu_marks)


print("maximum marks :",stu_marks.max())
print("minimum marks :",stu_marks.min())
print("average marks :",stu_marks.mean())
print("total  marks :",stu_marks.sum())


print(stu_marks[stu_marks>30])
print(stu_marks[stu_marks<30])


import pandas as pd
stu_name=pd.Series(["pari","khushi","sneha","raj","jay"],index=[1,2,3,4,5])
print("student names")
print(stu_name)

import pandas as pd
stu_attendence=pd.Series([34.67,45.78,78.90,90.89,87.65])
print("student attendence")
print(stu_attendence)

print(stu_marks[stu_attendence>65])
print(stu_marks[stu_attendence<65])

import pandas as pd
stu_data={
    "name":["pavan","raj","pari","khushi","disha"],
    "age":[23,43,21,24,28],
    "course":["BCA","bsc","bcom","bsc","btech"],
    "rollno":[1,2,3,4,5],
    "city":["morbi","rajkot","surat","ahmedabad","gandhinagar"]
}

df=pd.DataFrame(stu_data)
print("student information")
print(df)

print("\n student information")
print(df.info())

print("\n student description")
print(df.describe())

