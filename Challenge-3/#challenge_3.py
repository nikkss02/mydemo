#challenge_3
def challenge_3 (arg1, arg2, seperator='/'):
    keys= arg2.split(seperator)
    value= arg1
    for key in keys:
        value= value[key]
    return value

object1= {"a":{"b":{"c":"d"}}}
key1= "a/b/c"
print(challenge_3(object1,key1))

object2= {"x":{"y":{"z":"a"}}}
key2= "x/y/z"
print(challenge_3(object2,key2))
