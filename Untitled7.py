#!/usr/bin/env python
# coding: utf-8

# # Quizz 3
# 

# ## 3°E
# ### Alvarez Vazquez
# ### Cruz Sierra
# ### Mireles Rebollar
# ### Reyes Gomez

# In[13]:


values = int(input( "how much data do you want to introduce? "))
X=[]
Y=[]

totalx = 0
totaly = 0

for i in range(0, values):
    a = int(input("Introduce x: "))
    X.append(a)
    totalx +=a
print("This is your X :")
for x in X:
    print(x, end = ' ')
    
    
for i in range(0, values):
    b = int(input("Introduce y: "))
    Y.append(b)
    totaly +=b
print("This is your Y:")
    
for y in Y:
    print(y, end = ' ')  
    
for i in range(0,values):
    totalX2 += a^2 
    totalxy += a*b
    
B1 =(((values*(totalxy^2))-(totalx*totaly))/(values*(totalX2)-((totalx)^2)))    

B0 = ((totaly-(B1*totalx))/values)

print(f"y= {B1}x+{B0}")
    
 

