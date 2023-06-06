import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import make_msgid
import sys
import re
import requests
from bs4 import BeautifulSoup
#from email.MIMEImage import MIMEImage
import mimetypes
info_list = []

def validate_searched_name(input_text, name):
    
    return True

def search_product_on_amazon(input_text):
    # Extracting keywords from the input text
    keywords = re.findall(r'\b[A-Za-z0-9]+\b', input_text)
    # print(keywords)
    search_query = '+'.join(keywords)
    #print(keywords)
    #input()
    url = f'https://www.amazon.in/s?k={search_query}&ref=nb_sb_noss'
    #print(url)
    # Sending a GET request to Amazon India and fetching the search results
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
    response = requests.get(url, headers=headers)
    #print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    #print(results)
    # Extracting product details from the search results
    for result in results:
        #print("---------Begin-------")
        name = result.find('h2').text.strip()
        name_flag = validate_searched_name(input_text, name)
        if not name_flag:
            continue
        price = result.find('span', {'class': 'a-price-whole'})
        if not price:
            continue
        price = result.find('span', {'class': 'a-price-whole'}).text.strip()
        #print("*********")
        #print("Price = ", price)
        #print("*********")
        before_discount = result.find('span', {'class': 'a-letter-space'})
        #print("before discount", before_discount)
        discount = None
        if before_discount:
            for sibling in before_discount.find_next_siblings():
                if sibling.name == 'span':
                    discount = sibling.text.strip()
                    break
        #print("discount is :++++==== ", discount)
        if discount:
            #print("***discount*** ", discount)
            discount_info = discount
            product_link = result.find('a')['href']
            #print(name)
            info_list.append([product_link, name, price, discount])
            #print(f'Product: {name}\nPrice: {price}\nDiscount: {discount_info}\nLink: {product_link}\n')
        else:
            product_link = result.find('a')['href']
            #print(name)
            info_list.append([product_link, name, price, "0"])
            #print(f'Product: {name}\nPrice: {price}\nLink: {product_link}\n')
        #print("---------End-------")





productText = ""
textLength = len(sys.argv)
for i in range(2, textLength):
    productText += sys.argv[i]+" "

msg = MIMEMultipart()
regEmail = 'mayankjan2002@gmail.com'
password = "kmcpzncovicnevyy"
msg['from']="mayankjoshi12310@gmail.com"
msg['to']= regEmail
msg['subject']="Smart AI"
body = "This is a sample mail for testing purpose"
#part=MIMEImage
discount='50'#"admin search discount" #using web searching
price='1234' #"admin search price" #using web searching
link="https://github.com/UB-Mannheim/tesseract/wiki"#"admin fetch website product link" #using web searching
search_product_on_amazon(productText)

html_text='''
<html>
<body style="background-image: url('image1.jpeg');">
<hr />
	
	<div style="width:100%;margin-left:auto;margin-right:auto;">
	<h2>Welcome to smartai dustbin</h2>
	<h4>Recognized Product Name: '''+str(sys.argv[2])+'''</h4>
              <hr />
              <h3>Related products on Amazon</h3>
              <table style="border:2px solid black; border-collapse:collapse">
              <tr style="border:2px solid black">
                  <th style="border:2px solid black">S. no</th>
                  <th style="border:2px solid black">Product</th>
                  <th style="border:2px solid black">Price</th>
                  <th style="border:2px solid black">Discount</th>
              </tr>
              '''
sno = 0
for i in info_list:
    sno+=1
    #link = i[0]
    name = i[1]
    keywrds = re.findall(r'\b[A-Za-z0-9]+\b', name)
    #print(keywrds)
    searchquery = '+'.join(keywrds)
    link=f'https://www.amazon.in/s?k={searchquery}&ref=nb_sb_noss'
    price = i[2]
    discount= i[3]
    html_text = html_text+'''
<tr style="border:2px solid black">
<td style="border:2px solid black">'''+str(sno)+'''</td>
<td style="border:2px solid black"><a href="'''+str(link)+'''">'''+str(name)+'''</a></td>
<td style="border:2px solid black">'''+str(price)+'''</td>
<td style="border:2px solid black">'''+str(discount)+'''</td>
</tr>
'''
html_text=html_text+'''
</table>
	<p>Thank you for using our services</p>
	</div>
</body>
</html>
'''
#.format(image_cid=image_cid[1:-1]),subtype='html')
msg.attach(MIMEText(html_text,'html'))

with open(str(sys.argv[1]), 'rb') as f:
    img_data = MIMEImage(f.read())
    img_data.add_header('Content-Disposition', 'attachment', filename='logo.jpg')
    msg.attach(img_data)

text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("mayankjoshi12310@gmail.com",password)
server.sendmail("mayankjoshi12310@gmail.com",regEmail,text)
server.quit()
#PD$fTc$Aif#Trl1U$Tkg 000webhost password
