

################################################################################
# FUNCION PARA OBTENER EL PRECIO DEL DOLAR Y OTRAS DIVISAS
################################################################################

import mechanize
from bs4 import BeautifulSoup



def dolar():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url="https://transferwise.com/es/currency-converter/usd-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return val.text.split(',')[0]

def euro():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url="https://transferwise.com/es/currency-converter/eur-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return val.text.split(',')[0]


def pound():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url="https://transferwise.com/es/currency-converter/gbp-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return val.text.split(',')[0]

def zloty():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url="https://transferwise.com/es/currency-converter/pln-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return str(val.text.split(',')[0])+"."+str(val.text.split(',')[1])[:2]

def yen():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url=" https://transferwise.com/es/currency-converter/jpy-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return str(val.text.split(',')[0])+"."+str(val.text.split(',')[1])

def mex():
    br = mechanize.Browser()
    br.set_handle_equiv(False)
    # [('User-agent', 'Firefox')]
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    url="https://transferwise.com/es/currency-converter/mxn-to-cop-rate"
    html = br.open(url)
    soup = BeautifulSoup(html, features="lxml")
    val=soup.find('span', {'class': 'text-success'})
    return str(val.text.split(',')[0])+"."+str(val.text.split(',')[1])[:2]
