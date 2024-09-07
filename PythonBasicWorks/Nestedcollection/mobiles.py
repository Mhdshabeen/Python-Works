


mobiles=[
    {"id":100,"model":"iphone 11","brand":"apple","price":35000,"network":"5g"},
    {"id":101,"model":"iphone 12","brand":"apple","price":45000,"network":"4g"},
    {"id":102,"model":"iphone 13","brand":"apple","price":25000,"network":"5g"},
    {"id":103,"model":"s23 ultrs","brand":"samsung","price":30000,"network":"4g"},
    {"id":104,"model":"s21","brand":"samsung","price":23000,"network":"5g"},
    {"id":105,"model":"s22","brand":"samsung","price":50000,"network":"5g"},
    {"id":106,"model":"moto edge 5","brand":"motrola","price":38000,"network":"3g"},
    {"id":107,"model":"y9100","brand":"vivo","price":9000,"network":"4g"},
    {"id":108,"model":"y2000","brand":"vivo","price":12000,"network":"5g"},
    {"id":109,"model":"redmi note10 pro","brand":"xeiomi","price":18000,"network":"5g"}
    ]

# print all mobile models

mobile_name=[dicts.get("model") for dicts in mobiles]

# print(mobile_name)

# print all mobile brands

brands={mob.get("brand") for mob in mobiles}

# print(brands)

# print samsung mobile names

samsung_mobile_models=[mob.get("model") for mob in mobiles if mob.get("brand")=="samsung"]

# print(samsung_mobile_models)

# print all mobiles availablr in range of 20k to 40k

phone_in_price_range=[mob.get("model") for mob in mobiles if mob.get("price") in range(20000,40001)]

# print(phone_in_price_range)

# print name of costly mobile phone

cost=0

for mob in mobiles:

    if mob.get("price")>cost:

        cost=mob.get("price")

costly_mobile=[mob.get("model") for mob in mobiles if mob.get("price")==cost]

# print(costly_mobile)

# print(cost)

# def get_price(mob):

#     return mob.get("price")

costly_mobiles=max(mobiles,key=lambda mob:mob.get("price"))

# costly_mobiles=

# print(costly_mobiles)

mincost_mobile=min(mobiles,key=lambda mob:mob.get("price"))

# print(mincost_mobile)

# sort mobiles in order of their price increasing and decreing

def get_price(mob):

    return mob.get("price")

sorted_assending=sorted(mobiles,key=get_price)

# for mob in sorted_assending:

    # print(mob.get("model"), "=" ,mob.get("price"))

# print(sorted_assending)

# total sum of mobile price


total=sum([mob.get("price") for mob in mobiles])

print(total)