<p align="center"><img src="https://img.shields.io/badge/Version-1.0.1-blue"></p>
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
    "_default":{
        "1":{
            "Handle":[
                "12805515DS",
                "12805515DS",
                "12805515DS",
                "12805515DS"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, brand logo, solid color, round collar, short sleeves, no pockets",
                "",
                "",
                ""
            ],
            "Vendor":[
                "VALVOLA.",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, VALVOLA.",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12805515DS/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Dark blue",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "S",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "44",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12805515DS_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12805515DS_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12805515DS_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12805515DS_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12805515DS_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "2":{
            "Handle":[
                "12781181LM",
                "12781181LM",
                "12781181LM",
                "12781181LM",
                "12781181LM"
            ],
            "Title":[
                "PUMA X AMI \n",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "piqu\u00e9, brand logo, stripes, polo collar, short sleeves, button closing, lifestyle",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "PUMA x AMI ALEXANDRE MATTIUSSI",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "Polo shirt",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, Polo shirts, PUMA x AMI ALEXANDRE MATTIUSSI",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12781181LM/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Bright blue",
                "Bright blue",
                "Bright blue",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "S",
                "M",
                "L",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "106",
                "106",
                "106",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_e.jpg",
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "Polo shirt",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12781181LM_14_f.jpg",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                ""
            ]
        },
        "3":{
            "Handle":[
                "12812195UI",
                "12812195UI",
                "12812195UI",
                "12812195UI",
                "12812195UI",
                "12812195UI",
                "12812195UI",
                "12812195UI"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, brand logo, stripes, round collar, short sleeves, no pockets",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "RVLT/REVOLUTION",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, RVLT/REVOLUTION",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12812195UI/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Light green",
                "Brick red",
                "Light green",
                "Brick red",
                "",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "XL",
                "XL",
                "XXL",
                "XXL",
                "",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "39",
                "39",
                "39",
                "39",
                "",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12812195UI_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195UI_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195UI_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195UI_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195OV_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195OV_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195OV_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195OV_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12812195UI_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12812195OV_14_f.jpg",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        },
        "4":{
            "Handle":[
                "12744147QL",
                "12744147QL",
                "12744147QL",
                "12744147QL"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, brand logo, solid color with print, round collar, short sleeves, no pockets, small sized",
                "",
                "",
                ""
            ],
            "Vendor":[
                "JOHN RICHMOND",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, JOHN RICHMOND",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12744147QL/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "White",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "M",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "82",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12744147QL_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12744147QL_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12744147QL_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12744147QL_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12744147QL_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "5":{
            "Handle":[
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG",
                "12512710HG"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "piqu\u00e9, logo, basic solid color, polo collar, short sleeves, front closure, button closing, no pockets, side slit hemline",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "NORTH SAILS",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "Polo shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, Polo shirts, NORTH SAILS",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12512710HG/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Orange",
                "Green",
                "Azure",
                "Acid green",
                "Fuchsia",
                "Orange",
                "Green",
                "Azure",
                "Acid green",
                "Fuchsia",
                "Orange",
                "Green",
                "Azure",
                "Acid green",
                "Fuchsia",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "XXS",
                "XXS",
                "XXS",
                "XXS",
                "XXS",
                "XS",
                "XS",
                "XS",
                "XS",
                "XS",
                "M",
                "M",
                "M",
                "M",
                "M",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "23",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12512710WS_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710WS_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710WS_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710WS_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710ND_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710ND_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710ND_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710ND_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710GU_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710GU_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710GU_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710GU_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710HG_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710HG_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710HG_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710HG_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710VE_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710VE_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710VE_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710VE_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "Polo shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12512710WS_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710ND_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710GU_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710HG_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12512710VE_14_f.jpg",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        },
        "6":{
            "Handle":[
                "12824611PH",
                "12824611PH",
                "12824611PH",
                "12824611PH"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, no appliqu\u00e9s, multicolor pattern, round collar, short sleeves, no pockets, large sized",
                "",
                "",
                ""
            ],
            "Vendor":[
                "DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12824611PH/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Military green",
                "Military green",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "34",
                "36",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "162",
                "162",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12824611PH_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12824611PH_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12824611PH_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12824611PH_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12824611PH_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "7":{
            "Handle":[
                "12824419FX",
                "12824419FX",
                "12824419FX",
                "12824419FX"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, brand logo, multicolor pattern, round collar, short sleeves, no pockets, large sized",
                "",
                "",
                ""
            ],
            "Vendor":[
                "DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12824419FX/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Green",
                "Green",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "34",
                "36",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "153",
                "153",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12824419FX_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12824419FX_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12824419FX_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12824419FX_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12824419FX_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "8":{
            "Handle":[
                "12761198SO",
                "12761198SO",
                "12761198SO",
                "12761198SO"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, brand logo, solid color with print, round collar, short sleeves",
                "",
                "",
                ""
            ],
            "Vendor":[
                "OFF-WHITE\u2122",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, OFF-WHITE\u2122",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12761198SO/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Black",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "XS",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "228",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12761198SO_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12761198SO_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12761198SO_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12761198SO_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12761198SO_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "9":{
            "Handle":[
                
            ],
            "Title":[
                "Not Found"
            ],
            "Body (HTML)":[
                "piqu\u00e9, logo, multicolor pattern, polo collar, short sleeves, no pockets, stretch, large sized"
            ],
            "Vendor":[
                "DOLCE & GABBANA"
            ],
            "Standardized Product Type":[
                
            ],
            "Custom Product Type":[
                "Polo shirt"
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, Polo shirts, DOLCE & GABBANA"
            ],
            "Published":[
                true
            ],
            "ID":[
                "https://www.yoox.com/us/12566304SH/item#dept=clothingmen&sts=SearchResult"
            ],
            "Option1 Name":[
                "Color"
            ],
            "Option1 Value":[
                
            ],
            "Option2 Name":[
                "Size"
            ],
            "Option2 Value":[
                
            ],
            "Option3 Name":[
                
            ],
            "Option3 Value":[
                
            ],
            "Variant SKU":[
                
            ],
            "Variant Grams":[
                
            ],
            "Variant Inventory Tracker":[
                
            ],
            "Variant Inventory Qty":[
                
            ],
            "Variant Inventory Policy":[
                
            ],
            "Variant Fulfillment Service":[
                
            ],
            "Variant Price":[
                
            ],
            "Variant Compare At Price":[
                
            ],
            "Variant Requires Shipping":[
                
            ],
            "Variant Taxable":[
                
            ],
            "Variant Barcode":[
                
            ],
            "Image Src":[
                
            ],
            "Image Position":[
                
            ],
            "Image Alt Text":[
                
            ],
            "Gift Card":[
                false
            ],
            "SEO Title":[
                
            ],
            "SEO Description":[
                
            ],
            "Google Shopping / Google Product Category":[
                
            ],
            "Google Shopping / Gender":[
                
            ],
            "Google Shopping / Age Group":[
                
            ],
            "Google Shopping / MPN":[
                
            ],
            "Google Shopping / AdWords Grouping":[
                "Polo shirt"
            ],
            "Google Shopping / AdWords Labels":[
                
            ],
            "Google Shopping / Condition":[
                
            ],
            "Google Shopping / Custom Product":[
                false
            ],
            "Google Shopping / Custom Label 0":[
                
            ],
            "Google Shopping / Custom Label 1":[
                
            ],
            "Google Shopping / Custom Label 2":[
                
            ],
            "Google Shopping / Custom Label 3":[
                
            ],
            "Google Shopping / Custom Label 4":[
                
            ],
            "Variant Image":[
                
            ],
            "Variant Weight Unit":[
                
            ],
            "Variant Tax Code":[
                
            ],
            "Cost per item":[
                
            ],
            "Status":[
                "active"
            ]
        },
        "10":{
            "Handle":[
                "12012579BG",
                "12012579BG",
                "12012579BG",
                "12012579BG"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "Jersey<br>Solid color<br>Round collar<br>Long sleeves<br>Logo<br>Front closure<br>Button closing<br>No pockets<br>Large sized<br>",
                "",
                "",
                ""
            ],
            "Vendor":[
                "DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, DOLCE & GABBANA",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12012579BG/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Camel",
                "Camel",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "34",
                "36",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "93",
                "93",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12012579BG_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12012579BG_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12012579BG_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12012579BG_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12012579BG_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "11":{
            "Handle":[
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC",
                "12582930SC"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, logo, solid color with print, round collar, short sleeves, no pockets",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12582930SC/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Red",
                "Dark blue",
                "Bright blue",
                "Red",
                "Dark blue",
                "Bright blue",
                "Red",
                "Dark blue",
                "Bright blue",
                "Red",
                "Dark blue",
                "Bright blue"
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "M",
                "M",
                "M",
                "L",
                "L",
                "L",
                "XL",
                "XL",
                "XL",
                "XXL",
                "XXL",
                "XXL"
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44",
                "44"
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12582930SC_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930SC_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930SC_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930SC_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930GD_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930GD_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930GD_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930GD_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930JN_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930JN_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930JN_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930JN_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12582930SC_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930GD_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582930JN_14_f.jpg",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        },
        "12":{
            "Handle":[
                "12573156FE",
                "12573156FE",
                "12573156FE",
                "12573156FE",
                "12573156FE",
                "12573156FE"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, logo, solid color with print, round collar, short sleeves, no pockets",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12573156FE/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Grey",
                "Black",
                "Grey",
                "Black",
                "Grey",
                "Black"
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "S",
                "S",
                "M",
                "M",
                "L",
                "L"
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "69",
                "69",
                "69",
                "69",
                "69",
                "69"
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12573156FE_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12573156FE_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12573156TB_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12573156TB_14_r.jpg",
                "",
                ""
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "",
                ""
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12573156FE_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12573156TB_14_f.jpg",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                ""
            ]
        },
        "13":{
            "Handle":[
                "12821737QK",
                "12821737QK",
                "12821737QK",
                "12821737QK",
                "12821737QK",
                "12821737QK",
                "12821737QK",
                "12821737QK"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, studs, solid color, round collar, short sleeves, no pockets",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "VALENTINO",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "Basic T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, Basic T-shirt, VALENTINO",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12821737QK/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Black",
                "White",
                "Black",
                "White",
                "",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "S",
                "S",
                "3XL",
                "3XL",
                "",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "380",
                "380",
                "380",
                "380",
                "",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12821737QK_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737QK_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737QK_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737QK_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737HI_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737HI_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737HI_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737HI_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "Basic T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12821737QK_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12821737HI_14_f.jpg",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        },
        "14":{
            "Handle":[
                "12675419IG",
                "12675419IG",
                "12675419IG",
                "12675419IG"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "piqu\u00e9, brand logo, solid color, polo collar, short sleeves, 3 buttons, no pockets",
                "",
                "",
                ""
            ],
            "Vendor":[
                "BURBERRY",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "Polo shirt",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, Polo shirts, BURBERRY",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12675419IG/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Dark blue",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "XS",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "86",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12675419IG_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12675419IG_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12675419IG_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12675419IG_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "Polo shirt",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12675419IG_14_f.jpg",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                ""
            ]
        },
        "15":{
            "Handle":[
                "12528441TX",
                "12528441TX"
            ],
            "Title":[
                "Not Found",
                ""
            ],
            "Body (HTML)":[
                "jersey, contrasting applications, solid color, round collar, short sleeves, no pockets, large sized",
                ""
            ],
            "Vendor":[
                "DOLCE & GABBANA",
                ""
            ],
            "Standardized Product Type":[
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, DOLCE & GABBANA",
                ""
            ],
            "Published":[
                true,
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12528441TX/item#dept=clothingmen&sts=SearchResult",
                ""
            ],
            "Option1 Name":[
                "Color",
                ""
            ],
            "Option1 Value":[
                "Military green",
                "Military green"
            ],
            "Option2 Name":[
                "Size",
                ""
            ],
            "Option2 Value":[
                "34",
                "36"
            ],
            "Option3 Name":[
                "",
                ""
            ],
            "Option3 Value":[
                "",
                ""
            ],
            "Variant SKU":[
                "",
                ""
            ],
            "Variant Grams":[
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual"
            ],
            "Variant Price":[
                "114",
                "114"
            ],
            "Variant Compare At Price":[
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true
            ],
            "Variant Barcode":[
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12528441TX_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12528441TX_14_r.jpg"
            ],
            "Image Position":[
                "1",
                "2"
            ],
            "Image Alt Text":[
                "",
                ""
            ],
            "Gift Card":[
                false,
                ""
            ],
            "SEO Title":[
                "",
                ""
            ],
            "SEO Description":[
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12528441TX_14_f.jpg",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                ""
            ],
            "Cost per item":[
                "",
                ""
            ],
            "Status":[
                "active",
                ""
            ]
        },
        "16":{
            "Handle":[
                "12582937CH",
                "12582937CH",
                "12582937CH",
                "12582937CH",
                "12582937CH",
                "12582937CH",
                "12582937CH",
                "12582937CH"
            ],
            "Title":[
                "Not Found",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Body (HTML)":[
                "jersey, logo, solid color with print, round collar, short sleeves, no pockets",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Vendor":[
                "ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Standardized Product Type":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Custom Product Type":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Tags":[
                "HOME, Men, T-Shirts and Tops, T-shirts, ROBERTO CAVALLI",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Published":[
                true,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ID":[
                "https://www.yoox.com/us/12582937CH/item#dept=clothingmen&sts=SearchResult",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Name":[
                "Color",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option1 Value":[
                "Red",
                "Dark blue",
                "Red",
                "Dark blue",
                "",
                "",
                "",
                ""
            ],
            "Option2 Name":[
                "Size",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option2 Value":[
                "XL",
                "XL",
                "XXL",
                "XXL",
                "",
                "",
                "",
                ""
            ],
            "Option3 Name":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Option3 Value":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant SKU":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Grams":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Tracker":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Qty":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Inventory Policy":[
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny",
                "deny"
            ],
            "Variant Fulfillment Service":[
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual",
                "manual"
            ],
            "Variant Price":[
                "55",
                "55",
                "55",
                "55",
                "",
                "",
                "",
                ""
            ],
            "Variant Compare At Price":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Requires Shipping":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Taxable":[
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "Variant Barcode":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Image Src":[
                "https://cdn.yoox.biz//images/items/12/12582937CH_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937CH_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937CH_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937CH_14_a.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937LL_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937LL_14_r.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937LL_14_d.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937LL_14_a.jpg"
            ],
            "Image Position":[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"
            ],
            "Image Alt Text":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Gift Card":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Title":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "SEO Description":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Google Product Category":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Gender":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Age Group":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / MPN":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Grouping":[
                "T-shirt",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / AdWords Labels":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Condition":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Product":[
                false,
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 0":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 1":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 2":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 3":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Google Shopping / Custom Label 4":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Image":[
                "https://cdn.yoox.biz//images/items/12/12582937CH_14_f.jpg",
                "https://cdn.yoox.biz//images/items/12/12582937LL_14_f.jpg",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Variant Weight Unit":[
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g",
                "g"
            ],
            "Variant Tax Code":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Cost per item":[
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "Status":[
                "active",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
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