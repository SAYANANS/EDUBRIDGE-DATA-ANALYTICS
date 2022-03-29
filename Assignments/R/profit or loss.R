expense<-readline(prompt ="enter the expense")
income<-readline(prompt = "enter the income")
expense<-as.integer(expense)
income<-as.integer(income)
if(expense>income)
{
  print("loss")
}else{
  print("profit")
}