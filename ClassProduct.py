class Product:
    def __init__(self, ref=None, name=None, color=None, sku=None, quantityKil=None, place=None, desc=None):
        self.ref = ref
        self.name = name
        self.color = color
        self.sku = sku
        self.quantityKil = quantityKil
        self.place = place
        self.desc = desc
    
    # Metodos accesores
    def getRef(self):
        return self.ref
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getSku(self):
        return self.sku
    
    def getQuantityKil(self):
        return self.quantityKil
    
    def getPlace(self):
        return self.place
    
    def getDesc(self):
        return self.desc
    