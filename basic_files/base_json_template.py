def value_adder(max_value: int, data_set: list, value: str | bool) -> None:
    if max_value > len(data_set):
        difference_between = max_value - len(data_set)
        for _ in range(difference_between):
            data_set.append(value)
    else:
        pass


class JsonTemplate:
    def __init__(
            self,
            handle_text: str,
            title: str,
            body_html: str,
            vendor: str,
            custom_product_type: str,
            tags: str,
            product_id: str,
            colors: list,
            sizes: list,
            price: list,
            image_src: list,
            image_position: list,
            variant_image: list
    ) -> None:
        self.handle_text = handle_text
        self.title = [title]
        self.body_html = [body_html]
        self.vendor_text = [vendor]
        self.custom_product_type = [custom_product_type]
        self.tags = [tags]
        self.product_id = [product_id]

        self.published = [True]
        self.option_one_name = ['Color']
        self.option_two_name = ['Size']
        self.gift_card = [False]
        self.google_custom_product = [False]
        self.status = ['active']

        self.colors = colors
        self.sizes = sizes
        self.price = price
        self.image_src = image_src
        self.image_position = image_position
        self.variant_image = variant_image
        self.handle = []
        self.variant_inventory_policy = []
        self.variant_fulfilment_service = []
        self.variant_require_shipping = []
        self.variant_taxable = []
        self.variant_weight_unit = []

    def list_equal(self) -> None:
        max_value = max(len(self.colors), len(self.sizes), len(self.image_src))
        if max_value == len(self.colors) == len(self.sizes) == len(self.image_src) == len(self.variant_image):
            value_adder(max_value=max_value, data_set=self.handle, value=self.handle_text)
            value_adder(max_value=max_value, data_set=self.variant_inventory_policy, value="deny")
            value_adder(max_value=max_value, data_set=self.variant_fulfilment_service, value="manual")
            value_adder(max_value=max_value, data_set=self.variant_require_shipping, value=True)
            value_adder(max_value=max_value, data_set=self.variant_taxable, value=True)
            value_adder(max_value=max_value, data_set=self.variant_weight_unit, value="g")

            value_adder(max_value=max_value, data_set=self.title, value="")
            value_adder(max_value=max_value, data_set=self.body_html, value="")
            value_adder(max_value=max_value, data_set=self.vendor_text, value="")
            value_adder(max_value=max_value, data_set=self.custom_product_type, value="")
            value_adder(max_value=max_value, data_set=self.tags, value="")
            value_adder(max_value=max_value, data_set=self.product_id, value="")

            value_adder(max_value=max_value, data_set=self.published, value="")
            value_adder(max_value=max_value, data_set=self.option_one_name, value="")
            value_adder(max_value=max_value, data_set=self.option_two_name, value="")
            value_adder(max_value=max_value, data_set=self.gift_card, value="")
            value_adder(max_value=max_value, data_set=self.google_custom_product, value="")
            value_adder(max_value=max_value, data_set=self.status, value="")
        else:
            value_adder(max_value=max_value, data_set=self.handle, value=self.handle_text)
            value_adder(max_value=max_value, data_set=self.variant_inventory_policy, value="deny")
            value_adder(max_value=max_value, data_set=self.variant_fulfilment_service, value="manual")
            value_adder(max_value=max_value, data_set=self.variant_require_shipping, value=True)
            value_adder(max_value=max_value, data_set=self.variant_taxable, value=True)
            value_adder(max_value=max_value, data_set=self.variant_weight_unit, value="g")

            value_adder(max_value=max_value, data_set=self.colors, value="")
            value_adder(max_value=max_value, data_set=self.sizes, value="")
            value_adder(max_value=max_value, data_set=self.price, value="")
            value_adder(max_value=max_value, data_set=self.image_src, value="")
            value_adder(max_value=max_value, data_set=self.image_position, value="")
            value_adder(max_value=max_value, data_set=self.variant_image, value="")

            value_adder(max_value=max_value, data_set=self.title, value="")
            value_adder(max_value=max_value, data_set=self.body_html, value="")
            value_adder(max_value=max_value, data_set=self.vendor_text, value="")
            value_adder(max_value=max_value, data_set=self.custom_product_type, value="")
            value_adder(max_value=max_value, data_set=self.tags, value="")
            value_adder(max_value=max_value, data_set=self.product_id, value="")

            value_adder(max_value=max_value, data_set=self.published, value="")
            value_adder(max_value=max_value, data_set=self.option_one_name, value="")
            value_adder(max_value=max_value, data_set=self.option_two_name, value="")
            value_adder(max_value=max_value, data_set=self.gift_card, value="")
            value_adder(max_value=max_value, data_set=self.google_custom_product, value="")
            value_adder(max_value=max_value, data_set=self.status, value="")

    def main_dict(self) -> dict:
        self.list_equal()
        data = {
            "Handle": self.handle,
            "Title": self.title,
            "Body (HTML)": self.body_html,
            "Vendor": self.vendor_text,
            "Standardized Product Type": ["" for _ in self.handle],
            "Custom Product Type": self.custom_product_type,
            "Tags": self.tags,
            "Published": self.published,
            "ID": self.product_id,
            "Option1 Name": self.option_one_name,
            "Option1 Value": self.colors,
            "Option2 Name": self.option_two_name,
            "Option2 Value": self.sizes,
            "Option3 Name": ["" for _ in self.handle],
            "Option3 Value": ["" for _ in self.handle],
            "Variant SKU": ["" for _ in self.handle],
            "Variant Grams": ["" for _ in self.handle],
            "Variant Inventory Tracker": ["" for _ in self.handle],
            "Variant Inventory Qty": ["" for _ in self.handle],
            "Variant Inventory Policy": self.variant_inventory_policy,
            "Variant Fulfillment Service": self.variant_fulfilment_service,
            "Variant Price": self.price,
            "Variant Compare At Price": ["" for _ in self.handle],
            "Variant Requires Shipping": self.variant_require_shipping,
            "Variant Taxable": self.variant_taxable,
            "Variant Barcode": ["" for _ in self.handle],
            "Image Src": self.image_src,
            "Image Position": self.image_position,
            "Image Alt Text": ["" for _ in self.handle],
            "Gift Card": self.gift_card,
            "SEO Title": ["" for _ in self.handle],
            "SEO Description": ["" for _ in self.handle],
            "Google Shopping / Google Product Category": ["" for _ in self.handle],
            "Google Shopping / Gender": ["" for _ in self.handle],
            "Google Shopping / Age Group": ["" for _ in self.handle],
            "Google Shopping / MPN": ["" for _ in self.handle],
            "Google Shopping / AdWords Grouping": self.custom_product_type,
            "Google Shopping / AdWords Labels": ["" for _ in self.handle],
            "Google Shopping / Condition": ["" for _ in self.handle],
            "Google Shopping / Custom Product": self.google_custom_product,
            "Google Shopping / Custom Label 0": ["" for _ in self.handle],
            "Google Shopping / Custom Label 1": ["" for _ in self.handle],
            "Google Shopping / Custom Label 2": ["" for _ in self.handle],
            "Google Shopping / Custom Label 3": ["" for _ in self.handle],
            "Google Shopping / Custom Label 4": ["" for _ in self.handle],
            "Variant Image": self.variant_image,
            "Variant Weight Unit": self.variant_weight_unit,
            "Variant Tax Code": ["" for _ in self.handle],
            "Cost per item": ["" for _ in self.handle],
            "Status": self.status
        }
        return data

