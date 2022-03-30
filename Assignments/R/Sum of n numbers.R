i=1
sum=0
num1<-readline(prompt="Enter the number")
num1<-as.integer(num1)
while(i<=num1)
{
  sum=sum+i
  i=i+1
}
print(sum)
