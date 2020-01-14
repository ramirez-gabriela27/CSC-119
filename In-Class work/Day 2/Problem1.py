# R2.3 problem 1
#Variables are created for each variable in equation
sInitial = float(input ("Initial S:"))
vInitial = float(input ("Initial v:"))
t = float(input ("Time:"))
g = float(input ("g:"))
#Variables are then used in equation to solve for s
s = sInitial+(vInitial*t)+(.5*g*(t**2))
print("s=",s)

input()
        
