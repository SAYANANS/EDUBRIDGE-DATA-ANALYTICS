BS<-readline(prompt="Enter the basic salary")
BS<-as.integer(BS)
HRA<-0.1*BS
DA<-0.05*BS
PF<-0.04*BS
Netsalary<-(BS+HRA+DA)-PF
print(paste("Net Salary is",Netsalary))