# import numpy as np 
# arr=np.arange(1,10)
# print(arr)
# n=int(input("Enter dim of matrix:"))
# arr2=np.random.randint(1,100,(n,n))
# print(arr2)
# print("ram"*60)
# primer_diagonal=arr2[np.arange(n),np.arange(n)]
# print(primer_diagonal)
# secondary_diagonal=arr2[np.arange(n),np.arange(n-1,-1,-1)]
# print(secondary_diagonal)
# n=input("Enter element of array:")

# arr=np.array(n.split(","),dtype=int)
# print(arr[1])
# n=int(input("how man element:"))
# arr=np.empty(n,dtype=int)
# for i in range(n):
#     arr=int(input(f"Enter element{i+1}"))
#     print(arr)
# n=int(input("Enter matrix size:"))
# arr=np.array([list(map(int,input("enter element for row:").split(",")))for _ in range(n)for _ in range(n) ])
# print(arr)
# x=np.random.randint(1,10,5)
# print(x)
# xr=np.zeros((2,3))
# print(x)
# x=np.full((4,5),5)
# print(x)
# # arr=np.empty((2,6))
# # print(arr)
# # arr=np.indices((3,6))
# # print(arr)
# # arr=np.meshgrid((3,5))
# # print(arr)
# # arr=np.zeros_like((3,4))
# # print(arr)
# # arr=np.full_like((3,4),5)
# # print(arr)
# a=np.arange(60)
# arr1=a.reshape((10,2,3))
# print(arr1)
# arr1=np.sqrt((10,3,3))
# print(arr1)

# x=np.array([[1,2,3,4],
#             [2,3,4,5],
#             [0,2,3,4]])
# arr=np.einsum('ei,ei->e',x,x)
# print(arr)
# import numpy as np
# var=np.array([1,2,3,5,6])
# np.random.shuffle(var)
# print(var)
# var1=np.array([1,2,3,4,5,1,2,3,4])
# x=np.unique(var1,return_counts=True)
# print(x)
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv(r"C:\Users\Administrator\Desktop\test.csv")

# Train model
x = df[["cholesterol_mg_dl"]]
y = df["survival"]
model = LogisticRegression(max_iter=1000)
model.fit(x, y)

# Predict for cholesterol = 200
cholesterol = 200
predict = model.predict([[cholesterol]])[0]

if predict == 1:
    print("Survive")
else:
    print("Not Survive")
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # import the data
# df = pd.read_csv(r"C:\Users\Administrator\Desktop\test.csv")
# # independent_variable cholestrol
# x = np.array([df["cholesterol_mg_dl"]]).reshape(-1,1)


# # dependent_variable servival 
# y = np.array(df["survival"])

# x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.2 , random_state=2)

# clfModel = LogisticRegression().fit(x_train , y_train)

# # accurecy score
# acc = accuracy_score(y_test , clfModel.predict(x_test)) * 100

# cholesterol = 200
# pridict = clfModel.predict([[cholesterol]])[0]

# if pridict == 1:
#     print(f"cholesterol lavel is {cholesterol} : survive")
# elif pridict == 0 :
#     print(f"cholesterol lavel is {cholesterol} : not survive")