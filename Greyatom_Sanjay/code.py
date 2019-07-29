# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here

#Reading the file
data=pd.read_csv(path)

#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()

#Plotting bar plot
plt.bar(loan_status.index, loan_status)
plt.show()

#Code ends here


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#property_and_loan = pd.data(df.groupby(['Property_Area','Loan_Status'])

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

print(property_and_loan)

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']


#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')


#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_1.set_title('Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')


