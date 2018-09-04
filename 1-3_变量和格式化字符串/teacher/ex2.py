retail_price = 1.5
purchase_price = 0.5

quantity_per_box = 100
box_to_sell = 50
total_quantity = quantity_per_box * box_to_sell

profit_per_unit = retail_price - purchase_price
total_profit = profit_per_unit * total_quantity

total_commission = retail_price * total_quantity * 0.05



print("\n总进价：", purchase_price * total_quantity, "元。")
print("总利润：", retail_price * total_quantity, "元。")
print("每件毛利润：", profit_per_unit, "元。")
print("总毛利润：", total_profit, "元。")
print("老王的总提成：", total_commission, "元。")
print("提成后总毛利润：",total_profit - total_commission, "元。\n")
