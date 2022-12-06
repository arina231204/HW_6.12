import random

from credit.models import Client,Account, Credit


client1 = Client.objects.create(name='Бердиев Н.Д.', citizenship='КР', birth_year='1994-12-12', work_place='Codify')
account1 = Account.objects.create(number = random.randint(1000000000000000,10000000000000000), account_type=1, client=client1)
account2 = Account.objects.create(number = random.randint(1000000000000000,10000000000000000), account_type=2, client=client1)
account1.accounts.create(sum=20000)
account2.accounts.create(sum=5555)

client2 = Client.objects.create(name='Nina F.J.', citizenship='UK', birth_year='2000-09-12')
account1 = Account.objects.create(number = random.randint(1000000000000000,10000000000000000), account_type=1, client=client2)
account2 = Account.objects.create(number = random.randint(1000000000000000,10000000000000000), account_type=2, client=client2)
account1.accounts.create(sum=23424)
account2.accounts.create(sum=520555)

