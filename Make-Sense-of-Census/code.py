# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))
census=np.concatenate((data,new_record),axis=0)

age=census[:,0]
print(age)
max_age=age.max()
print(max_age)

min_age=age.min()
print(min_age)


age_mean=age.mean()

age_mean=np.round(age_mean, decimals=2)
print(age_mean)

age_std=age.std()

age_std=np.round(age_std,decimals=2)
print(age_std)


race=census[:,2]
print(race)

race_0=census[census[:,2]==0]

race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_1)
print(len_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(len_1)
print(len_2)
print(len_3)
print(len_4)
minimum=min(len_0,len_1,len_2,len_3,len_4)
if   len(race_0)==minimum:
     minority_race=0
elif   len(race_1)==minimum:
     minority_race=1  
elif   len(race_2)==minimum:
     minority_race=2
elif   len(race_3)==minimum:
     minority_race=3
elif   len(race_4)==minimum:
     minority_race=4
print(minority_race)  


citizens=census[:,0]
print(citizens)
senior_citizens=census[census[:,0]>60]
# print(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
np.round(avg_working_hours,decimals=2)
print(avg_working_hours)

num=census[:,1]
high=census[census[:,1]>10]
low=census[census[:,1]<=10]



avg_pay_high=high.mean(axis=0)[7]

# avg_pay_high=np.round(age_pay_high, decimals=2)

# age_mean=age.mean()

# age_mean=np.round(age_mean, decimals=2)
avg_pay_low=low.mean(axis=0)[7]


print(avg_pay_high)
print(avg_pay_low)



