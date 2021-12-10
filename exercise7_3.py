# ostoskori
shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
    ]

# silmukoidaan lista tuotteista
print("Kuitti ostoksista:")
for item in shopcart:
    print("- " + item['name'])
print()

# list comprehensionilla otetaan hinnat omaksi listakseen
prices = [sub['price'] for sub in shopcart]

# lasketaan kokonaishinta ja VAT
totalprice = 0
for sums in prices:
    totalprice = totalprice + sums
vat = totalprice - (totalprice / 1.24)
vat = round(vat, 2)

# tulostetaan
print(f'Yhteensä {totalprice} €.')
print(f'ALV:n osuus: {vat} €.')
print('Tervetuloa uudelleen!')


#price = product['price']
