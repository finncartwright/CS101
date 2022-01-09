#British Tax calculator!
class TaxPayer:
    capital_gains_rate = 0.1

    def __init__(self, name, age, address, income, capital_gains):
        self.name = name
        self.age = int(age)
        self.address = address
        self.income = float(income.strip(','))
        self.capital_gains = float(capital_gains.strip(','))
        self.total_tax = 0
        if self.income >= 100000:
            self.capital_gains_rate = 0.2
    
    def __repr__(self):
        print("{} at {}.".format(self.name, self.address))
    
    def total_tax_calculation(self):
        self.income_tax = self.income_tax_calculation()
        self.capital_gains_tax = self.capital_gains_calculation()
        self.total_tax += self.income_tax + self.capital_gains_tax
        
        print("£{} in income tax, £{} in capital gains tax so the total is: £{}.".format(self.income_tax, self.capital_gains_tax, self.total_tax))

    def income_tax_calculation(self):
        total_income_tax = 0
        if self.income <= 10000:
            total_income_tax = 0
        elif self.income > 10000 and self.income <= 25000:
            total_income_tax += TaxPayer.lower_income_tax(self) 
        elif self.income > 25000 and self.income <= 50000:
            total_income_tax += TaxPayer.lower_income_tax(self) + TaxPayer.middle_income_tax(self)
        elif self.income > 50000 and self.income <= 150000:
            total_income_tax += TaxPayer.lower_income_tax(self) + TaxPayer.middle_income_tax(self) + TaxPayer.upper_income_tax(self)
        elif self.income >= 150000:
            total_income_tax += TaxPayer.lower_income_tax(self) + TaxPayer.middle_income_tax(self) + TaxPayer.upper_income_tax(self) + TaxPayer.highest_income_tax(self)
        return total_income_tax

    def lower_income_tax(self):
        lower_tax = min((self.income - 10000) * 0.25, 15000 * 0.25)
        return lower_tax
    
    def middle_income_tax(self):
        middle_tax = min((self.income - 25000) * 0.30, 25000*0.3)
        return middle_tax
    
    def upper_income_tax(self):
        upper_tax = min((self.income - 50000) * 0.35, 100000 * 0.35)
        return upper_tax

    def highest_income_tax(self):
        highest_tax = (self.income - 150000) * 0.45
        return highest_tax
    
    def capital_gains_calculation(self):
        if self.capital_gains < 12300:
            return 0 
        else:
            return (self.capital_gains - 12300) * self.capital_gains_rate 


name = input('Please enter your full name: ').upper()
age = input('Please enter your age numerically: ')
address  = input('Please enter your full address: ').upper()
income = input('Please enter the amount of income subject to income tax received in the previous tax year: ')
capital_gains = input('Please enter the amount of money recieved from capital gains in the previous tax year: ')
current_taxpayer = TaxPayer(name, age, address, income, capital_gains)

print(current_taxpayer.total_tax_calculation())

