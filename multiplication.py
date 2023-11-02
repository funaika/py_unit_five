#multiplication tables
#kalen funai
#11/01/2023

def multiplication_table(numberLearned):
    strV = ""
    for x in range(1,10):
        multiNumber = str(numberLearned * x)
        strV += multiNumber + " "
    print(strV)

multiplication_table(6)