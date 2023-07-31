from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary 
        if self.vendor_model.is_correct_vendor(username, password):
            self.vendor_session.login(username) # here enter the username and apssword to login if its true then below message will populate
            print("User {} logged in successfully!".format(username))
            return True
        else:
            print("Invalid username or password.")
            return False

    def logout(self, username):
        # Add your code here to log out the current vendor
        self.vendor_session.logout(username)
        print("User {} Logged out Successfully".format(username)) # adding code to logged out user

