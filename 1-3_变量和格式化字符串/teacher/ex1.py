retail_price = 2
purchase_price = 0.5
quantity_per_box = 100
profit_per_unit = retail_price - purchase_price

print("\n总进价：", purchase_price * quantity_per_box, "元。")
print("总利润：", retail_price * quantity_per_box, "元。")
print("每件毛利润：", profit_per_unit, "元。")
print("总毛利润：", profit_per_unit * quantity_per_box, "元。\n")
