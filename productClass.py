class Product:
    
    def __init__(self, productName, productPrice):
        self.productName = productName
        self.productPrice = productPrice

 
    def getProductName(self):
        return self.productName

    def setProductName(self, productName):
        self.productName = productName

    def getProductPrice(self):
        return self.productPrice

    def setProductPrice(self, productPrice):
        self.productPrice = productPrice

  
    def getTotalPrice(self):
        return self.productPrice + self.calulateTax()

    def calulateTax(self):
        return 8.2 * self.productPrice / 100


