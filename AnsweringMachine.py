from PhoneDatabase import PhoneDatabase
from Recording import Recording
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Dial
import random

global randVar
global randInt
randVar = 0
randInt = 0

def IDLE():
    r = Recording()
    usrInput = 0

    while(usrInput != 3):
        print('What action would you like to take')
        print('1: Check Message box (' + str(len(r.recordings)) + ' Messages) ('  + str(r.getNewMessages()) + ' New Messages)')
        print('2: Quit')

        usrInput = input('Input an integer in the range given above')

        if(usrInput == '1'):
            messageInbox(r)
        elif(usrInput == '2'):
            return
        else:
            print('not a valid input')

        print()

app = Flask(__name__)

randVar = 0

@app.route("/voice", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    phoneDB = PhoneDatabase()
    number = request.form['From']
    global randVar
    global randInt

    resp = VoiceResponse()

    if randVar == 0:
        randInt = random.randint(1000, 9999)
        randVar = randInt
    else:
        randVar = randInt
        randInt = random.randint(1000, 9999)

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']
        if(choice == str(randVar)):
            # <Say> a different message depending on the caller's choice
            if(phoneDB.isPhoneNumberBlocked(number) == True):
                resp.say('Your phone number is blocked, please do not call back')
                return str(resp)
            if(phoneDB.isWhiteOrBlack() == 'black'):
                if (phoneDB.isNumberInBlackList(number) == True):
                    resp.say('You have reached the voicemail machine, leave a message after the beep')
                    resp.record(timeout=15, play_beep=True, transcribe=True)
                    return str(resp)
                elif (phoneDB.isNumberInBlackList(number) == False):
                    dial = Dial(caller_id = str(number))
                    dial.number(phoneDB.forwardNumber)
                    resp.append(dial)
                    return str(resp)
                else:
                    resp.say("Sorry, I don't understand that choice.")
            elif(phoneDB.isWhiteOrBlack() == 'white'):
                if (phoneDB.isNumberInWhiteList(number) == True):
                    dial = Dial(caller_id=str(number))
                    dial.number(phoneDB.forwardNumber)
                    resp.append(dial)
                    return str(resp)
                elif (phoneDB.isNumberInWhiteList(number) == False):
                    resp.say('You have reached the voicemail machine, leave a message after the beep')
                    resp.record(timeout=15, play_beep=True, transcribe=True)
                    return str(resp)
                else:
                    resp.say("Sorry, I don't understand that choice.")
        else:
            resp.say('The numbers entered were incorrect, try again')

    # Start our <Gather> verb
    gather = Gather(num_digits=4)
    gather.say('Enter ' + str(randInt) + ' to continue')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)

def messageInbox(r):
    validInput = False
    while(validInput == False):
        print('What would you like to do?')
        print('1: Display the messages')
        print('2: Delete a message')
        print('Otherwise, type e to exit')
        index = input()
        if(index == '1'):
            validInput = True
            r.displayMessages()
        elif(index == '2'):
            validInput = True
            r.deleteRecording()
        elif(index == 'e'):
            return
        else:
            print('The value chosen is not valid, choose again')



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
    #IDLE()
