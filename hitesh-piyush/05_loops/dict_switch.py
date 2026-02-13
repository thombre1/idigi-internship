users = [
    {"id": 1, "total": 400, "coupon":"F50"},
    {"id": 2, "total": 200, "coupon":"F10"},
    {"id": 3, "total": 100, "coupon":"P50"}
]

discount = {
    "F50": (0.2,0),
    "F10": (0.5,0),
    "P50": (0.2,10)
}

# the elements will be destructured on their own
for user in users:
    percent,flat = discount[user["coupon"]]
    minusValue = user["total"] * percent + flat
    print(f"{user["id"]} get minusValue: {minusValue}")


