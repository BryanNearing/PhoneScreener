import pymysql
import PhoneDatabase as PhoneDatabase

def main():
    db = pymysql.connect("localhost","bryan", "1234","numbers" )
    cursor = db.cursor()
    runProgram(cursor, db);
    db.close()



def runProgram(cursor, db):
    usrInput = 0
    while (usrInput != 6):
        print('What action would you like to take')
        print('1: Edit the phone number database')
        print('2: Change the Whitelist/Blacklist toggle')
        print('3: See what mode you are in')
        print('4: Quit')

        usrInput = input('Input an integer in the range given above')

        if (usrInput == '1'):
            editLists(cursor, db)
        elif (usrInput == '2'):
            toggle(cursor, db)
        elif (usrInput == '3'):
            getMode(cursor)
        elif (usrInput == '4'):
            return
        else:
            print('not a valid input')

        print()

def toggle(cursor, db):
    cursor.execute("select * from toggle")
    ans = cursor.fetchall()

    for i in ans:
        for num in range(0, len(i)):
            if(i[num] == 'black'):
                cursor.execute("update toggle set toggle = 'white'")
                db.commit()
            elif(i[num] == 'white'):
                cursor.execute("update toggle set toggle = 'black'")
                db.commit()

def printLists(cursor):
    cursor.execute("show tables")
    for x in cursor:
        print(x)

def editLists(cursor, db):
    usrInput = 0
    while(usrInput != 3):
        print('What would you like to do')
        print('1: Delete a value from the lists')
        print('2: Add a value to the lists')
        print('3: Exit')

        usrInput = input()
        if(usrInput == '1'):
            deleteValue(cursor, db)
        elif(usrInput == '2'):
            addValue(cursor, db)
        elif(usrInput == '3'):
            return
        else:
            print('The value entered was not correct, only values 1-3 are accepted')

def deleteValue(cursor, db):
    usrInput = 0
    print('What list would you like to delete a number from?')
    while(usrInput != '4'):
        print('1: The BlockList')
        print('2: The BlackList')
        print('3: The WhiteList')
        print('4: Exit')

        usrInput = input()

        if(usrInput == '1'):
            deleteFromBlock(cursor, db)
        elif(usrInput == '2'):
            deleteFromBlack(cursor, db)
        elif(usrInput == '3'):
            deleteFromWhite(cursor, db)
        elif(usrInput == '4'):
            return
        else:
            print('The value entered was not correct, only values 1-4 are accepted')

def deleteFromBlock(cursor, db):
    print('What number would you like to delete (Do not input the + sign)')
    cursor.execute("SELECT * FROM blocklist")
    ans = cursor.fetchall()

    for i in ans:
        for num in range(0, len(i)):
            print(str(num + 1) + ': +' + i[num])


    usrInput = input()

    if(len(usrInput) > 11 or len(usrInput) < 11):
        print('This was not a valid number')
    else:
        statement = "delete from blocklist where number = " + usrInput
        cursor.execute(statement)
        db.commit()

def deleteFromBlack(cursor, db):
    print('What number would you like to delete (Do not input the + sign)')
    cursor.execute("SELECT * FROM blacklist")
    ans = cursor.fetchall()

    for i in ans:
        for num in range(0, len(i)):
            print(str(num + 1) + ': +' + i[num])

    usrInput = input()

    if (len(usrInput) > 11 or len(usrInput) < 11):
        print('This was not a valid number')
    else:
        statement = "delete from blacklist where number = " + usrInput
        cursor.execute(statement)
        db.commit()

def deleteFromWhite(cursor, db):
    print('What number would you like to delete (Do not input the + sign)')
    cursor.execute("SELECT * FROM whitelist")
    ans = cursor.fetchall()

    for i in ans:
        for num in range(0, len(i)):
            print(str(num + 1) + ': +' + i[num])

    usrInput = input()

    if (len(usrInput) > 11 or len(usrInput) < 11):
        print('This was not a valid number')
    else:
        statement = "delete from whitelist where number = " + usrInput
        cursor.execute(statement)
        db.commit()

def addValue(cursor, db):
    usrInput = 0
    print('What list would you like to add to?')
    while(usrInput != '4'):
        print('1: The BlockList')
        print('2: The BlackList')
        print('3: The WhiteList')
        print('4: Exit')

        usrInput = input()

        if(usrInput == '1'):
            addToBlock(cursor, db)
        elif(usrInput == '2'):
            addToBlack(cursor, db)
        elif(usrInput == '3'):
            addToWhite(cursor, db)
        elif(usrInput == '4'):
            return
        else:
            print('The value entered was not correct, only values 1-4 are accepted')

def addToBlock(cursor, db):
    number = input('What number would you like to add')
    if (len(number) > 10 or len(number) < 10):
        print('This is not a valid phone number')
    else:
        number = "+1" + number
        statement = 'Insert into blocklist (number) values (' + number + ')'
        cursor.execute(statement)
        db.commit()

def addToBlack(cursor, db):
    number = input('What number would you like to add')
    if (len(number) > 10 or len(number) < 10):
        print('This is not a valid phone number')
    else:
        number = "+1" + number
        statement = 'Insert into blacklist (number) values (' + number + ')'
        cursor.execute(statement)
        db.commit()

def addToWhite(cursor, db):
    number = input('What number would you like to add')
    if(len(number) > 10 or len(number) < 10):
        print('This is not a valid phone number')
    else:
        number = "+1" + number
        statement = 'Insert into whitelist (number) values (' + number + ')'
        cursor.execute(statement)
        db.commit()


def getMode(cursor):
    cursor.execute("select * from toggle")
    ans = cursor.fetchall()

    for i in ans:
        for num in range(0, len(i)):
            print("You are in " + i[0] + 'list mode')


if __name__ == '__main__':
     main()
