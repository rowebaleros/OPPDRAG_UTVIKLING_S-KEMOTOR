# sørger for at det er mulig å lese innholdet fra txt-filen

def lesInnTekst(filnavn):
    try:
        with open(filnavn, "r", encoding="utf-8") as file:  # åpner filen
            return file.read() # returnerer innholdet tilbake
    except FileNotFoundError: # kode for om hvis tekstfilen finnes
        return f"'{filnavn}' not found." # hvis txt-filen ikke finnes returnerer den tilbake en feilmelding
 
# funksjon for å kunne søke etter spesifikke ord i tekstfilen

def sok_ord(lines, ord):
    results = [] # lagrer innholdet som har det spesifikke ordet i seg
    ord_count = 0 # teller hvor mange ganger ordet finnes i innholdet
    for line_number, line in enumerate(lines, start=1): # går gjennom hver linje med et nummer
        if ord.lower() in line.lower():  # søker etter om det er i stor eller liten første bokstav
            results.append((line_number, line.strip())) # lagrer linjenummer og tekst fra innholdet
            ord_count += line.lower().split().count(ord.lower())  # teller hvor mange ganger et ord oppstår i samme linje
    return results, ord_count # returnerer tilbake hvor mange linjer og totalt antall ganger det ordet dukker opp

# kode for å skrive ut om ordet finnes i tekstfilen
 
def printOrd(file_content, ord):
    if ord.lower() in file_content.lower():  # Sjekker om ordet finnes i filen
        return f"'{ord}' exists in the text." # printer ut denne teksten om ordet eksisterer i innholdet
    else:
        return f"'{ord}' not found in the text." # printer ut denne teksten hvis ordet du leter etter ikke eksisterer i innholdet
 
# Hovedprogram
textfile = input("What is your text file? ")
file_content = lesInnTekst(textfile) 
print(file_content)
 
if "not found" in file_content:
    print(file_content)
else:
    print("\nFile content successfully read.\n")
    lines = file_content.split("\n")  # Deler teksten inn i linjer
 
    ord = input("What word do you want to find? ")
    search_results, ord_count = sok_ord(lines, ord)
 
    print(printOrd(file_content, ord))
    print(f"\nOccurrences: {ord_count}")
    if search_results:
        print("\nLines containing the word:")
        for line_number, line in search_results:
            print(f"Line {line_number}: {line}")