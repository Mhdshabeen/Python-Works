# WAP with dic of key emp name,emp id, dept,salary,combo offer
# print all the keys in employee dict
#print all the values in emp dict
# print all the key value pairs in employee dict
# add extra working day to dic
#chk if the dict contain key extra working days



emplyee={"name":"hari",
         "id":"AME20CS016",
         "dept":"r&d",
         "salary":50000,
         "combo offer":1000
         }

# print all the keys in employee dict

all_keys=emplyee.keys()

#print all the values in emp dict

all_values=emplyee.values()

# print all the key value pairs in employee dict

for k,v in emplyee.items():

    print(k,v)

# add extra working day to dic

emplyee["extra_working"]=5


#chk if the dict contain key extra working days

if "extra_working" in emplyee:

    print("present")

else:

    print("not present")

# clculate the net pay of the person if ectra working day present

if "extra_working" in emplyee:

    net_pay=emplyee.get("salary") + (emplyee.get("extra_working")*emplyee.get("combo offer"))

    print(net_pay)

else:

    net_pay=emplyee.get("salary")

    print(net_pay)
