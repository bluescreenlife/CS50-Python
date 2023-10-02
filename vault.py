class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts."

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.galleons + other.galleons
        knuts = self.galleons + other.galleons
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

# total = Vault(galleons, sickles, knuts)
# print(total)


# instead, overload operator and allow adding of vaults - see __add__ function above

total = potter + weasley # py has now been taught what it means to add 2 variables of these types (vaults)
print(total)

