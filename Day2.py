#Q1)

a =  b = c =20
a = a/10
b = b*50
c = c+60

print("a= ", a)
print("b= ", b)
print("c= ", c)

print("\n\n")

#Q2)

# old_str = "PYTHON"
# new_str = list(old_str)

# new_str[2] = "G"

# Final = "".join(new_str)

# print(Final)

text = 'SAYUZ'
print(text)
text = text[:2] + 'G' + text[3:]

print("text after conversion: ")
print(text)

print("\n\n")


#Q3)

d = 2
e = 3.145

print("Before Converting \n",d,"\n",e)
d = float(d)
e = int(e)

print("After Converting \n",d,"\n",e)



OUTPUT:
[Running] python -u "c:\Users\SAYUZ\Desktop\Python-Internship\Day2.py"
a=  2.0
b=  1000
c=  80



SAYUZ
text after conversion: 
SAGUZ



Before Converting 
 2 
 3.145
After Converting 
 2.0 
 3

[Done] exited with code=0 in 0.332 seconds

