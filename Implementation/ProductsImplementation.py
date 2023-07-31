from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        # check if the vendor is logged in, then add the product and return True else Return False
         if not self.vendor_session.check_login(self._username):
            print("Please do signup or login first.")
            return False        # here  checking if Venfor is registered or not if registered then ask for login
        
         self.product_model.add_product(product_name, product_type, available_quantity, unit_price)
         print(product_name + " added successfully!")  # here adding the product details
         return True
                                                    
    def search_product_by_name(self, product_name):
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        if not self.vendor_session.check_login(self._username): # here checking vendor is registered or not
            print("Please  do signup or login first")
            return False  
        
        retrieved_product = self.product_model.search_product(product_name)   
        return retrieved_product  
        #if (retrieved_product):
        #    print(retrieved_product)
        #else:
        #    print("asked product is not avaialble")

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products 
        if not self.vendor_session.check_login(self._username):
            print("Please signup or login first.")
            return False
        
        Products = self.product_model.all_products()
        return Products

