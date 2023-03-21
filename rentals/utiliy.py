def calculate_total_price(price, Days, hourss):
    if isinstance(price, str):
        price = int(price)
    if isinstance(days, str):
        days = int(days)
        days = days * 24
        total = days * price
    else:
        if isinstance(hourss, str):
            time = int(hourss)
        total = time * price
    return total