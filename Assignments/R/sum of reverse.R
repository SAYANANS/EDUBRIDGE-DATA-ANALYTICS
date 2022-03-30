n<-readline(prompt="Enter the number")
n<-as.integer(n)
sum = 0
while (n > 0) 
{
  sum=sum+n%%10
  n=as.integer(n/10)
}

print(sum)