def value_adder(max_value: int, data_set: list, value: dict) -> None:
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

        self.title = [{"value": title}]
        self.body_html = [{"value": body_html}]
        self.vendor_text = [{"value": vendor}]
        self.custom_product_type = [{"value": custom_product_type}]
        self.tags = [{"value": tags}]
        self.product_id = [{"value": product_id}]

        self.published = [{"value": True}]
        self.option_one_name = [{"value": "Color"}]
        self.option_two_name = [{"value": "Size"}]
        self.gift_card = [{"value": False}]
        self.google_custom_product = [{"value": False}]
        self.status = [{"value": "active"}]

        self.initial_colors = colors
        self.colors = []

        self.initial_sizes = sizes
        self.sizes = []

        self.initial_price = price
        self.price = []

        self.initial_image_src = image_src
        self.image_src = []

        self.initial_image_position = image_position
        self.image_position = []

        self.initial_variant_image = variant_image
        self.variant_image = []

        self.handle = []
        self.variant_inventory_policy = []
        self.variant_fulfilment_service = []
        self.variant_require_shipping = []
        self.variant_taxable = []
        self.variant_weight_unit = []

    def initial_list_formatter(self):
        for color in self.initial_colors:
            self.colors.append({"value": color})

        for size in self.initial_sizes:
            self.sizes.append({"value": size})

        for price in self.initial_price:
            self.price.append({"value": price})

        for image_src in self.initial_image_src:
            self.image_src.append({"value": image_src})

        for image_position in self.initial_image_position:
            self.image_position.append({"value": image_position})

        for variant_image in self.initial_variant_image:
            self.variant_image.append({"value": variant_image})

    def list_equal(self) -> None:
        self.initial_list_formatter()

        max_value = max(len(self.colors), len(self.sizes), len(self.image_src))
        if max_value == len(self.colors) == len(self.sizes) == len(self.image_src) == len(self.variant_image):
            value_adder(max_value=max_value, data_set=self.handle, value={"value": self.handle_text})
            value_adder(max_value=max_value, data_set=self.variant_inventory_policy, value={"value": "deny"})
            value_adder(max_value=max_value, data_set=self.variant_fulfilment_service, value={"value": "manual"})
            value_adder(max_value=max_value, data_set=self.variant_require_shipping, value={"value": True})
            value_adder(max_value=max_value, data_set=self.variant_taxable, value={"value": True})
            value_adder(max_value=max_value, data_set=self.variant_weight_unit, value={"value": "g"})

            value_adder(max_value=max_value, data_set=self.title, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.body_html, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.vendor_text, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.custom_product_type, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.tags, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.product_id, value={"value": ""})

            value_adder(max_value=max_value, data_set=self.published, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.option_one_name, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.option_two_name, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.gift_card, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.google_custom_product, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.status, value={"value": ""})

        else:
            value_adder(max_value=max_value, data_set=self.handle, value={"value": self.handle_text})
            value_adder(max_value=max_value, data_set=self.variant_inventory_policy, value={"value": "deny"})
            value_adder(max_value=max_value, data_set=self.variant_fulfilment_service, value={"value": "manual"})
            value_adder(max_value=max_value, data_set=self.variant_require_shipping, value={"value": True})
            value_adder(max_value=max_value, data_set=self.variant_taxable, value={"value": True})
            value_adder(max_value=max_value, data_set=self.variant_weight_unit, value={"value": "g"})

            value_adder(max_value=max_value, data_set=self.title, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.body_html, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.vendor_text, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.custom_product_type, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.tags, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.product_id, value={"value": ""})

            value_adder(max_value=max_value, data_set=self.published, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.option_one_name, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.option_two_name, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.gift_card, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.google_custom_product, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.status, value={"value": ""})

            value_adder(max_value=max_value, data_set=self.colors, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.sizes, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.price, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.image_src, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.image_position, value={"value": ""})
            value_adder(max_value=max_value, data_set=self.variant_image, value={"value": ""})

    def main_dict(self) -> dict:
        self.list_equal()
        data = {
            "Handle": self.handle,
            "Title": self.title,
            "Body (HTML)": self.body_html,
            "Vendor": self.vendor_text,
            "Standardized Product Type": [{"value": "" for _ in self.handle}],
            "Custom Product Type": self.custom_product_type,
            "Tags": self.tags,
            "Published": self.published,
            "ID": self.product_id,
            "Option1 Name": self.option_one_name,
            "Option1 Value": self.colors,
            "Option2 Name": self.option_two_name,
            "Option2 Value": self.sizes,
            "Option3 Name": [{"value": "" for _ in self.handle}],
            "Option3 Value": [{"value": "" for _ in self.handle}],
            "Variant SKU": [{"value": "" for _ in self.handle}],
            "Variant Grams": [{"value": "" for _ in self.handle}],
            "Variant Inventory Tracker": [{"value": "" for _ in self.handle}],
            "Variant Inventory Qty": [{"value": "" for _ in self.handle}],
            "Variant Inventory Policy": self.variant_inventory_policy,
            "Variant Fulfillment Service": self.variant_fulfilment_service,
            "Variant Price": self.price,
            "Variant Compare At Price": [{"value": "" for _ in self.handle}],
            "Variant Requires Shipping": self.variant_require_shipping,
            "Variant Taxable": self.variant_taxable,
            "Variant Barcode": [{"value": "" for _ in self.handle}],
            "Image Src": self.image_src,
            "Image Position": self.image_position,
            "Image Alt Text": [{"value": "" for _ in self.handle}],
            "Gift Card": self.gift_card,
            "SEO Title": [{"value": "" for _ in self.handle}],
            "SEO Description": [{"value": "" for _ in self.handle}],
            "Google Shopping / Google Product Category": [{"value": "" for _ in self.handle}],
            "Google Shopping / Gender": [{"value": "" for _ in self.handle}],
            "Google Shopping / Age Group": [{"value": "" for _ in self.handle}],
            "Google Shopping / MPN": [{"value": "" for _ in self.handle}],
            "Google Shopping / AdWords Grouping": self.custom_product_type,
            "Google Shopping / AdWords Labels": [{"value": "" for _ in self.handle}],
            "Google Shopping / Condition": [{"value": "" for _ in self.handle}],
            "Google Shopping / Custom Product": self.google_custom_product,
            "Google Shopping / Custom Label 0": [{"value": "" for _ in self.handle}],
            "Google Shopping / Custom Label 1": [{"value": "" for _ in self.handle}],
            "Google Shopping / Custom Label 2": [{"value": "" for _ in self.handle}],
            "Google Shopping / Custom Label 3": [{"value": "" for _ in self.handle}],
            "Google Shopping / Custom Label 4": [{"value": "" for _ in self.handle}],
            "Variant Image": self.variant_image,
            "Variant Weight Unit": self.variant_weight_unit,
            "Variant Tax Code": [{"value": "" for _ in self.handle}],
            "Cost per item": [{"value": "" for _ in self.handle}],
            "Status": self.status
        }
        return data
