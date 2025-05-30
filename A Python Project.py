# Kaun Banega Crorepati Game
l=["1)Who is the god of cricket?\na)Sachin\nb)Kohli","2)The king of Cricket is-\na)Unmukt Chand\nb)Virat Kohli"]
a=["a","b"]
b=["a","b"]
print(l[0])
ans=input("Enter your correct option:")
if(ans==(a[0])):
    print("Correct and you get 20rs")
else:
    print("Incorrect")
print(l[1])
ans1=input("Enter your correct option:")
if(ans1==(b[1])):
    print("Correct and you get 20rs")
else:
    print("Incorrect")

if(ans==(a[0]) and  ans1==(b[1])):
    print("You total earn 40rs")
elif(ans==(a[0])):
    print("You only get 20 rs ")
elif(ans1==(b[1])):
    print("You only get 20 rs ")
else:
    print("You won nothing.Better luck next time!")