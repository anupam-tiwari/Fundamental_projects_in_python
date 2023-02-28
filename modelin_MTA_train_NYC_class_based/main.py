class Turnstill: 
    def __init__(self,location,direction,type_of,db):
        self.location = location
        self.direction = direction
        self.type = type_of
        self.db = db
    
    def pay(self,serial_num): 
        temp = self.db.get(serial_num,0)
        if temp: 
            if self.db[serial_num]["balance"] > 3: 
                self.db[serial_num]["balance"] = self.db[serial_num]["balance"] - 3
                self.db[serial_num]["trips"] = self.db[serial_num]["trips"] + 1
        return self.db[serial_num]["balance"]

    def sendStatus(self): 
        return self
    

#db = {"#101010":{"balance":500,"trips":10}}
db = {"0x101":{"balance":500,"trips":10}}
t1 = Turnstill("bayridge","multi","below_waits",db)
print(t1.pay("0x101"))

#
