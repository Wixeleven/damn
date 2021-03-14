# Spēles apraksts
# Autors
# Datums, vieta

# Importē random libary
# Importē math libary


def game_function():
    # User input skailtim no kura(min) līdz kuram(max) tiks izvēlēts nejaušs skaitlis, kas jāuzmin
    # Ievadi attiecīgu tekstu, lai lietotājs saprot, ka lower ir min un upper max
    lower = int(input(":- "))
    upper = int(input(":- "))

    # Tiek nejauši izvēlēts random skaitlis no lietotāja izvēlētā apgabala, kas būs skaitlis, kas jāuzmin
    # __________ vietā ieraksti vajadzīgo library
    x = _______.randint(lower, upper)

    #Attiecīgi norādītajam apgabalam tiek izrēķināts atbilstošs mēģinājumu skaits
    print("\n\tTev ir tikai ", round(math.log(upper - lower + 1, 2)),
      " mēģinājumi uzminēt skaitli!\n")

    # Skaitītājs minējumiem.
    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Uzmini skaitli:- "))
        # __ ievadi ar kuru mainīgo tiks salīdzināts guess
        if __ == guess:
            print("Apsveicu, Tu uzvarēji ar ",count, " mēģinājumiem")
            break
        elif  __ > guess:
            print("Tavs minējums ir pārāk mazs!")
        elif __ < guess:
            print("Tavs minējums ir pārāk liels!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nSkaitlis ir%d" % x)
        print("\tVēlu veiksmi nākamreiz")
    
    return 0

def welcome_text(text):
    print(f'Hi, {text}')
    # Izsauc game_function, funkcijai nav jānorāda nekādi parametri

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Izsauc welcome_text funkciju un parametros norādi izprintējamo tekstu
