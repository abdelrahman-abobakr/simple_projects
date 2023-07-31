# second part   list   dictionnary set    tuple

dict={"name":{"first":"abdo","middle":"abobakr","last":"zaki"},
              "address":{"governorate":"minya","city":"maghagha","village":"dhmaro"},
              "birthdate":{"year":"2001","month":9,"day":14}}

print(dict)

(dict["birthdate"])["month"]=10
# it is the same as   dict["birthdate"]["month"]=10
(dict["birthdate"])["day"]=22

print(dict)