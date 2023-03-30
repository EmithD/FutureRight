#creating a min_max function
normalize <- function(x, max=1, min=0) 
{
    a= (((x-min(x))* (new_max-new_min))/(max(x)-min(x)))+new_min
    return(a)
}

#importing data set
data <- read.csv("E:\\STUDY\\SDGP\\Git Repository\\FutureRight\\FutureRight\\BackEnd\\Data\\PersonalityTest\\train.csv")

data
