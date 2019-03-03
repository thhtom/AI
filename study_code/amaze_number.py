def amaze_number (n):
   all_list = []
   while n%2==0:
         n=n/2
         all_list.append(2)
   while n%3==0:
         n=n/3
         all_list.append(3)
   while n%5==0:
         n=n/5
         all_list.append(5)
   if n==1:
       return all_list
   else:
       return None
print amaze_number(1845281250)
print amaze_number(3690562500)
print amaze_number(1230187500)
print amaze_number(10023750)
