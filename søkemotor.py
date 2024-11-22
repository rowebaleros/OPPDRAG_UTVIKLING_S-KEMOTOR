# sørger for at det er mulig å lese innholdet fra txt-filen

def lesInnTekst(filnavn):
    try:
        with open(filnavn, "r", encoding="utf-8") as file:  # åpner filen
            return file.read()  # returnerer innholdet tilbake
    except FileNotFoundError:  # kode for om hvis tekstfilen finnes
        return f"'{filnavn}' not found."  # hvis txt-filen ikke finnes returnerer den tilbake en feilmelding


# Funksjon for å kunne søke etter spesifikke ord i tekstfilen

def sok_ord(lines, ord):
    results = []  # lagrer innholdet som har det spesifikke ordet i seg
    ord_count = 0  # teller hvor mange ganger ordet finnes i innholdet
    for line_number, line in enumerate(lines, start=1):  # går gjennom hver linje med et nummer
        if ord.lower() in line.lower():  # søker etter om det er i stor eller liten første bokstav
            results.append((line_number, line.strip()))  # lagrer linjenummer og tekst fra innholdet
            ord_count += line.lower().split().count(ord.lower())  # teller hvor mange ganger et ord oppstår i samme linje
    return results, ord_count  # returnerer tilbake hvor mange linjer og totalt antall ganger det ordet dukker opp


# Funksjon for å sjekke om ordet finnes i filen og returnere en melding

def printOrd(file_content, ord):
    if ord.lower() in file_content.lower():  # sjekker om ordet finnes i filen
        return f"'{ord}' exists in the text."  # printer ut denne teksten om ordet eksisterer i innholdet
    else:
        return f"'{ord}' not found in the text."  # printer ut denne teksten hvis ordet du leter etter ikke finnes i innholdet


# Hovedprogrammet

def main():
    textfile = input("What is your text file? ")  # ber brukieren om å oppgi tekstfil-navnet
    file_content = lesInnTekst(textfile)  # leser innholdet til filen
   

    if "not found" in file_content:  # hvis filen ikke finnes så printer den ut en feilmelding
        print(file_content)
    else:
        print("\nFile content successfully read.\n")  # godkjenner at filen har blitt lest
        lines = file_content.split("\n")  # splitter innholdet inn i linjer

        while True:  # kode så at man ikke bare blir kastet ut når man skriver et ord som ikke finnes i innholdet
            ord = input("What word do you want to find? (type 'exit' to quit): ") 
            if ord.lower() == "exit":  # Sjekker om brukeren vil stoppe programmet
                print("Exiting the program. Goodbye!")  # stopper programmet
                break

            search_results, ord_count = sok_ord(lines, ord)  # Søker etter ordet i linjene
            print(printOrd(file_content, ord))  # Viser om ordet finnes
            print(f"\nOccurrences: {ord_count}")  # Viser antall forekomster av ordet
            if search_results:  # Hvis ordet finnes i noen linjer
                print("\nLines containing the word:")  # Skriver ut linjene
                for line_number, line in search_results:
                    print(f"Line {line_number}: {line}")  # Viser linjenummer og tekst


# Kjører hovedprogrammet

if __name__ == "__main__":
    main()