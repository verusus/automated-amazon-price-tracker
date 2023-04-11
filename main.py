import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "hamid.business.go@gmail.com"
password = "bjinhxejfydbenmw"
PRODUCT_URL = "https://www.amazon.com/dp/B00CCYLBZ0/ref=sspa_dk_detail_3?pd_rd_i=B00CCYLBZ0&pd_rd_w=gimGY&content-id" \
              "=amzn1.sym.89ee1d2e-380f-4a05-89e5-d22eb0a17762&pf_rd_p=89ee1d2e-380f-4a05-89e5-d22eb0a17762&pf_rd_r" \
              "=BAY7RN85XGWHA6GV84P0&pd_rd_wg=oUSIX&pd_rd_r=3b0e48c1-a7b2-48a4-a139-f1931f37ecf0&s=home-garden&sp_csd" \
              "=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa" \
              "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR1ozSVFIMEQ2TENCJmVuY3J5cHRlZElkPUEwNDM5MzI5Q0hOSFhFS0lYNENOJmVuY3J5cHRlZ" \
              "EFkSWQ9QTAxODgxMTExMTBNNFZONjIwM1hUJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN" \
              "0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
LIMIT_PRICE = 300

r = requests.get(PRODUCT_URL,
                 headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34",
                          "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,fr-FR;q=0.7,ar;q=0.6"
                          }
                 )
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
price_and_shipping = float(soup.select(selector="span.a-size-base.a-color-base")[3].getText().split("$")[1])
# print(price_and_shipping)
product_name = soup.find(id="productTitle").get_text()

if price_and_shipping < 300:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Drop down price alert!\n\n'{product_name}' is now {price_and_shipping}$ "
                                f"including shipping price!\n{PRODUCT_URL}")

