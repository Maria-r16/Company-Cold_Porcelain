class Product:
    def __init__(self, ref=None, sku=None, name=None, color=None, quantityKil=None, place=None, desc=None):
        self.ref = ref
        self.sku = sku
        self.name = name
        self.color = color
        self.quantityKil = quantityKil
        self.place = place
        self.desc = desc
    
    # Metodos accesores
    def getRef(self):
        return self.ref
    
    def getSku(self):
        return self.sku
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getQuantityKil(self):
        return self.quantityKil
    
    def getPlace(self):
        return self.place
    
    def getDesc(self):
        return self.desc
    