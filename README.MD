<p align="center"><img src="https://img.shields.io/badge/Version-1.0.2-blue"></p>
<p align="center">
  <a href="https://github.com/mdminhaz2003">
    <img src="https://img.shields.io/github/followers/mdminhaz2003?label=Follow&style=social">
  </a>
  <a href="https://github.com/mdminhaz2003/Telegram-Scraper">
    <img src="https://img.shields.io/github/stars/mdminhaz2003/Telegram-Scraper?style=social">
  </a>
</p>
<p align="center" style="font-family: 'Fantasy';">
  www.yoox.com website scraper
</p>
<p align="center">
</p>

---

Requirements
============
* Python
* Git
* Chrome Driver

Build
=====
To build and run this application locally, you'll need the latest versions of Git, Python and Chrome Driver.


### Clone this repository
```commandline
git clone https://github.com/mdminhaz2003/Yoox-Scraper.git
```

### Go into the repository
```commandline
cd Yoox_Scraper
```
### .env file structure
```text
BASE_URL=https://www.yoox.com/us/women          # Base path should not be changed.
PAGE_URL=https://www.yoox.com/us/men/shoponline/t-shirts%20and%20tops_mc#/dept=clothingmen&gender=U&page=       # Enter your page url here. format should be same 
START_PAGE=1        # Page start
END_PAGE=3          # Page End
DRIVER_PATH=./chrome_driver/linux_64/chromedriver       # Enter your chrome driver path for Mac or Linux
OUTPUT_CSV_PATH=./output_csv/yoox_product_info.csv      # Enter your output CSV file path
```
### Requirements installing
```commandline
python3 -m pip install -r requirements.txt
```
### Scrap only product URL
```commandline
python3 yoox_url_scraper.py
```
### Scrap Product Details
```commandline
python3 yoox_product_scraper.py
```
### Finally, we will get a JSON file [./db_files/yoox_product_info.json](https://github.com/mdminhaz2003/Yoox-Scraper/blob/master/db_files/yoox_product_info.json)
```json
{
  "_default": {
    "1": {
      "Handle": [
        {
          "value": "13778830XE"
        },
        {
          "value": "13778830XE"
        },
        {
          "value": "13778830XE"
        },
        {
          "value": "13778830XE"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "twill, brand logo, solid color, high waisted, belt loops, tapered leg, regular fit, hook-and-eye closure, zipper closure, multipockets"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DONDUP"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Casual pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Pants, Casual pants, DONDUP"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/13778830XE/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Military green"
        },
        {
          "value": "Military green"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "32"
        },
        {
          "value": "36"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "97"
        },
        {
          "value": "97"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13778830XE_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13778830XE_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13778830XE_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13778830XE_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Casual pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13778830XE_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "2": {
      "Handle": [
        {
          "value": "12794851EE"
        },
        {
          "value": "12794851EE"
        },
        {
          "value": "12794851EE"
        },
        {
          "value": "12794851EE"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "plain weave, brand logo, stripes, button-down collar, long sleeves, buttoned cuffs, button closing, no pockets"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "HARMONT&BLAINE"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Striped shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Shirts, Striped shirts, HARMONT&BLAINE"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/12794851EE/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Azure"
        },
        {
          "value": "Azure"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "XXL"
        },
        {
          "value": "3XL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "86"
        },
        {
          "value": "86"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12794851EE_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12794851EE_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12794851EE_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12794851EE_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Striped shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12794851EE_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "3": {
      "Handle": [
        {
          "value": "13642561HP"
        },
        {
          "value": "13642561HP"
        },
        {
          "value": "13642561HP"
        },
        {
          "value": "13642561HP"
        },
        {
          "value": "13642561HP"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "denim, medium wash, brand logo, solid color, hidden buttons, multipockets, stretch, model: d-mihtry, contains non-textile parts of animal origin, mid rise"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Denim pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Jeans and Denim, Denim pants, DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/13642561HP/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Blue"
        },
        {
          "value": "Blue"
        },
        {
          "value": "Blue"
        },
        {
          "value": "Blue"
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "28W-30L"
        },
        {
          "value": "29W-30L"
        },
        {
          "value": "30W-30L"
        },
        {
          "value": "31W-30L"
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "65"
        },
        {
          "value": "65"
        },
        {
          "value": "65"
        },
        {
          "value": "65"
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_e.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "5"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Denim pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13642561HP_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "4": {
      "Handle": [
        {
          "value": "12799619TL"
        },
        {
          "value": "12799619TL"
        },
        {
          "value": "12799619TL"
        },
        {
          "value": "12799619TL"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "plain weave, no appliqués, optical pattern, classic neckline, long sleeves, buttoned cuffs, hidden buttons, no pockets"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DNL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Shirts, Patterned shirts, DNL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/12799619TL/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Black"
        },
        {
          "value": "Black"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "16"
        },
        {
          "value": "16 ½"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "82"
        },
        {
          "value": "82"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12799619TL_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12799619TL_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12799619TL_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12799619TL_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12799619TL_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "5": {
      "Handle": [
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        },
        {
          "value": "12606007RD"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "sweatshirt fleece, brand logo, solid color with print, round collar, long sleeves, no pockets, french terry lining"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Sweatshirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Sweaters and Sweatshirts, Sweatshirts, DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/12606007RD/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "White"
        },
        {
          "value": "Black"
        },
        {
          "value": "White"
        },
        {
          "value": "Black"
        },
        {
          "value": "White"
        },
        {
          "value": "Black"
        },
        {
          "value": "White"
        },
        {
          "value": "Black"
        },
        {
          "value": "White"
        },
        {
          "value": "Black"
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "S"
        },
        {
          "value": "S"
        },
        {
          "value": "M"
        },
        {
          "value": "M"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "XL"
        },
        {
          "value": "XL"
        },
        {
          "value": "XXL"
        },
        {
          "value": "XXL"
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        },
        {
          "value": "41"
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007RD_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007RD_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007RD_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007RD_14_a.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007SH_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007SH_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007SH_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007SH_14_a.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "5"
        },
        {
          "value": "6"
        },
        {
          "value": "7"
        },
        {
          "value": "8"
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Sweatshirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007RD_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12606007SH_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "6": {
      "Handle": [
        {
          "value": "13757132DI"
        },
        {
          "value": "13757132DI"
        },
        {
          "value": "13757132DI"
        },
        {
          "value": "13757132DI"
        }
      ],
      "Title": [
        {
          "value": "MN AUTHENTIC CHINO RELAXED PANT\n"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "gabardine, brand logo, solid color, high waisted, belt loops, straight leg, regular fit, 1 button, zipper closure, five pockets, stretch"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "VANS"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Casual pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Pants, Casual pants, VANS"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/13757132DI/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Sage green"
        },
        {
          "value": "Sage green"
        },
        {
          "value": "Sage green"
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "30"
        },
        {
          "value": "34"
        },
        {
          "value": "36"
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "45"
        },
        {
          "value": "45"
        },
        {
          "value": "45"
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13757132DI_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13757132DI_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13757132DI_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/13/13757132DI_14_e.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Casual pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/13/13757132DI_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "7": {
      "Handle": [
        {
          "value": "12803875RL"
        },
        {
          "value": "12803875RL"
        },
        {
          "value": "12803875RL"
        },
        {
          "value": "12803875RL"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "plain weave, no appliqués, houndstooth, classic neckline, long sleeves, buttoned cuffs, button closing, stretch"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "AT.P.CO"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Shirts, Patterned shirts, AT.P.CO"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/12803875RL/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Blue"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "15 ½"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "70"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12803875RL_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12803875RL_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12803875RL_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12803875RL_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12803875RL_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "8": {
      "Handle": [
        {
          "value": "16077499HJ"
        },
        {
          "value": "16077499HJ"
        },
        {
          "value": "16077499HJ"
        },
        {
          "value": "16077499HJ"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "denim, brand logo, solid color, classic neckline, single-breasted , long sleeves, buttoned cuffs, unlined, button closing, multipockets, light wash"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Denim jacket"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Coats & Jackets, Denim jackets, DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/16077499HJ/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Blue"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "S"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "102"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/16/16077499HJ_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/16/16077499HJ_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/16/16077499HJ_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/16/16077499HJ_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Denim jacket"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/16/16077499HJ_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "9": {
      "Handle": [
        {
          "value": "42855360XU"
        },
        {
          "value": "42855360XU"
        },
        {
          "value": "42855360XU"
        },
        {
          "value": "42855360XU"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "denim, brand logo, solid colour with appliqués, medium wash, mid rise, multipockets, button closing, model: larkee, stretch, contains non-textile parts of animal origin"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Denim pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Jeans and Denim, Denim pants, DIESEL"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/42855360XU/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Blue"
        },
        {
          "value": "Blue"
        },
        {
          "value": "Blue"
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "29W-32L"
        },
        {
          "value": "30W-32L"
        },
        {
          "value": "32W-32L"
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "60"
        },
        {
          "value": "60"
        },
        {
          "value": "60"
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/42/42855360XU_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/42/42855360XU_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/42/42855360XU_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/42/42855360XU_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Denim pants"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/42/42855360XU_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    },
    "10": {
      "Handle": [
        {
          "value": "12804035PD"
        },
        {
          "value": "12804035PD"
        },
        {
          "value": "12804035PD"
        },
        {
          "value": "12804035PD"
        }
      ],
      "Title": [
        {
          "value": "Not Found"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Body (HTML)": [
        {
          "value": "plain weave, no appliqués, floral design, classic neckline, long sleeves, button closing, no pockets"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Vendor": [
        {
          "value": "L.B.K."
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Standardized Product Type": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Custom Product Type": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Tags": [
        {
          "value": "HOME, Men, Shirts, Patterned shirts, L.B.K."
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Published": [
        {
          "value": true
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "ID": [
        {
          "value": "https://www.yoox.com/us/12804035PD/item#dept=clothingmen&sts=SearchResult"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Name": [
        {
          "value": "Color"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option1 Value": [
        {
          "value": "Sky blue"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Name": [
        {
          "value": "Size"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option2 Value": [
        {
          "value": "S"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Name": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Option3 Value": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant SKU": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Grams": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Tracker": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Qty": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Inventory Policy": [
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        },
        {
          "value": "deny"
        }
      ],
      "Variant Fulfillment Service": [
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        },
        {
          "value": "manual"
        }
      ],
      "Variant Price": [
        {
          "value": "74"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Compare At Price": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Requires Shipping": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Taxable": [
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        },
        {
          "value": true
        }
      ],
      "Variant Barcode": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Image Src": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12804035PD_14_f.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12804035PD_14_r.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12804035PD_14_d.jpg"
        },
        {
          "value": "https://cdn.yoox.biz//images/items/12/12804035PD_14_a.jpg"
        }
      ],
      "Image Position": [
        {
          "value": "1"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        }
      ],
      "Image Alt Text": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Gift Card": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Title": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "SEO Description": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Google Product Category": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Gender": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Age Group": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / MPN": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Grouping": [
        {
          "value": "Patterned shirt"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / AdWords Labels": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Condition": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Product": [
        {
          "value": false
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 0": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 1": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 2": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 3": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Google Shopping / Custom Label 4": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Image": [
        {
          "value": "https://cdn.yoox.biz//images/items/12/12804035PD_14_f.jpg"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Variant Weight Unit": [
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        },
        {
          "value": "g"
        }
      ],
      "Variant Tax Code": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Cost per item": [
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ],
      "Status": [
        {
          "value": "active"
        },
        {
          "value": ""
        },
        {
          "value": ""
        },
        {
          "value": ""
        }
      ]
    }
  }
}
```
### Convert JSON to CSV Format
```commandline
python3 json_to_csv_converter.py
```
### Now, we will get a csv file in [./output_csv/yoox_product_info.csv](https://github.com/mdminhaz2003/Yoox-Scraper/blob/master/output_csv/yoox_product_info.csv)
[License](https://github.com/mdminhaz2003/Yoox-Scraper/blob/master/LICENSE.md)
========
```text
The MIT License (MIT)

Copyright (c) 2022 MD. MINHAZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[Connect with Author](https://www.github.com/mdminhaz2003/)
========

<p align="center">
    <a href="https://www.buymeacoffee.com/mdminhaz2003"><img src="https://img.shields.io/badge/-Buy me a coffee-000000?style=for-the-badge&logo=buymeacoffee&logoColor=yellow"/></a>
    <a href="https://www.youtube.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-FF0000?style=for-the-badge&logo=YouTube&logoColor=white"/></a>
    <a href="https://www.facebook.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-3423A6?style=for-the-badge&logo=Facebook&logoColor=white"/></a>
    <a href="https://www.linkedin.com/in/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white"/></a>
    <a href="mailto:mdm047767@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=for-the-badge&logo=Gmail&logoColor=white"/></a>
    <a href="https://instagram.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-E4405F?style=for-the-badge&logo=Instagram&logoColor=white"/></a>
    <a href="https://twitter.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
</p>