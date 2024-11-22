# Sørger for at det er mulig å lese innholdet fra tekstfilen
def lesInnTekst(filnavn):
    try:
        with open(filnavn, "r", encoding="utf-8") as file:  # Åpner filen
            return file.read()  # Returnerer innholdet
    except FileNotFoundError:  # Håndterer feil hvis filen ikke finnes
        return f"'{filnavn}' not found."  # Returnerer en feilmelding

# Funksjon for å kunne søke etter spesifikke ord i tekstfilen
def sok_ord(lines, ord):
    results = []  # Lagrer linjene som inneholder ordet
    ord_count = 0  # Teller hvor mange ganger ordet finnes
    for line_number, line in enumerate(lines, start=1):  # Går gjennom hver linje med et nummer
        if ord.lower() in line.lower():  # Søker uavhengig av store/små bokstaver
            results.append((line_number, line.strip()))  # Lagrer linjenummer og tekst
            ord_count += line.lower().split().count(ord.lower())  # Teller hvor mange ganger ordet oppstår i linjen
    return results, ord_count  # Returnerer linjene og totalt antall ganger ordet dukker opp

# Funksjon for å sjekke om ordet finnes i filen og returnere en melding
def printOrd(file_content, ord):
    if ord.lower() in file_content.lower():  # Sjekker om ordet finnes i teksten
        return f"'{ord}' exists in the text."  # Returnerer melding hvis ordet finnes
    else:
        return f"'{ord}' not found in the text."  # Returnerer melding hvis ordet ikke finnes

# Hovedprogram
def main():
    textfile = input("What is your text file? ")  # Ber brukeren oppgi tekstfilnavn
    file_content = lesInnTekst(textfile)  # Leser innholdet i filen
    print(file_content)  # Viser filens innhold

    if "not found" in file_content:  # Hvis filen ikke finnes
        print(file_content)  # Viser feilmelding
    else:
        print("\nFile content successfully read.\n")  # Bekrefter at filen er lest
        lines = file_content.split("\n")  # Deler innholdet inn i linjer

        while True:  # **Ny løkke for flere søk**
            ord = input("What word do you want to find? (type 'exit' to quit): ")  # **"exit"-kommando for å avslutte**
            if ord.lower() == "exit":  # **Sjekker om brukeren vil avslutte**
                print("Exiting the program. Goodbye!")  # **Avslutter programmet**
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