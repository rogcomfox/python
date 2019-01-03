biologi = []
a = 1
i = 0
jalan = True

while(jalan):
    tanya = input("Apakah ingin menginput data? (y/t): ")
    print("-----------------------------")
    if(tanya == "y"):
        data_biologi = input ("Input nama genus dan spesies tanaman ke-{}: ".format(a))
        biologi.append(data_biologi)
        a += 1
        print ("Data yang telah tersimpan sebanyak {} tanaman".format(len(biologi)))
        for bio in biologi:
            print ("- {}".format(bio))
        print("-----------------------------")    
    elif(tanya == "t"):
        tanya1 = input("Apakah ingin mencari data? (y/t): ")
        print("-----------------------------")
        if(tanya1 == "y"):
            masuk = input("Masukkan nama spesies dari tanaman: ")
            for masuk in biologi.index(i):
                print("Data Ditemukan")
                print(masuk)
                i+=1
        if(tanya1 == "t"):
            jalan = False