import os,sqlite3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chromedriver =  "/home/0x656e/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()
chrome_options.add_argument("--disable-javascript --disable-javascript-i18n-api")
chrome_options.add_argument("load-extension=/home/0x656e/.config/google-chrome/Default/Extensions/fdcgdnkidjaadafnichfpabhfomcebme/5.5.6_0/")
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

def geturl(url):
    try:
        driver.get(url)

        notified = driver.find_element_by_css_selector('.defacet a').get_attribute('href')
        checkdb(notified)
    except NoSuchElementException:
        return "ID"
def checkdb(notified):
    op = sqlite3.connect("zone-h.db")
    cs = op.cursor()
    notified = notified.lower()
    query = """SELECT * FROM teams where teamurl='%s'""" %notified
    query = cs.execute(query).fetchall()
    if query == []:
        teamname = notified.split("=")[1]
        cs.execute("INSERT INTO teams(teamname,teamurl) VALUES(?,?)",(teamname,notified))
        op.commit()
        op.close()
        print(teamname+ "is added")
    else:

        pass


id = 512
while True:
    link =  "http://www.zone-h.com/mirror/id/%s" %id
    chk = geturl(link)
    if chk == False:
        print(id)
        driver.quit()
    elif chk == "ID":

        print("Hatalı id:"+str(id))
        print("# Captchayı veya hatayı giderdiyseniz 1'e basın aksi halde 1 harici bir tuşa basın")
        islem = input("Komut : >")
        if islem == "1":
            id = id
        else:
            id +=1
    else:
        id += 1
        print(id)
