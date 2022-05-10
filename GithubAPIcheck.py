import string, random, requests, json, time

def generateUser():

    thefile = open("wordlist", "r")
    wlist = thefile.read().split("\n")

    while True:
        theword = random.choice(wlist)
        thelength = len(theword)
        if 4 < thelength < 25: #determines the length of the word (5-24 letters)
            return theword
            break

while True:
        user = generateUser()
        try:
                jsonData = json.loads(
                        requests.get(f"https://api.github.com/users/{user}").text
                        )
                print (jsonData['login'] + ' exists')
        except Exception as e:
                print (f'User: {user}, does not exist\n')
                exit()
