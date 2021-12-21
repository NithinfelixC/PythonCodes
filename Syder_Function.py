# Create a Function in Python, we use def and define the funtion with a name and tag a variable if needed.

def Full_Name(name):
    print("Nithin"+' '+name)

Full_Name("Felix")

# We can also create function using integers or calcuations and call that function

def AddNumber(a,b):
    X = a+b
    print(X)
    
AddNumber(382, 932)


# If we have a scenario where the overall Class grades of sections A to B are as follows. And we need to find the Average of a Standard/Class Year. So we can use the def function to create an automated formula to keep running the calucations automatically.

Class_Average_12A = 78
Class_Average_12B = 74
Class_Average_12C = 88
Class_Average_12D = 92
Class_Average_12E = 70
Class_Average_12F = 64 
Class_Average = (78,74,88,92,70,64)


def Average(Class_Average):
    Class_Average = (78,74,88,92,70,64)
    X=sum(Class_Average)/len(Class_Average)
    print(X)

Average(Class_Average)


#Creating another function 

def Analysis(d):
    Best_Climate = 45
    Y = 'Go outside'
    N = 'Do not go outside'
    if d>Best_Climate:
        print(Y)
    else:
        print(N)

Analysis(35)