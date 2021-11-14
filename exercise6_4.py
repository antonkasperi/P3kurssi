products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y89875_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

query = input("Minkä vuoden koodit haetaan?\n")

matches = []
for order in products:
    if query in order:
        matches.append(x)


# print(matches)