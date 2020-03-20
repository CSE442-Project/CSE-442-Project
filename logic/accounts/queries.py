from accounts.models import ContractorProfile, Address

def getClosestContractors(){
    currentAddi = Address.object.get(pk=1)
    zipcode = currentAddi.zip
    print(zipcode.ContractorProfile_set.all()[:5])
}
