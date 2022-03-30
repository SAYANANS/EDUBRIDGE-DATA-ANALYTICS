a=0
b=1
print(a)
print(b)
n<-readline(prompt="Enter the number")
n<-as.integer(n)
i=1
while(i<=n)
{
  f=a+b
  print(f)
  a=b
  b=f
  i=i+1
}