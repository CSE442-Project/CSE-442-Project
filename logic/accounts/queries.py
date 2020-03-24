from . import models

def getClosestContractors():
    address = Address.objects.get(pk=1).values('zip')
    contractors = ContractorProfile.objects.values('user', 'zip')
    output = []
    count = 0
    for e in contractors:
        if e["zip"] == address["zip"] and count < 5:
            output.append(e)
            count = count + 1
    return output

def printContractors():
    toPrint = getClosestContractors()
    if len(p) == 0:
        print("Sorry, there are no available contractors in your area.")
    else:
        for p in toPrint:
            print(p + '\n')
