import json

def JSONFoods():
    
    with open ("/home/mert/Desktop/pythonWorkspace/foods.json","r",encoding="utf-8") as dosya:
    
        load_r = json.load(dosya)
        

    for index,isim in enumerate (load_r,start=1):

        print(index,isim['restaurant'].capitalize())

    user = str(input("Bir Şirket İsmi Yazınız : ")).lower()

    if user:
        for i in load_r:
            if user.lower() == i['restaurant']:
                for j in i['foodItems']:
                    print("Menü Adı :",j['foodName'] , "---", "KALORİ : ",(str(j['calories'])))
                    continue
                break
        else:
            print("LÜTFEN GEÇERLİ BİR ŞİRKET İSMİ GİRİNİZ!!")

JSONFoods()

