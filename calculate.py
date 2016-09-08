import decimal
import math
import datetime
import sys

if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit()

mainData = []
personStats = []
totalStats = {}

#Main Debugging Switch
debug = 2

totalSum = decimal.Decimal(0)
totalCorrectSum = decimal.Decimal(0)
totalIncorrectSum = decimal.Decimal(0)
remainingIncorrectSum = decimal.Decimal(0)
houseWinnings = decimal.Decimal(0)
houseRoundingWinnings = decimal.Decimal(0)
finalHouseWinnings = decimal.Decimal(0)
    
personSum = [decimal.Decimal(0)] * len(mainData)
personCorrectSum = [decimal.Decimal(0)] * len(mainData)
personIncorrectSum = [decimal.Decimal(0)] * len(mainData)
personWinningPercentage = [decimal.Decimal(0)] * len(mainData)
personPreWinnings = [decimal.Decimal(0)] * len(mainData)
personNetGain = [decimal.Decimal(0)] * len(mainData)

def main():
    inputData()
    calculate()
    outputFile() 

def inputData():
    isAsking = True
    while isAsking:
        askingResponse = neat(input("Is there another person? (y,n) "), 1)
        if askingResponse == "y":
            personData = askPersonData()
            if debug:
                print(personData)
            mainData.append(personData)
        elif askingResponse == "n":
            isAsking = False
            if debug:
                print(mainData)
        else:
            print("Invalid response, please try again.")
            continue

def askPersonData():
    isFinished = False
    
    name = ""
    isCorrectQ1 = False
    isCorrectQ2 = False
    isCorrectQ3 = False
    isCorrectQ4 = False
    betQ1 = decimal.Decimal(0)
    betQ2 = decimal.Decimal(0)
    betQ3 = decimal.Decimal(0)
    betQ4 = decimal.Decimal(0)
    
    while isFinished == False:
        name = neat(input("Enter the name: "))
        
        tempCorrect1 = neat(input("Was question #1 correct? (y,n) "), 1)
        if tempCorrect1 == "y":
            isCorrectQ1 = True
        elif tempCorrect1 == "n":
            isCorrectQ1 = False
        else:
            print("Invalid response, please try again.")
            continue
        try:
            betQ1 = decimal.Decimal(input("What was the bet for question #1? "))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        tempCorrect2 = neat(input("Was question #2 correct? (y,n) "), 1)
        if tempCorrect2 == "y":
            isCorrectQ2 = True
        elif tempCorrect2 == "n":
            isCorrectQ2 = False
        else:
            print("Invalid response, please try again.")
            continue
        try:
            betQ2 = decimal.Decimal(input("What was the bet for question #2? "))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        tempCorrect3 = neat(input("Was question #3 correct? (y,n) "), 1)
        if tempCorrect3 == "y":
            isCorrectQ3 = True
        elif tempCorrect3 == "n":
            isCorrectQ3 = False
        else:
            print("Invalid response, please try again.")
            continue
        try:
            betQ3 = decimal.Decimal(input("What was the bet for question #3? "))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        tempCorrect4 = neat(input("Was question #4 correct? (y,n) "), 1)
        if tempCorrect4 == "y":
            isCorrectQ4 = True
        elif tempCorrect4 == "n":
            isCorrectQ4 = False
        else:
            print("Invalid response, please try again.")
            continue
        try:
            betQ4 = decimal.Decimal(input("What was the bet for question #4? "))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        isFinished = True

    personData = {
        "name":name,
        "isCorrectQ1":isCorrectQ1, "isCorrectQ2":isCorrectQ2,
        "isCorrectQ3":isCorrectQ3, "isCorrectQ4":isCorrectQ4,
        "betQ1":betQ1, "betQ2":betQ2, "betQ3":betQ3, "betQ4":betQ4
    }
    return personData

def calculate():
    global totalSum
    global totalCorrectSum
    global totalIncorrectSum
    global remainingIncorrectSum
    global houseWinnings
    global houseRoundingWinnings
    global finalHouseWinnings
    
    global personSum
    global personCorrectSum
    global personIncorrectSum
    global personWinningPercentage
    global personPreWinnings
    global personNetGain
    
    totalSum = decimal.Decimal(0)
    totalCorrectSum = decimal.Decimal(0)
    totalIncorrectSum = decimal.Decimal(0)
    remainingIncorrectSum = decimal.Decimal(0)
    houseWinnings = decimal.Decimal(0)
    houseRoundingWinnings = decimal.Decimal(0)
    finalHouseWinnings = decimal.Decimal(0)

    personSum = [decimal.Decimal(0)] * len(mainData)
    personCorrectSum = [decimal.Decimal(0)] * len(mainData)
    personIncorrectSum = [decimal.Decimal(0)] * len(mainData)
    personWinningPercentage = [decimal.Decimal(0)] * len(mainData)
    personPreWinnings = [decimal.Decimal(0)] * len(mainData)
    personNetGain = [decimal.Decimal(0)] * len(mainData)

    index = 0
    
    for person in mainData:
        for i in range(1, 5):
            if mainData[index].get("isCorrectQ%d" %i) == True:
                personCorrectSum[index] += mainData[index].get("betQ%d" %i)
                personSum[index] += mainData[index].get("betQ%d" %i)
            else:
                personIncorrectSum[index] += mainData[index].get("betQ%d" %i)
                personSum[index] += mainData[index].get("betQ%d" %i)
        index += 1

    for i in personSum:
        totalSum += i
    for i in personCorrectSum:
        totalCorrectSum += i
    for i in personIncorrectSum:
        totalIncorrectSum += i

    isHousePercentageComlpete = False
    while isHousePercentageComlpete == False:
        try:
            housePercentage = decimal.Decimal(input("What percentage will the house take? (decimal value) "))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        if housePercentage <= 1.0 and housePercentage >= 0.0:
            isHousePercentageComlpete = True
        else:
            print("The percentage nust be between 0.0 and 1.0")

    houseWinnings = housePercentage * totalIncorrectSum

    remainingIncorrectSum = totalIncorrectSum - houseWinnings

    index = 0
    for person in mainData:
        if personCorrectSum[index] == decimal.Decimal(0):
            personWinningPercentage[index] = 0
            personPreWinnings[index] = 0
        else:
            personWinningPercentage[index] = (personCorrectSum[index] / totalCorrectSum)
            personPreWinnings[index] = decimal.Decimal(str(math.floor(float(str((((personCorrectSum[index] / totalCorrectSum) * \
            remainingIncorrectSum)*100))))))/100
        personNetGain[index] = personPreWinnings[index] - personIncorrectSum[index]
        index += 1

    preWinningSum = 0
    for personWinnings in personPreWinnings:
        preWinningSum += personWinnings
    houseRoundingWinnings = remainingIncorrectSum - preWinningSum

    finalHouseWinnings = houseWinnings + houseRoundingWinnings

    if debug:
        print("totalSum = %s" %totalSum)
        print("totalCorrectSum = %s" %totalCorrectSum)
        print("totalIncorrectSum = %s" %totalIncorrectSum)
        print("remainingIncorrectSum = %s" %remainingIncorrectSum)
        print("houseWinnings = %s" %houseWinnings)
        print("houseRoundingWinnings = %s" %houseRoundingWinnings)
        print("finalHouseWinnings = %s" %finalHouseWinnings)
        print("personSum = %s" %personSum)
        print("personCorrectSum = %s" %personCorrectSum)
        print("personIncorrectSum = %s" %personIncorrectSum)
        print("personWinningPercentage = %s" %personWinningPercentage)
        print("personPreWinnings = %s" %personPreWinnings)
        print("personNetGain = %s" %personNetGain)

def outputFile():
    today = datetime.date.today
    f = open("result.txt", "w")
    
    text = " _____     _       _       ____       _   \n" \
        "|_   _| __(_)_   _(_) __ _| __ )  ___| |_ \n" \
        "  | || '__| \ \ / / |/ _` |  _ \ / _ \ __|\n" \
        "  | || |  | |\ V /| | (_| | |_) |  __/ |_ \n" \
        "  |_||_|  |_| \_/ |_|\__,_|____/ \___|\__|\n\n" \
        "Input Data:\n" \
        "+----------+-------------+-------------+-------------+-------------+\n"

    index = 0
    for i in mainData:
        text += "|{0:10}|{1:5} ${2:6.6}|{3:5} ${4:6.6}|{5:5} ${6:6.6}|{7:5} ${8:6.6}|\n" \
            "+----------+-------------+-------------+-------------+-------------+\n".format(
            mainData[index]["name"], \
            ("Right" if mainData[index]["isCorrectQ1"] == True else "Wrong"), str(mainData[index]["betQ1"]), \
            ("Right" if mainData[index]["isCorrectQ2"] == True else "Wrong"), str(mainData[index]["betQ2"]), \
            ("Right" if mainData[index]["isCorrectQ3"] == True else "Wrong"), str(mainData[index]["betQ3"]), \
            ("Right" if mainData[index]["isCorrectQ4"] == True else "Wrong"), str(mainData[index]["betQ4"])
        )
        index += 1
    
    text += "\nBasic Information:\n" \
        " {:24}: {:8.8}\n {:24}: {:8.8}\n {:24}: {:8.8}\n {:24}: {:8.8}\n {:24}: {:8.8}\n {:24}: {:8.8}\n {:24}: {:8.8}\n\n".format(
        "Sum of all bets", str(totalSum),
        "Sum of correct bets", str(totalCorrectSum),
        "Sum of incorrect bets", str(totalIncorrectSum),
        "House winnings", str(houseWinnings),
        "Remaining incorrect bets", str(remainingIncorrectSum),
        "Rounding house winnings", str(houseRoundingWinnings),
        "Final house winnings", str(finalHouseWinnings),
    )

    text += "Complex Player Data:\n" \
        " Name : Sum : RightSum : WrongSum : Percentage : Winnings : NetGain\n" \
        "+----------+-------+-------+-------+-------+-------++-------+\n"

    index = 0
    for i in mainData:
        text += "|{0:10.10}|{1:<6.6} |{2:<6.6} |{3:<6.6} |{4:<6.3} |{5:<6.6} |{6:<+6.6} |\n" \
        "+----------+-------+-------+-------+-------+-------+-------+\n".format(
            str(mainData[index]["name"]), \
            float(str(personSum[index])), \
            float(str(personCorrectSum[index])), \
            float(str(personIncorrectSum[index])), \
            float(str(personWinningPercentage[index])), \
            float(str(personPreWinnings[index])), \
            float(str(personNetGain[index])), \
        )
        index += 1

    if debug == 2:
        print(text)

    f.write(text)
    f.close()


def neat(input, isLower = False):
    if isLower:
        return str(input).strip().lower()
    else:
        return str(input).strip()

if __name__ == "__main__":
    main()