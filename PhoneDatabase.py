import pymysql

class PhoneDatabase:

    def __init__(self):
        self.db = pymysql.connect("localhost", "guest", "1234", "numbers")
        self.cursor = self.db.cursor()
        self.cursor.execute("Select * from fwdnum")
        ans = self.cursor.fetchall()
        for i in ans:
            self.forwardNumber = '+1' + i[0]
            print(forwardNumber)

    def isPhoneNumberBlocked(self, phoneNumber):
        ishere = False
        self.cursor.execute("Select * from blocklist")
        ans = self.cursor.fetchall()
        for i in ans:
            for num in range(0, len(i)):
                phoneNumber = str(phoneNumber).replace('+', "")
                if(phoneNumber == i[num]):
                    ishere = True
        if(ishere == True):
            return True
        else:
            return False

    def isNumberInWhiteList(self, phoneNumber):
        ishere = False
        self.cursor.execute("Select * from whitelist")
        ans = self.cursor.fetchall()
        for i in ans:
            for num in range(0, len(i)):
                phoneNumber = str(phoneNumber).replace('+', "")
                if (phoneNumber == i[num]):
                    ishere = True
        if(ishere == True):
            return True
        else:
            return False

    def isNumberInBlackList(self, phoneNumber):
        ishere = False
        self.cursor.execute("Select * from blacklist")
        ans = self.cursor.fetchall()
        for i in ans:
            for num in range(0, len(i)):
                phoneNumber = str(phoneNumber).replace('+', "")
                if (phoneNumber == i[num]):
                    ishere = True
        if (ishere == True):
            return True
        else:
            return False

    def isWhiteOrBlack(self):
        self.cursor.execute(("select * from toggle limit 1"))
        ans = self.cursor.fetchall()

        for i in ans:
            for num in range(0, len(i)):
                return i[num]

    def getForwardingNumber(self):
        self.cursor.execute("select * from forwardingNumber")
        ans = self.cursor.fetchall()
        for i in ans:
		return '+' + i[0]
	
