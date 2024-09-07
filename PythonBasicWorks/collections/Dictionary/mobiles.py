# WAP to create a dict with keys names,brand,price,is_available



mobile={"names":"iphone13","brand":"apple","price":50000,"is_avilable":True,"offer":1500}

# print mobile name
#use get(key) method

print(mobile.get("names"))

print(mobile.get("price"))

print(mobile["is_avilable"])

# keys() retrn all valid keys

#print(mobile.keys())

# values() return all values

#print(mobile.values())
# items() return all key value pairs

#for k,v in mobile.items():
    #print(k,v)


#mobile.get("names")

# pop(key) remove thus key value pair

#removed=mobile.pop("names")



#print(removed)

# add a key value pair to dict
# add offer 500 

# mobile["offer"]=500

# print(mobile)

# chek weather a key exist or not
# syntax = "key" in dic name

print("present" if "names" in mobile else "not present")

# selling price

if "offer" in mobile:

    selling_price=mobile["price"]-mobile["offer"]

else:

    selling_price=mobile["price"]

print(selling_price)