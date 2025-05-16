def grade(n):
if 90 <= n <= 100:
return 'A'
elif 80 <= n < 90:
return 'B'
elif 70 <= n < 80:
return 'C'
elif 60 <= n < 70:
return 'D'
else :
return 'F'
print(grade(89.9))
