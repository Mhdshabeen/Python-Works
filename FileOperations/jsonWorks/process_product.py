

from json import load

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\FileOperations\\jsonWorks\\product.json",encoding="UTF-8")

items=load(f)

# print(len(items))

# Q1 disply title of all products

item_names=[i.get('title') for i in items]

# Q2 select jewelery items from the list

item_in_jewelery_category=[i.get("title") for i in items if i.get("category")=="jewelery"]

# print(item_in_jewelery_category)

# Q3 product with price grater than 100

item_price_geaterthan_hundred=[i.get("title") for i in items if i.get("price")>100]

# print(item_price_geaterthan_hundred)

# Q4 items in range 100 to 150

item_in_range_100_t0_150=[i.get("title") for i in items if i.get("price")>=100 and i.get("price")<=300]

# print(item_in_range_100_t0_150)

# Q5 disply product having rating greater than 4.1

item_with_rating_4_1=[{"id":i.get("id"),"rating":i.get("rating").get("rate")} for i in items if i.get("rating").get("rate")>4.1]

# print(item_with_rating_4_1)

# Q5 product with most number of rating

def rating_count(dic):

    return dic.get("rating").get("count")

top_selling_product=max(items,key=rating_count)

print([top_selling_product.get("title"),top_selling_product.get("rating").get("count")])

