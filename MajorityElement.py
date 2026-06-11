def MajorityElement(lst1):


   num_count = {}
   list_len = len(lst1)

   #count the elements in the list and store the count of each element in a dictionary
   for num in lst1:

       num_count[num] = num_count.get(num,0) + 1

   #checks each element's count and returns if the element count is greater than half of the list length. Otherwise, it returns the dictionary value
   for num, count in num_count.items():

      if count > list_len // 2:

         return num

      else:

         return num_count

list1 = [2,2,1,2,3,3,3]
print(MajorityElement(list1))