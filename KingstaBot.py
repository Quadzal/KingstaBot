try:
    import platform
    import subprocess as cmd
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import os
    from time import sleep
    from InstagramAPI import InstagramAPI
    import re
    import pyautogui
except:
    if platform.system()=="Windows":
        cmd.call("pip3 install selenium InstagramApi pyautogui subprocess",shell=True)
    else:
        print("")




if platform.system()=="Windows":
    cmd.call("color a",shell=True)
print("""
############################################
##                  ESATBEY35(KingKong)    #
##                  KingİnstaBot.py        #
############################################
""")



print("""Seçenekler:

1-)Biyografi Değiştir
2-)Foto Değiştir
3-)Unfollow Yapanları Tespit Et Ve Takipten Çık
4-)Hedef Hesabın Takipçilerini Takip Et.
5-)Anasayfadaki Fotoğrafları Beğen
6-)Gönderi At
7-)Program Hakkında
9-)Programdan Çık
""")

secenekler=int(input("Seçiniz >>> "))
if platform.system()=="Windows":
    cmd.call("cls", shell=True)

takipet=[]
liste=[]

takip=[]

unfollow=[]


sayi=1

ayarlar = Options()
ayarlar.add_argument("--headless")
ayarlar.add_argument("--windows-size=1920x1080")
driver = webdriver.Chrome(os.getcwd()+"\src\chromedriver.exe",chrome_options=ayarlar)
def albumvefotoyukle():
    print("""
1-)Fotoğraf Yükle
2-)Albüm Yükle
""")

    gir=input("Seçiniz>>> ")

    api=InstagramAPI("instadenemehesap35esat88","esat3535")
    api.login()
    cmd.call("cls", shell=True)

    if gir=="1":
        path=input("Fotoğrafınızın Dosya Yolunu Giriniz: ")
        soru=input("Açıklama Yazmak İstiyor musunuz? E/H ")
        if soru=="E" or soru=="e":
            aciklama=input("Yazmak İstediğiniz Açıklamayı Giriniz: ")
            api.uploadPhoto(photo=path,caption=aciklama)
        else:
            api.uploadPhoto(photo=path)
    elif gir=="2":
        albumliste = []
        kactane=int(input("Kaç Tane Fotoğraftan Albüm Yapmak İstiyorsunuz: "))
        sayii=1
        albümfotosayi=0
        if 10<kactane:
            print("10dan Fazla Girilemez Çıkılıyor!")
            exit()
        elif kactane<2:
            print("2 den küçük Girilemez Çıkılıyor")
            exit()
        else:


            while kactane > albümfotosayi:
                dosyayolu = input("{0}. Fotoğrafınızın Dosya Yolunu Giriniz: ".format(sayii))
                albumliste.append({"type": "photo",
                            "file": dosyayolu})
                albümfotosayi += 1
                sayii+=1
                soru = input("Açıklama Yazmak İstiyor musunuz? E/H ")
                if soru == "E" or soru == "e":

                    aciklamaaa = input("Yazmak İstediğiniz Açıklamayı Giriniz: ")
                    api.uploadAlbum(albumliste,caption=aciklamaaa)
                else:
                    api.uploadAlbum(albumliste)
            print("Albüm Eklenmiştir!")
    else:
        print("Yanlış Seçenek Girildi Programdan Çıkılıyor!")
        exit()
def girisyapmak():
    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
    sleep(2)
    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    driver.get("https://www.instagram.com/")
    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
    sleep(3)
    print("KingİnstaBot >>> ")
    global k_adi
    print("Bot Başlamıştır!\n")
    k_adi = input("KingİnstaBot >>> Kullanıcı Adını Giriniz: ")

    global sifre
    sifre = input("KingİnstaBot >>> Sifreyi Giriniz: ")
    print("\nGiriş Yapılıyor...\n")
    girisbutonu = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
    girisbutonu.click()
    sleep(2)
    kullaniciadi = driver.find_element_by_name("username")
    parola = driver.find_element_by_name("password")
    kullaniciadi.send_keys(k_adi)
    parola.send_keys(sifre)
    sleep(2)
    girisyap = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
    sleep(3)
    girisyap.click()
    sleep(3)



def fotodegistir():
    driver.get("https://www.instagram.com/accounts/edit/")
    koymakistediginizresminadresi=input("Resmin Dosya Yolunu Giriniz: ")
    sleep(3)
    fotodegistircss=driver.find_element_by_class_name("LUEBY")
    fotodegistircss.click()
    sleep(3)
    fotoseccss=driver.find_element_by_css_selector(".aOOlW.bIiDR")
    fotoseccss.click()
    pyautogui.typewrite(koymakistediginizresminadresi)
    sleep(1)
    pyautogui.press("enter")
    sleep(15)
    print("Foto Değiştirilmiştir!")
def biyodegistir():
    print("Lütfen Biyografinizi Önce Boş Bırakınız.!\n")
    biyodegiscek=input("Biyografiniz Ne İle Değişsin: ")
    driver.get("https://www.instagram.com/accounts/edit/")
    biyografi=driver.find_element_by_id("pepBio")
    biyografi.send_keys(biyodegiscek)
    sleep(2)
    gönderbuton=driver.find_element_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P")
    gönderbuton.click()
    sleep(3)
    print("\nBiyografi Değiştirilmiştir!")





def takipvetakipcilericek():
    api = InstagramAPI(k_adi,sifre)
    api.login()
    cmd.call("cls", shell=True)
    usrid=api.username_id
    followers = api.getTotalSelfFollowers()
    takipedilenler = api.getTotalFollowings(str(usrid))
    nesne = re.findall("'pk':(.*?),", str(followers))
    for i in nesne:
        liste.append(i)
    nesne2 = re.findall("'pk':(.*?),", str(takipedilenler))
    for i in nesne2:
        takip.append(i)

def takiptencik():
    instapi=InstagramAPI(k_adi,sifre)
    instapi.login()
    cmd.call("cls", shell=True)
    for i in takip:
        if i in liste:
            continue
        else:
            a = i.replace(" ", "")
            unfollow.append(a)
            print("\nTakip Etmeyenin Kullanıcı Adı: ",a)

    takipcikarsayi=int(input("Ne Kadar Unfollow Yapan Çıkarılsın: "))
    if takipcikarsayi>len(unfollow):
        print("Unfollow Yapanların Sayısından Fazla Sayı Girdiniz!")
        exit()
    elif takipcikarsayi<0 or takipcikarsayi==0:
        print("Sıfırdan Küçük Sayı Veya Sıfır Girilemez!")
        exit()
    else:
        for i in unfollow:
            instapi.unfollow(i)
            takipcikarsayi -=1
            if takipcikarsayi == 0:
                print("\nİşlem Bitmiştir!")
                break
            else:
                continue

def takipcileritakipet():
    takipciler=[]
    print("Hedef Hesabı Önce Takip Edin Veya Gizli Hesap Olmasın Yoksa Hata Verir!\n")
    takipcicekilecekhesap=input("Hangi Hesabın Takipçilerini Takip Etmek İstiyorsanız Kullanıcı Adını Giriniz: ")
    hedeftakipciler = []
    driver.get("https://www.instagram.com/"+takipcicekilecekhesap)
    sleep(3)
    a = driver.page_source
    sayi1=1
    userid = re.findall('"id":"(.*?)",', str(a))

    for i in userid:
        hedeftakipciler.append(i)
    api = InstagramAPI(k_adi,sifre)
    api.login()
    cmd.call("cls",shell=True)
    takipcilericek = api.getTotalFollowers(hedeftakipciler[1])
    usernameayir = re.findall("'pk':(.*?),", str(takipcilericek))
    for i in usernameayir:
        a=i.replace(" ","")
        takipciler.append(a)
    print(len(takipciler)," Kişi Bulundu!")
    for x in takipciler:
        print("{0}. Kişi Takip Edildi!".format(sayi1))
        api.follow(x)
        sayi1+=1

def fotobegen():
    bul = driver.find_element_by_css_selector(".aOOlW.HoLwm")
    sleep(3)
    bul.click()
    sleep(3)
    driver.get("https://www.instagram.com/")
    fotosayi=0
    anasayfabegeni=int(input("Anasayfanızdaki Kaç Adet Gönderi Beğenilsin: \n"))
    if anasayfabegeni<fotosayi or anasayfabegeni==fotosayi:
        print("Sıfır Veya Sıfırdan Küçük Sayı Girdiğiniz Tespit Edildi!\n")
        print("Programdan Çıkılıyor...")
        exit()
    else:
        while fotosayi<anasayfabegeni:
            fotosayi+=1
            begenbuton=driver.find_element_by_css_selector(".Szr5J.coreSpriteHeartOpen")
            sleep(1)
            begenbuton.click()

    print("Anasayfanızdaki {} Foto Beğenilmiştir!",format(anasayfabegeni))




if secenekler==9:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("\nProgramdan Çıkılıyor Lütfen Bekleyin...")
    sleep(1)
    exit()
elif secenekler==7:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("""
    ############################################
    ##Programın Adı:KingİnstaBot.py                 #
    ##Programı Hazırlayan:King Kong(EsatBey35) #
    ##Program Sürümü:1.0                       #
    ##Hazırlayanın Email'i:esat3515@gmail.com  #
    ############################################
    """)

elif secenekler==1:
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Çıkış Yapılıyor.")
        driver.quit()
        exit()
    else:
        print("KingİnstaBot >>> Giriş Yapıldı.")
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("KingİnstaBot >>> Giriş Yapıldı.")
    biyodegistir()
elif secenekler==2:
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Çıkış Yapılıyor.")
        driver.quit()
        exit()
    else:
        print("KingİnstaBot >>> Giriş Yapıldı.")
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)

    fotodegistir()
elif secenekler==3:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    takipvetakipcilericek()
    takiptencik()

elif secenekler==4:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    girisyapmak()
    takipcileritakipet()
elif secenekler==5:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    girisyapmak()
    sleep(3)
    fotobegen()
elif secenekler==6:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    albumvefotoyukle()
else:
    print("Yanlış Seçenek Girdiniz Programdan Çıkılıyor!")
    exit()

try:
    os.remove(os.getcwd() + "\debug.log")
except:
    sleep(5)
    driver.quit()