print("Nguyen Van Thai","\nMSSV: 235752021610005")
class Nguoi(object):
    def getGender(self):
        return "Unknown";
class Nam(Nguoi):
    def getGender (self):
        return "Nam";
class Nu(Nguoi):
    def getGender (self):
        return "Nu";
aNam=Nam()
aNu=Nu()
print (aNam.getGender())
print (aNu.getGender())
