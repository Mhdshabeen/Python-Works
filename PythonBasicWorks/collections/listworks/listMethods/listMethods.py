# class list:

    # def append(value)      #add new element to end of list

def is_append(list,value):


    list=[1,2,3,4,5]

    list.append(value) 

    return list #[1, 2, 3, 4, 5]

#print(is_append(list,5))

#====================================================================================================================================


    #def insert(index,value)   # used to add element at a given position

def is_insert(list,index,value):

    list=[1,2,3,4,5]

    list.insert(index,value)

    return list #[1, 2, 2.5, 3, 4, 5]

#print(is_insert(list,2,2.5))


#====================================================================================================================================


    # def count()   return the count of a specific element in list

def is_count(list,element):

    list=[1,2,3,3,4,3,5]

    return list.count(element)

# print(is_count(list,3))


#======================================================================================================================================


    #def pop() or def pop(index)    default it remove and return last element from the list or remove and return element from the given index

def is_pop(list,index):

    list=[1,2,3,6,4,8]

    return list.pop(index)

#print(is_pop(list,1)) #1


#=====================================================================================================================================


    # def remove(element)   remove the first occurance element from the list and return entire list

def is_remove(list,value):

    list=[2,4,1,5]

    list.remove(value)

    return list #[4, 1, 5]

#print(is_remove(list,2))


#===================================================================================================================================


    # def reverse()  

def is_reverse(list):

    list=[1,2,3,4]

    list.reverse()

    return list #[4, 3, 2, 1]

#print(is_reverse(list))


#===================================================================================================================================
    

    # def extend([collection of elements])  extend current list by given list elements

def is_extend(list,newlist):

    list=[1,2,3,4,5]

    list.extend(newlist)

    return list #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#print(is_extend(list,[1,2,3,4,5]))


#====================================================================================================================================


    # def copy() return list to new variable



#====================================================================================================================================

    # def sort() default it sort assending . if we give reverse=true then it sort desendingly

# list=[1,9,2,8,3,7,4,6,5]

# list.sort(reverse=True)

# print(list)






