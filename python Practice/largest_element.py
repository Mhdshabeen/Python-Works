# Python program to print the largest element in an array


arry1=[2,6.37,68,14,79,36.85,103,67,93,83]
arry2=["afav","ddfh","suhdusfu","sdfhudgbuh","absdgsdgyfb","asdnsdhb"]

print("maximum of integer:>",max(arry1))

print("maximum of string:> ", max(arry2,key= lambda w:len(w)),len(max(arry2,key= lambda w:len(w))))