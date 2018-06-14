#Checks how many digits contains inputed natural number
#n>0 ; type(n)==int

def task86A(n):
    numberOfDigits=1;
    if ((n-(n % 10)) > 0):
        numberOfDigits+=task86A((n-(n%10))/10);
    return numberOfDigits
