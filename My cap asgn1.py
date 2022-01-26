R= float(1.1)
Pi=3.14
area= Pi*R*R
a=("the area of the circle with the radius {} is : %.4f" %area )
print(a.format(R))


#File name 
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
