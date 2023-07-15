#!/usr/bin/python3
from ipaddress import IPv4Network

netmask = [0,128,192,224,240,248,252,254,255]
wildcard = [255,127,63,31,15,7,3,1,0]

def omvandla(input):
    sub = IPv4Network('0.0.0.0/' + input).netmask
    wild = IPv4Network('0.0.0.0/' + input).hostmask
    cidr = IPv4Network('0.0.0.0/' + input).prefixlen
    print("Subnätmasken är: ",sub)
    print("Wildcardmasken är ",wild)
    print("CIDR är ",cidr)

def checker (val, input):
    splittat = [int(octett) for octett in input.split(".")]
    if len(splittat) != 4:
        print("Fel vid input, försök igen")
        return False
    if val == 2:
        for octett in splittat:
            if octett not in netmask:
                print("Nätmasken är ej tillåten")
                return False
        if splittat[0] < 255 and splittat[1] != 0:
            print("Nätmasken ej korrekt i andra oktetten")
            return False
        elif splittat[1] < 255 and splittat[2] != 0:
            print("Nätmasken ej korrekt i tredje oktetten")
            return False
        elif splittat[2] < 255 and splittat[3] != 0:
            print("Nätmasken ej korrekt i fjärde oktetten")
            return False
        elif splittat[3] == 254:
            print("Nätmask ej tillåten")
            return False
    if val == 3:
        for octett in splittat:
            if octett not in wildcard:
                print("Wildcardmasken är ej tillåten")
                return False
        if splittat[1] < 255 and splittat[0] != 0:
            print("Wildcardmask ej korrekt i första oktetten")
            return False
        elif splittat[2] < 255 and splittat[1] != 0:
            print("Wildcardmask ej korrekt i andra oktetten")
            return False
        elif splittat[3] < 255 and splittat[2] != 0:
            print("Wildcardmask ej korrekt i tredje oktetten")
            return False
        elif splittat[3] == 1:
            print("Wildcardmask ej användbar")
            return False
    return True



if __name__ == '__main__':
    while True:
        try:
            val = int(input("Vad vill du göra om?\nVälj mellan 1/2/3/4\n1: CIDR?\n2: Subnät?\n3: Wildcard?\n4: Avsluta?\n"))
            if val == 1:
                try:
                    cidrin = input("Vilken CIDR vill du göra om? ")
                    cidr = int(cidrin)
                    if cidr >= 0 and cidr <= 32:
                        if cidr == 31:
                            print("CIDR ej korrekt, CIDR 31 går ej att använda")
                        else:
                            omvandla(cidrin)
                    else:
                        print("CIDR ej korrekt och går mellan 0 till 32 med undantag 31")
                except:
                    print("CIDR kan endast vara mellan 1-32 i siffror")
            if val == 2:
                try:
                    subnatin = input("Vilken subnäts adress? ")
                    if checker(val,subnatin):
                        omvandla(subnatin)
                    else:
                        continue
                except:
                    print("Nätmask är endast siffor avskiljda med . mellan varje oktett")
            if val == 3:
                try:
                    wildcardin = input("Vilken wildcard mask? ")
                    if checker(val,wildcardin):
                        omvandla(wildcardin)
                except:
                    print("Wildcard mask är endast siffror avskiljda med . mellan varje oktett")
            if val == 4:
                break
        except ValueError:
            print("Svar måste anges med siffrorna 1,2,3 eller 4")

    print("Programmet har kört klart, tack för denna gången")
    exit(0)