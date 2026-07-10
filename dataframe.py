import pandas as pd
stu_data={
    "rollno" : [1,2,3,4,5],
    "Name" : ["pari","raj","sneha","jay","khushi"],
    "gender" : ["femal","male","female","male","female"],
    "course" : ["BscIT","BBA","Bcom","Btech","BCA"],
    "marks" :   [50,45,46,47,48]   
        
}
df=pd.DataFrame(stu_data)
print("student data")
print(df)
print("\n student information")
print(df.info())
print(df.describe())

import pandas as pd
emp_data={
    "employee_id":[1,2,3,4,5], 
    "Name":["jay","raj","pari","sneha","dev"],
    "Department":["It","hr","sales","manager","hr"],
    "salary":[25000,30000,40000,50000,60000],
    "experience":["5 years","2 years","3 years","4 years","2 years"]
                
}
df=pd.DataFrame(emp_data)
print("employee data")
print(df)
print("\n employee information")
print(df.info())
print("\n employee description")
print(df.describe())

import pandas as pd
car_data={
    "car_id":[2507,4562,7843,1287,3429],
    "brand_name":["BMW","TATA","suzuki","maruti","toyota"],
    "price":[500000,700000,800000,1000000,900000],
    "fuel type":["diesal","petrol","diesal","petrol","diesal"],
    "mileage":[55,80,90,100,90]
}
df=pd.DataFrame(car_data)
print("car data")
print(df)

import pandas as pd
patient_data={
    "patient_id":[203,704,843,409,640],
    "Name":["raj","mehul","jay","parul","abhi"],
    "age":[25,56,34,56,88],
    "gender":["male","male","male","female","male"],
    "disease_name":["fever","headache","BP","sugar","thoyrode"],
    "doctor_name":["Dr patel","Dr jay","Dr mehta","Dr raj","Dr siraj"]
}
df=pd.DataFrame(patient_data)
print("patient data")
print(df)