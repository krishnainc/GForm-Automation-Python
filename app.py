from selenium import webdriver
from random import randint

#for shit in range(10):


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome()
browser.get("https://forms.gle/94CjNmDii8AW8P3f8")

radio1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label')
radio1.click()

Next1 = browser.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
Next1.click()

#jantina
k = randint(1, 2)
if(k == 1):
        lelaki = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
        lelaki.click()

if(k == 2):
        perempuan = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
        perempuan.click()

#umur
umur = randint(19,30)
age = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
age.send_keys(umur)

#etnik
etnik = randint(1,4)
if(etnik == 1):
    melayu = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    melayu.click()

if(etnik == 2):
    cina = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    cina.click()

if(etnik == 3):
    india = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    india.click()

if(etnik == 4):
    lain = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div')
    lain.click()

#agama
agama = randint(1,5)
if(agama == 1):
    islam = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    islam.click()

if(agama == 2):
    buddha = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    buddha.click()

if(agama == 3):
    hindu = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    hindu.click()

if(agama == 4):
    kristian = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div')
    kristian.click()

if(agama == 5):
    lain2 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
    lain2.click()

#uni
uni = randint(1,2)
if(uni == 1):
    kerajaan = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    kerajaan.click()

if(uni == 2):
    swasta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    swasta.click()

#socmed
socmed = randint(1,7)
if(socmed == 1):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()

if(socmed == 2):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()

if(socmed == 3):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()
    insta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    insta.click()

if(socmed == 4):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()
    insta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    insta.click()
    twit = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]')
    twit.click()

if(socmed == 5):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()
    insta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    insta.click()
    twit = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]')
    twit.click()
    sc = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]')
    sc.click()

if(socmed == 6):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()
    insta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    insta.click()
    twit = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]')
    twit.click()
    sc = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]')
    sc.click()
    fb = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]')
    fb.click()

if(socmed == 7):
    ws = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    ws.click()
    tt = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    tt.click()
    insta = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    insta.click()
    twit = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]')
    twit.click()
    sc = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]')
    sc.click()
    fb = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]')
    fb.click()
    tele = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[7]/label/div/div[1]/div[2]')
    tele.click()

#tempohmasa
tempohmasa = randint(1,12)
jam = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
jam.send_keys(tempohmasa)

#games
games = randint(1,2)
if(games == 1):
    mlbb = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    mlbb.click()

if(games == 2):
    cod = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    cod.click()

#bully
bully = randint(1,3)
if(bully == 1):
    pernah = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    pernah.click()

if(bully == 2):
    tidakpernah = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    tidakpernah.click()

if(bully == 3):
    tidakpasti = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    tidakpasti.click()

#victim
victim = randint(1,3)
if(victim == 1):
    pernah2 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    pernah2.click()

if(victim == 2):
    tidakpernah2 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    tidakpernah2.click()

if(victim == 3):
    tidakpasti2 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    tidakpasti2.click()

#platform
platform = randint(1,3)
if(platform == 1):
    whatsapp = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
    whatsapp.send_keys("whatsapp")

if(platform == 2):
    whatsapp = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
    whatsapp.send_keys("instagram")

if(platform == 3):
    whatsapp = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
    whatsapp.send_keys("twitter")

#kesan
kesan = randint(1,3)
if(kesan == 1):
    pernah3 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    pernah3.click()

if(kesan == 2):
    tidakpernah3 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    tidakpernah3.click()

if(kesan == 3):
    tidakpasti3 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    tidakpasti3.click()

#pembuli
pembuli = randint(1,3)
if(pembuli == 1):
    pernah4 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    pernah4.click()

if(pembuli == 2):
    tidakpernah4 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    tidakpernah4.click()

if(pembuli == 3):
    tidakpasti4 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    tidakpasti4.click()

#tindakan
tindakan = randint(1,3)
if(tindakan == 1):
    pernah5 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    pernah5.click()

if(tindakan == 2):
    tidakpernah5 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    tidakpernah5.click()

if(tindakan == 3):
    tidakpasti5 = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div/div')
    tidakpasti5.click()

#suicide
suicide = randint(1,10)
if(suicide == 1):
    menoreh = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    menoreh.click()

if(suicide == 2):
    menumbuk = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    menumbuk.click()
    
    memukul = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    memukul.click()

if(suicide == 3):
    mengelar = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]')
    mengelar.click()

    mencucuk = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]')
    mencucuk.click()

    mengores = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]')
    mengores.click()

if(suicide == 4):
    menghantuk = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[7]/label/div/div[1]/div[2]')
    menghantuk.click()

    menggunting = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[8]/label/div/div[1]/div[2]')
    menggunting.click()

    melompat = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[9]/label/div/div[1]/div[2]')
    melompat.click()

    menggaru = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[10]/label/div/div[1]/div[2]')
    menggaru.click()

if(suicide == 5):
    menampar = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[11]/label/div/div[1]/div[2]')
    menampar.click()

    mengikat = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[12]/label/div/div[1]/div[2]')
    mengikat.click()

    menggaduh = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[13]/label/div/div[1]/div[2]')
    menggaduh.click()

if(suicide == 6):
    menelan = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[14]/label/div/div[1]/div[2]')
    menelan.click()

if(suicide == 7):
    menahan = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[15]/label/div/div[1]/div[2]')
    menahan.click()

    clorox = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[16]/label/div/div[1]/div[2]')
    clorox.click()

if(suicide == 8):
    menoreh = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    menoreh.click()

    clorox = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[16]/label/div/div[1]/div[2]')
    clorox.click()

    menampar = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[11]/label/div/div[1]/div[2]')
    menampar.click()

if(suicide == 9):
    mengores = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]')
    mengores.click()

    menghantuk = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[7]/label/div/div[1]/div[2]')
    menghantuk.click()

if(suicide == 10):
    mencucuk = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]')
    mencucuk.click()

#rawatan
rawatan = randint(1,2)
if(rawatan == 1):
    psiko = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input')
    psiko.send_keys("tidak")

if(rawatan == 2):
    psiko = browser.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input')
    psiko.send_keys("Ya")

Next2 = browser.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
Next2.click()

#bahagian B
#satu
satu = randint(1,5)
if(satu == 1):
    satu1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    satu1.click()

if(satu == 2):
    satu2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    satu2.click()

if(satu == 3):
    satu3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    satu3.click()

if(satu == 4):
    satu4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    satu4.click()

if(satu == 5):
    satu5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    satu5.click()

#dua
dua = randint(1,5)
if(dua == 1):
    dua1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    dua1.click()

if(dua == 2):
    dua2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    dua2.click()

if(dua == 3):
    dua3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    dua3.click()

if(dua == 4):
    dua4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    dua4.click()

if(dua == 5):
    dua5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    dua5.click()

#tiga
tiga = randint(1,5)
if(tiga == 1):
    tiga1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    tiga1.click()

if(tiga == 2):
    tiga2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    tiga2.click()

if(tiga == 3):
    tiga3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    tiga3.click()

if(tiga == 4):
    tiga4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    tiga4.click()

if(tiga == 5):
    tiga5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    tiga5.click()

#empat
empat = randint(1,5)
if(empat == 1):
    empat1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    empat1.click()

if(empat == 2):
    empat2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    empat2.click()

if(empat == 3):
    empat3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    empat3.click()

if(empat == 4):
    empat4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    empat4.click()

if(empat == 5):
    empat5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    empat5.click()

#lima
lima = randint(1,5)
if(lima == 1):
    lima1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    lima1.click()

if(lima == 2):
    lima2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    lima2.click()

if(lima == 3):
    lima3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    lima3.click()

if(lima == 4):
    lima4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    lima4.click()

if(lima == 5):
    lima5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    lima5.click()

#enam
enam = randint(1,5)
if(enam == 1):
    enam1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    enam1.click()

if(enam == 2):
    enam2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    enam2.click()

if(enam == 3):
    enam3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    enam3.click()

if(enam == 4):
    enam4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    enam4.click()

if(enam == 5):
    enam5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    enam5.click()

#tujuh
tujuh = randint(1,5)
if(tujuh == 1):
    tujuh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    tujuh1.click()

if(tujuh == 2):
    tujuh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    tujuh2.click()

if(tujuh == 3):
    tujuh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    tujuh3.click()

if(tujuh == 4):
    tujuh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    tujuh4.click()

if(tujuh == 5):
    tujuh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    tujuh5.click()

#lapan
lapan = randint(1,5)
if(lapan == 1):
    lapan1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    lapan1.click()

if(lapan == 2):
    lapan2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    lapan2.click()

if(lapan == 3):
    lapan3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    lapan3.click()

if(lapan == 4):
    lapan4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    lapan4.click()

if(lapan == 5):
    lapan5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    lapan5.click()

#sembilan
sembilan = randint(1,5)
if(sembilan == 1):
    sembilan1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sembilan1.click()

if(sembilan == 2):
    sembilan2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sembilan2.click()

if(sembilan == 3):
    sembilan3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sembilan3.click()

if(sembilan == 4):
    sembilan4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sembilan4.click()

if(sembilan == 5):
    sembilan5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sembilan5.click()

#sepuluh
sepuluh = randint(1,5)
if(sepuluh == 1):
    sepuluh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sepuluh1.click()

if(sepuluh == 2):
    sepuluh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sepuluh2.click()

if(sepuluh == 3):
    sepuluh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sepuluh3.click()

if(sepuluh == 4):
    sepuluh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sepuluh4.click()

if(sepuluh == 5):
    sepuluh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sepuluh5.click()

#sebelas
sebelas = randint(1,5)
if(sebelas == 1):
    sebelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sebelas1.click()

if(sebelas == 2):
    sebelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sebelas2.click()

if(sebelas == 3):
    sebelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sebelas3.click()

if(sebelas == 4):
    sebelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sebelas4.click()

if(sebelas == 5):
    sebelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sebelas5.click()

#duabelas
duabelas = randint(1,5)
if(duabelas == 1):
    duabelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duabelas1.click()

if(duabelas == 2):
    duabelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duabelas2.click()

if(duabelas == 3):
    duabelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duabelas3.click()

if(duabelas == 4):
    duabelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duabelas4.click()

if(duabelas == 5):
    duabelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duabelas5.click()

#tigabelas
tigabelas = randint(1,5)
if(tigabelas == 1):
    tigabelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    tigabelas1.click()

if(tigabelas == 2):
    tigabelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    tigabelas2.click()

if(tigabelas == 3):
    tigabelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    tigabelas3.click()

if(tigabelas == 4):
    tigabelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    tigabelas4.click()

if(tigabelas == 5):
    tigabelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    tigabelas5.click()

#empatbelas
empatbelas = randint(1,5)
if(empatbelas == 1):
    empatbelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    empatbelas1.click()

if(empatbelas == 2):
    empatbelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    empatbelas2.click()

if(empatbelas == 3):
    empatbelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    empatbelas3.click()

if(empatbelas == 4):
    empatbelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    empatbelas4.click()

if(empatbelas == 5):
    empatbelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    empatbelas5.click()

#limabelas
limabelas = randint(1,5)
if(limabelas == 1):
    limabelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    limabelas1.click()

if(limabelas == 2):
    limabelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    limabelas2.click()

if(limabelas == 3):
    limabelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    limabelas3.click()

if(limabelas == 4):
    limabelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    limabelas4.click()

if(limabelas == 5):
    limabelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    limabelas5.click()

#enambelas
enambelas = randint(1,5)
if(enambelas == 1):
    enambelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    enambelas1.click()

if(enambelas == 2):
    enambelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    enambelas2.click()

if(enambelas == 3):
    enambelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    enambelas3.click()

if(enambelas == 4):
    enambelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    enambelas4.click()

if(enambelas == 5):
    enambelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    enambelas5.click()

#tujuhbelas
tujuhbelas = randint(1,5)
if(tujuhbelas == 1):
    tujuhbelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    tujuhbelas1.click()

if(tujuhbelas == 2):
    tujuhbelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    tujuhbelas2.click()

if(tujuhbelas == 3):
    tujuhbelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    tujuhbelas3.click()

if(tujuhbelas == 4):
    tujuhbelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    tujuhbelas4.click()

if(tujuhbelas == 5):
    tujuhbelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    tujuhbelas5.click()

#lapanbelas
lapanbelas = randint(1,5)
if(lapanbelas == 1):
    lapanbelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    lapanbelas1.click()

if(lapanbelas == 2):
    lapanbelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    lapanbelas2.click()

if(lapanbelas == 3):
    lapanbelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    lapanbelas3.click()

if(lapanbelas == 4):
    lapanbelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    lapanbelas4.click()

if(lapanbelas == 5):
    lapanbelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    lapanbelas5.click()

#sembilanbelas
sembilanbelas = randint(1,5)
if(sembilanbelas == 1):
    sembilanbelas1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sembilanbelas1.click()

if(sembilanbelas == 2):
    sembilanbelas2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sembilanbelas2.click()

if(sembilanbelas == 3):
    sembilanbelas3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sembilanbelas3.click()

if(sembilanbelas == 4):
    sembilanbelas4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sembilanbelas4.click()

if(sembilanbelas == 5):
    sembilanbelas5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sembilanbelas5.click()

#duapuluh
duapuluh = randint(1,5)
if(duapuluh == 1):
    duapuluh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluh1.click()

if(duapuluh == 2):
    duapuluh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluh2.click()

if(duapuluh == 3):
    duapuluh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluh3.click()

if(duapuluh == 4):
    duapuluh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluh4.click()

if(duapuluh == 5):
    duapuluh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluh5.click()

#duapuluhsatu
duapuluhsatu = randint(1,5)
if(duapuluhsatu == 1):
    duapuluhsatu1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhsatu1.click()

if(duapuluhsatu == 2):
    duapuluhsatu2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhsatu2.click()

if(duapuluhsatu == 3):
    duapuluhsatu3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhsatu3.click()

if(duapuluhsatu == 4):
    duapuluhsatu4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhsatu4.click()

if(duapuluhsatu == 5):
    duapuluhsatu5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhsatu5.click()

#duapuluhdua
duapuluhdua = randint(1,5)
if(duapuluhdua == 1):
    duapuluhdua1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhdua1.click()

if(duapuluhdua == 2):
    duapuluhdua2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhdua2.click()

if(duapuluhdua == 3):
    duapuluhdua3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhdua3.click()

if(duapuluhdua == 4):
    duapuluhdua4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhdua4.click()

if(duapuluhdua == 5):
    duapuluhdua5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhdua5.click()

#duapuluhtiga
duapuluhtiga = randint(1,5)
if(duapuluhtiga == 1):
    duapuluhtiga1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhtiga1.click()

if(duapuluhtiga == 2):
    duapuluhtiga2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhtiga2.click()

if(duapuluhtiga == 3):
    duapuluhtiga3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhtiga3.click()

if(duapuluhtiga == 4):
    duapuluhtiga4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhtiga4.click()

if(duapuluhtiga == 5):
    duapuluhtiga5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhtiga5.click()

#duapuluhempat
duapuluhempat = randint(1,5)
if(duapuluhempat == 1):
    duapuluhempat1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhempat1.click()

if(duapuluhempat == 2):
    duapuluhempat2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhempat2.click()

if(duapuluhempat == 3):
    duapuluhempat3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhempat3.click()

if(duapuluhempat == 4):
    duapuluhempat4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhempat4.click()

if(duapuluhempat == 5):
    duapuluhempat5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhempat5.click()

#duapuluhlima
duapuluhlima = randint(1,5)
if(duapuluhlima == 1):
    duapuluhlima1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhlima1.click()

if(duapuluhlima == 2):
    duapuluhlima2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhlima2.click()

if(duapuluhlima == 3):
    duapuluhlima3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhlima3.click()

if(duapuluhlima == 4):
    duapuluhlima4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhlima4.click()

if(duapuluhlima == 5):
    duapuluhlima5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhlima5.click()

#duapuluhenam
duapuluhenam = randint(1,5)
if(duapuluhenam == 1):
    duapuluhenam1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhenam1.click()

if(duapuluhenam == 2):
    duapuluhenam2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhenam2.click()

if(duapuluhenam == 3):
    duapuluhenam3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhenam3.click()

if(duapuluhenam == 4):
    duapuluhenam4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhenam4.click()

if(duapuluhenam == 5):
    duapuluhenam5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhenam5.click()

#duapuluhtujuh
duapuluhtujuh = randint(1,5)
if(duapuluhtujuh == 1):
    duapuluhtujuh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    duapuluhtujuh1.click()

if(duapuluhtujuh == 2):
    duapuluhtujuh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    duapuluhtujuh2.click()

if(duapuluhtujuh == 3):
    duapuluhtujuh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    duapuluhtujuh3.click()

if(duapuluhtujuh == 4):
    duapuluhtujuh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    duapuluhtujuh4.click()

if(duapuluhtujuh == 5):
    duapuluhtujuh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    duapuluhtujuh5.click()

Next3 = browser.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
Next3.click()

#bahagian C
#fizikal
fizikal = randint(1,2)
if(fizikal == 1):
    fiz1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    fiz1.click()
if(fizikal == 2):
    fiz2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    fiz2.click()

#cedera
cedera = randint(1,2)
if(cedera == 1):
    ced1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    ced1.click()
if(cedera == 2):
    ced2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    ced2.click()

#bunuh
bunuh = randint(1,2)
if(bunuh == 1):
    bun1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    bun1.click()
if(bunuh == 2):
    bun2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
    bun2.click()

#bagaimana
bagaimana = randint(1,10)
if(bagaimana == 1):
    bagai1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai1.send_keys("pisau")

if(bagaimana == 2):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("makan panadol")

if(bagaimana == 3):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("minum ubat batuk")

if(bagaimana == 4):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("laparkan diri")

if(bagaimana == 5):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("melecurkan tangan")

if(bagaimana == 6):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("menghantuk kepala di dinding")

if(bagaimana == 7):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("menjerit sehingga tiada suara")

if(bagaimana == 8):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("memotong rambut")

if(bagaimana == 9):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("tendang dinding")

if(bagaimana == 10):
    bagai2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bagai2.send_keys("tumbuk cermin")


#berapa
berapa = randint(1,10)
if(berapa == 1):
    berapa1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa1.send_keys("1")

if(berapa == 2):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("2")

if(berapa == 3):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("3")

if(berapa == 4):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("4")

if(berapa == 5):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("5")

if(berapa == 6):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("6")

if(berapa == 7):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("7")

if(berapa == 8):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("8")

if(berapa == 9):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("9")

if(berapa == 10):
    berapa2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    berapa2.send_keys("10")

#bahagian
bahagian = randint(1,10)
if(bahagian == 1):
    bahagian1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian1.send_keys("kaki")

if(bahagian == 2):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("tapak tangan")

if(bahagian == 3):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("pergelangan tangan")

if(bahagian == 4):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("kepala")

if(bahagian == 5):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("belakang badan")

if(bahagian == 6):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("siku")

if(bahagian == 7):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("muka")

if(bahagian == 8):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("jari")

if(bahagian == 9):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("dahi")

if(bahagian == 10):
    bahagian2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bahagian2.send_keys("peha")

#first
first = randint(1,5)
if(first == 1):
    first1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    first1.click()

if(first == 2):
    first2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    first2.click()

if(first == 3):
    first3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    first3.click()

if(first == 4):
    first4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    first4.click()

if(first == 5):
    first5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    first5.click()

#second
second = randint(1,5)
if(second == 1):
    second1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    second1.click()

if(second == 2):
    second2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    second2.click()

if(second == 3):
    second3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    second3.click()

if(second == 4):
    second4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    second4.click()

if(second == 5):
    second5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    second5.click()

#third
third = randint(1,5)
if(third == 1):
    third1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    third1.click()

if(third == 2):
    third2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    third2.click()

if(third == 3):
    third3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    third3.click()

if(third == 4):
    third4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    third4.click()

if(third == 5):
    third5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    third5.click()

#fourth
fourth = randint(1,5)
if(fourth == 1):
    fourth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    fourth1.click()

if(fourth == 2):
    fourth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    fourth2.click()

if(fourth == 3):
    fourth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    fourth3.click()

if(fourth == 4):
    fourth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    fourth4.click()

if(fourth == 5):
    fourth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    fourth5.click()

#fifth
fifth = randint(1,5)
if(fifth == 1):
    fifth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    fifth1.click()

if(fifth == 2):
    fifth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    fifth2.click()

if(fifth == 3):
    fifth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    fifth3.click()

if(fifth == 4):
    fifth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    fifth4.click()

if(fifth == 5):
    fifth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    fifth5.click()

#sixth
sixth = randint(1,5)
if(sixth == 1):
    sixth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sixth1.click()

if(sixth == 2):
    sixth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sixth2.click()

if(sixth == 3):
    sixth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sixth3.click()

if(sixth == 4):
    sixth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sixth4.click()

if(sixth == 5):
    sixth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sixth5.click()

#seventh
seventh = randint(1,5)
if(seventh == 1):
    seventh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    seventh1.click()

if(seventh == 2):
    seventh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    seventh2.click()

if(seventh == 3):
    seventh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    seventh3.click()

if(seventh == 4):
    seventh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    seventh4.click()

if(seventh == 5):
    seventh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    seventh5.click()

#eighth
eighth = randint(1,5)
if(eighth == 1):
    eighth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    eighth1.click()

if(eighth == 2):
    eighth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    eighth2.click()

if(eighth == 3):
    eighth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    eighth3.click()

if(eighth == 4):
    eighth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    eighth4.click()

if(eighth == 5):
    eighth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    eighth5.click()

#ninth
ninth = randint(1,5)
if(ninth == 1):
    ninth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    ninth1.click()

if(ninth == 2):
    ninth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    ninth2.click()

if(ninth == 3):
    ninth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    ninth3.click()

if(ninth == 4):
    ninth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    ninth4.click()

if(ninth == 5):
    ninth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    ninth5.click()

#tenth
tenth = randint(1,5)
if(tenth == 1):
    tenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    tenth1.click()

if(tenth == 2):
    tenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    tenth2.click()

if(tenth == 3):
    tenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    tenth3.click()

if(tenth == 4):
    tenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    tenth4.click()

if(tenth == 5):
    tenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    tenth5.click()

#eleventh
eleventh = randint(1,5)
if(eleventh == 1):
    eleventh1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    eleventh1.click()

if(eleventh == 2):
    eleventh2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    eleventh2.click()

if(eleventh == 3):
    eleventh3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    eleventh3.click()

if(eleventh == 4):
    eleventh4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    eleventh4.click()

if(eleventh == 5):
    eleventh5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    eleventh5.click()

#twelveth
twelveth = randint(1,5)
if(twelveth == 1):
    twelveth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    twelveth1.click()

if(twelveth == 2):
    twelveth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    twelveth2.click()

if(twelveth == 3):
    twelveth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    twelveth3.click()

if(twelveth == 4):
    twelveth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    twelveth4.click()

if(twelveth == 5):
    twelveth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    twelveth5.click()

#thirteenth
thirteenth = randint(1,5)
if(thirteenth == 1):
    thirteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    thirteenth1.click()

if(thirteenth == 2):
    thirteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    thirteenth2.click()

if(thirteenth == 3):
    thirteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    thirteenth3.click()

if(thirteenth == 4):
    thirteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    thirteenth4.click()

if(thirteenth == 5):
    thirteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    thirteenth5.click()

#fourteenth
fourteenth = randint(1,5)
if(fourteenth == 1):
    fourteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    fourteenth1.click()

if(fourteenth == 2):
    fourteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    fourteenth2.click()

if(fourteenth == 3):
    fourteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    fourteenth3.click()

if(fourteenth == 4):
    fourteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    fourteenth4.click()

if(fourteenth == 5):
    fourteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    fourteenth5.click()

#fifteenth
fifteenth = randint(1,5)
if(fifteenth == 1):
    fifteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    fifteenth1.click()

if(fifteenth == 2):
    fifteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    fifteenth2.click()

if(fifteenth == 3):
    fifteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    fifteenth3.click()

if(fifteenth == 4):
    fifteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    fifteenth4.click()

if(fifteenth == 5):
    fifteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    fifteenth5.click()

#sixteenth
sixteenth = randint(1,5)
if(sixteenth == 1):
    sixteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    sixteenth1.click()

if(sixteenth == 2):
    sixteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    sixteenth2.click()

if(sixteenth == 3):
    sixteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    sixteenth3.click()

if(sixteenth == 4):
    sixteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    sixteenth4.click()

if(sixteenth == 5):
    sixteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    sixteenth5.click()

#seventeenth
seventeenth = randint(1,5)
if(seventeenth == 1):
    seventeenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    seventeenth1.click()

if(seventeenth == 2):
    seventeenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    seventeenth2.click()

if(seventeenth == 3):
    seventeenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    seventeenth3.click()

if(seventeenth == 4):
    seventeenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    seventeenth4.click()

if(seventeenth == 5):
    seventeenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    seventeenth5.click()

#eighteenth
eighteenth = randint(1,5)
if(eighteenth == 1):
    eighteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    eighteenth1.click()

if(eighteenth == 2):
    eighteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    eighteenth2.click()

if(eighteenth == 3):
    eighteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    eighteenth3.click()

if(eighteenth == 4):
    eighteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    eighteenth4.click()

if(eighteenth == 5):
    eighteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    eighteenth5.click()

#nineteenth
nineteenth = randint(1,5)
if(nineteenth == 1):
    nineteenth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    nineteenth1.click()

if(nineteenth == 2):
    nineteenth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    nineteenth2.click()

if(nineteenth == 3):
    nineteenth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    nineteenth3.click()

if(nineteenth == 4):
    nineteenth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    nineteenth4.click()

if(nineteenth == 5):
    nineteenth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    nineteenth5.click()

#twentieth
twentieth = randint(1,5)
if(twentieth == 1):
    twentieth1 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')
    twentieth1.click()

if(twentieth == 2):
    twentieth2 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')
    twentieth2.click()

if(twentieth == 3):
    twentieth3 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div')
    twentieth3.click()

if(twentieth == 4):
    twentieth4 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div')
    twentieth4.click()

if(twentieth == 5):
    twentieth5 = browser.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div')
    twentieth5.click()

Next4 = browser.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
Next4.click()

submit = browser.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
submit.click()

#until 101 was ori















    









