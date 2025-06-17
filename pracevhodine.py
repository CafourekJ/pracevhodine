krmna_davka = 0

while True:
    vaha = int(input("Zadej váhu kočky v kg: "))
    davka = vaha * 30 + 70
    print("Kočka váží", vaha, "kg a měla by dostat", davka, "gramů krmení denně.")
    krmna_davka += davka

    dalsi = input("Chceš zadat další kočku? (ano/ne): ")
    if dalsi != "ano":
        break

print("Celková krmná dávka pro všechny kočky:", krmna_davka, "gramů.")