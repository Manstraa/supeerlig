#step 1 turk oldugunu hatirla
#adim1 : fonksiyon olustur
#adim 2 : 3 tane girdi olustur
#adim 3 : if kullanarak cikti olustur


def dort_buyukler():
    girdi = raw_input('Takimini Gir :')
    if girdi=='Besiktas':
        print('Takiminiz Mac Fazlasiyla 41 Puan ile 5 . Sirada')
    elif girdi=='Galatasaray' :
        print('Takiminiz Kume Dusecek G.O')
    if girdi=='Fenerbahce' :
        print('Takiminizi tuttugunuz icin sabriniza hayran oldugumuzu belirtmek isteriz')
    elif girdi=='Trabzonspor' :
        print('UYYY SAMPiYONSUN USSAAGiM')
print (dort_buyukler())
