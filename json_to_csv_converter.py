import csv
from dotenv import dotenv_values
from tinydb import TinyDB


config = dotenv_values(dotenv_path='./.env')
db = TinyDB('./db_files/yoox_product_info.json')
all_data = db.all()

headers = [key for key in all_data[0].keys()]


def row_data_creator(
        handle: str,
        title: str,
        body_html: str,
        vendor: str,
        standardized_product_type: str,
        custom_product_type: str,
        tags: str,
        published: str,
        product_id: str,
        option_one_name: str,
        option_one_value: str,
        option_two_name: str,
        option_two_value: str,
        option_three_name: str,
        option_three_value: str,
        variant_sku: str,
        variant_grams: str,
        variant_inventory_tracker: str,
        variant_inventory_qty: str,
        variant_inventory_policy: str,
        variant_fulfillment_service: str,
        variant_price: str,
        variant_compare_at_price: str,
        variant_requires_shipping: str,
        variant_taxable: str,
        variant_barcode: str,
        image_src: str,
        image_position: str,
        image_alt_text: str,
        gift_card: str,
        seo_title: str,
        seo_description: str,
        google_product_category: str,
        google_gender: str,
        google_age_group: str,
        google_mpn: str,
        google_adwords_grouping: str,
        google_adwords_labels: str,
        google_condition: str,
        google_custom_product: str,
        google_custom_label_0: str,
        google_custom_label_1: str,
        google_custom_label_2: str,
        google_custom_label_3: str,
        google_custom_label_4: str,
        variant_image: str,
        variant_weight_unit: str,
        variant_tax_code: str,
        cost_per_item: str,
        status: str
) -> dict:
    return {
        'Handle': handle,
        'Title': title,
        'Body (HTML)': body_html,
        'Vendor': vendor,
        'Standardized Product Type': standardized_product_type,
        'Custom Product Type': custom_product_type,
        'Tags': tags,
        'Published': published,
        'ID': product_id,
        'Option1 Name': option_one_name,
        'Option1 Value': option_one_value,
        'Option2 Name': option_two_name,
        'Option2 Value': option_two_value,
        'Option3 Name': option_three_name,
        'Option3 Value': option_three_value,
        'Variant SKU': variant_sku,
        'Variant Grams': variant_grams,
        'Variant Inventory Tracker': variant_inventory_tracker,
        'Variant Inventory Qty': variant_inventory_qty,
        'Variant Inventory Policy': variant_inventory_policy,
        'Variant Fulfillment Service': variant_fulfillment_service,
        'Variant Price': variant_price,
        'Variant Compare At Price': variant_compare_at_price,
        'Variant Requires Shipping': variant_requires_shipping,
        'Variant Taxable': variant_taxable,
        'Variant Barcode': variant_barcode,
        'Image Src': image_src,
        'Image Position': image_position,
        'Image Alt Text': image_alt_text,
        'Gift Card': gift_card,
        'SEO Title': seo_title,
        'SEO Description': seo_description,
        'Google Shopping / Google Product Category': google_product_category,
        'Google Shopping / Gender': google_gender,
        'Google Shopping / Age Group': google_age_group,
        'Google Shopping / MPN': google_mpn,
        'Google Shopping / AdWords Grouping': google_adwords_grouping,
        'Google Shopping / AdWords Labels': google_adwords_labels,
        'Google Shopping / Condition': google_condition,
        'Google Shopping / Custom Product': google_custom_product,
        'Google Shopping / Custom Label 0': google_custom_label_0,
        'Google Shopping / Custom Label 1': google_custom_label_1,
        'Google Shopping / Custom Label 2': google_custom_label_2,
        'Google Shopping / Custom Label 3': google_custom_label_3,
        'Google Shopping / Custom Label 4': google_custom_label_4,
        'Variant Image': variant_image,
        'Variant Weight Unit': variant_weight_unit,
        'Variant Tax Code': variant_tax_code,
        'Cost per item': cost_per_item,
        'Status': status
    }


with open(file=config['OUTPUT_CSV_PATH'], mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(f=file, fieldnames=headers)

    writer.writeheader()

    for product in all_data:
        index = 0

        for _ in product.get('Handle'):
            row = row_data_creator(
                product.get('Handle')[index]["value"],
                product.get('Title')[index]["value"],
                product.get('Body (HTML)')[index]["value"],
                product.get('Vendor')[index]["value"],
                product.get('Standardized Product Type')[index]["value"],
                product.get('Custom Product Type')[index]["value"],
                product.get('Tags')[index]["value"],
                product.get('Published')[index]["value"],
                product.get('ID')[index]["value"],
                product.get('Option1 Name')[index]["value"],
                product.get('Option1 Value')[index]["value"],
                product.get('Option2 Name')[index]["value"],
                product.get('Option2 Value')[index]["value"],
                product.get('Option3 Name')[index]["value"],
                product.get('Option3 Value')[index]["value"],
                product.get('Variant SKU')[index]["value"],
                product.get('Variant Grams')[index]["value"],
                product.get('Variant Inventory Tracker')[index]["value"],
                product.get('Variant Inventory Qty')[index]["value"],
                product.get('Variant Inventory Policy')[index]["value"],
                product.get('Variant Fulfillment Service')[index]["value"],
                product.get('Variant Price')[index]["value"],
                product.get('Variant Compare At Price')[index]["value"],
                product.get('Variant Requires Shipping')[index]["value"],
                product.get('Variant Taxable')[index]["value"],
                product.get('Variant Barcode')[index]["value"],
                product.get('Image Src')[index]["value"],
                product.get('Image Position')[index]["value"],
                product.get('Image Alt Text')[index]["value"],
                product.get('Gift Card')[index]["value"],
                product.get('SEO Title')[index]["value"],
                product.get('SEO Description')[index]["value"],
                product.get('Google Shopping / Google Product Category')[index]["value"],
                product.get('Google Shopping / Gender')[index]["value"],
                product.get('Google Shopping / Age Group')[index]["value"],
                product.get('Google Shopping / MPN')[index]["value"],
                product.get('Google Shopping / AdWords Grouping')[index]["value"],
                product.get('Google Shopping / AdWords Labels')[index]["value"],
                product.get('Google Shopping / Condition')[index]["value"],
                product.get('Google Shopping / Custom Product')[index]["value"],
                product.get('Google Shopping / Custom Label 0')[index]["value"],
                product.get('Google Shopping / Custom Label 1')[index]["value"],
                product.get('Google Shopping / Custom Label 2')[index]["value"],
                product.get('Google Shopping / Custom Label 3')[index]["value"],
                product.get('Google Shopping / Custom Label 4')[index]["value"],
                product.get('Variant Image')[index]["value"],
                product.get('Variant Weight Unit')[index]["value"],
                product.get('Variant Tax Code')[index]["value"],
                product.get('Cost per item')[index]["value"],
                product.get('Status')[index]["value"]
            )

            writer.writerow(rowdict=row)
            index += 1

