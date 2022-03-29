x<-readline(prompt="enter first num")
y<-readline(prompt="enter second num")
x<-as.integer(x)
y<-as.integer(y)
temp<-x
x<-y
y<-temp
print(paste("swap =",x,y))