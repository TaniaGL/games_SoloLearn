#Popsicles:

siblings = int(input()) 
popsicles = int(input()) 

result = popsicles % siblings

if result == 0:
    print("give away")
else:
    print("eat them yourself")
