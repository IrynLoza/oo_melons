"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        christmas_melon_price = base_price * 1.5
           
        if self.order_type == "international" and self.qty < 10:
            if self.species == "Christmas melons":
                total = (1 + self.tax) * self.qty * christmas_melon_price + self.additional_international_tax
                return total
            else:
                total = (1 + self.tax) * self.qty * base_price + self.additional_international_tax
                return total

        if self.order_type == "domestic":
            if self.species == "Christmas melons":
                total = (1 + self.tax) * self.qty * christmas_melon_price
                return total
            else:
                total = (1 + self.tax) * self.qty * base_price
                return total   


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True       

class GovernmentMelonOrder(AbstractMelonOrder):
    """Security inspection for melons"""

    def __init__(self, species, qty):
        """Initialize security inspection"""
        super().__init__(species, qty)
        self.order_type = "goverment"
        self.tax = 0.00
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order has passed the inspection."""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.""" 
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17
        self.additional_international_tax = 3
        self.shipped = False
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code
