hesapA = {
    'ad': 'Zeynep Güney',
    'hesapNo': '123456',
    'bakiye': 3000,
    'ekHesap': 2000
}

hesapB = {
    'ad': 'Ali Turen',
    'hesapNo': '163456',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print("Paranızı alabilirisiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye']+ hesap['ekHesap']


        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h)')
            
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar -  hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")  
        else:
            print("Bakiye yetersiz")    
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL dir. ")                  

paraCek(hesapA, 3000) 

print("************************")
paraCek(hesapA, 2000)
