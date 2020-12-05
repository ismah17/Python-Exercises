string1="Ishani"
string2=" is"
string3=" learning"
string4=" python"
print(string1+ string2+ string3+ string4)
print("Ishani" " is" " learning" " python") #concatinate
print("hello" *5)
print("hello" *(5 +4))
print(5*"hello" "456")
print("my birthday is {}".format(20))
print("I bought a mechanical keyboard, wow factor is so high ")
print("Luci loves Ishani to the moon and back")
#string replcement #
age =  24
print("my age is " + str(age)+ " years")
print("my age is {}".format(age) + "years")
print("There are {0} days in {1},{2},{3},{4},{5},{6},{7}"
      .format(31, "JAN", "MAR", " MAY", "JULY", "AUG", "OCT", "NOV"))
print("These are the days of each month has Jan:{0}, Feb:{1}, Mar:{0}, Apr:{2}, May:{0}, June:{2}, July:{0}, Aug:{0}, Sep:{2}, Oct:{0}, Nov:{2}, Dec:{1}".format(31,28,30))
print()

print("""Jan:{0}
Feb:{1}
 Mar:{0}
  Apr:{2}
   May:{0}
    June:{2}
     July:{0}
      Aug:{0}
       Sep:{2}
        Oct:{0}
         Nov:{2}
          Dec:{1}""".format(31, 28, 30))
###string formatting###

for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
