

# from datetime import datetime

# print(datetime.now().date())


# from django.db import models
# from datetime import datetime
# punch_date = models.DateTimeField(default=datetime.now)
# for x in dir(punch_date):
#     print(x)


# for x in list(map(lambda x: x * 2, [1, 2, 3, 4])):
#     print(x)


import decimal

dec1 = decimal.Decimal('0.2')
dec2 = decimal.Decimal(0.2)

print(dec1)
print(dec2)
print(dec1 == dec2)
