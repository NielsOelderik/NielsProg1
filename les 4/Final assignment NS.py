def standaardtarief(afstandKM):
    if afstandKM >= 50:
        return (afstandKM * 0.60 + 15)
    if afstandKM <= 0:
        return 0
    else:
        return (afstandKM * 0.80)

inputleeftijd = int(input('leeftijd: '))
inputweekendrit = str(input('is het weekend? ja/nee: '))
inputafstandKM = int(input('afstand in KM: '))

def ritprijs(leeftijd, weekendrit, afstandKM):
    TempPrijs = standaardtarief(afstandKM) * 0.70
    if inputweekendrit == 'nee':
        if inputleeftijd < 12 or inputleeftijd >= 65:
            return TempPrijs
        else:
            return standaardtarief(afstandKM)
    else:
        Tempprijs = standaardtarief(afstandKM) * 0.65
        tempprijs = standaardtarief(afstandKM) * 0.60
        if inputleeftijd <= 12 or inputleeftijd >= 65:
            return TempPrijs
        else:
            return tempprijs

print('deze rit kost u €', ritprijs(inputleeftijd, inputweekendrit, inputafstandKM))
