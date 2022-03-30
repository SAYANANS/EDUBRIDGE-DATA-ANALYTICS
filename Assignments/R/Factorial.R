i=1
fact=1
num1<-readline(prompt="Enter the number")
num1<-as.integer(num1)
while(i<=num1)
{
  fact=i*fact
  i=i+1
}
print(fact)