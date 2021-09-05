
class Shop():
    def __init__(self, name, owner):
        self.name = name
        self.customerList = []
        self.productsList = []
        self.receiptList = []
        self.owner = owner
        self.totalSales = 0

    
    def addCustomer(self, newClient):
        self.customerList.append(newClient)

    def addProduct(self, newProduct):
        self.productsList.append(newProduct)

    def addReceipt(self, newReceipt):
        self.receiptList.append(newReceipt)

    def showCustomer(self):
        for customer in self.customerList:
            print(customer)

    def showProduct(self):
        print("\t\tProductos disponibles")
        for product in self.productsList:
            print(product)
        
    def showReceipts(self):
        for receipt in self.receiptList:
            print(receipt)
            print("------------------------------")

    def findCustomer(self, customerid):
        for customer in self.customerList:
            if customerid == customer.id:
                return customer
        return False

    def findProduct(self, productName):
        for product in self.productsList:
            if productName == product.name:
                return product
        return False

    def salesC(self):
        for receipt in self.receiptList:
            self.totalSales += receipt.priceSale
        print(f"Acumulado en ventas: {self.totalSales}")

class Customer():
    def __init__ (self, name, id, telefon, address):
        self.name = name
        self.id = id
        self.telefon = telefon
        self.address = address

    def __str__(self):
        return "Nombre: "+self.name + " - " +  "ID: "+str(self.id) + " - " + "Teléfono: "+self.telefon + " - " + "Dirección: "+self.address

class Product():
    def __init__(self, name, price, description, availableUnits):
        self.name = name
        self.price = price
        self.description = description
        self.availableUnits = availableUnits

    def __str__(self):
        return "Nombre del producto: " + self.name + " - " + "Precio: " + str(self.price) + " - " + "Descripción: " + self.description + " - " + "Unidades: " + str(self.availableUnits)

class Receipt():
    def __init__(self, clientN, id, tele, add, prod, priceSale):
        self.clientN =  clientN
        self.id = id
        self.tele = tele
        self.add = add
        self.prod = prod
        self.priceSale = priceSale

    def __str__(self):
        return "Comprador: "+ self.clientN + "\nID: " + str(self.id) + "\nTelefono: " + self.tele + "\nDirección: " + self.add + "\nProducto Comprado: " + self.prod + "\nTotal de la compra: " + str(self.priceSale)

myShop = Shop("NicoStore", "Nicolas Jimenez")

open = True
while open:
    options = f"""
    Bienvenido a la tienda {myShop.name}
    -------------------------------------------------------------
    Ingrese "NC" para agregar un nuevo cliente al listado.
    Ingrese "NP" para agregar un producto al inventario.
    Ingrese "V" para realizar una nueva venta.
    Digite "AV" para conocer el acumulado de ventas.
    Ingrese "MC" para mostrar los clientes.
    Teclee "F" para ver las facturas acumuladas.
    Ingrese "P" para ver los productos en tienda
    X para salir.
    """
    selection = input(options)
    if selection.upper() == "NC":
        customerName = input("\nNombre del cliente: ")
        customerID = int(input("Numero de identificación del cliente: "))
        customerTelefon = input("Telefono de contacto: ")
        customerAddress = input("Dirección de residencia del cliente: ")
        newCustomer = Customer(customerName, customerID, customerTelefon, customerAddress)
        myShop.addCustomer(newCustomer)
        print("---------------------------------\n¡Cliente agregado exitosamente!\n---------------------------------")
    
    elif selection.upper() =="NP":
        productName = input("Ingrese el nombre del producto: ")
        productPrice = int(input("Ingrese el precio del producto: "))
        productDescription = input("Ingrese una descripción corta de su producto: ")
        availableUnits = int(input("Unidades del producto disponibles: "))
        newProduct = Product(productName, productPrice, productDescription, availableUnits)
        myShop.addProduct(newProduct)
        print("---------------------------------\nProducto agregado con éxito!\n---------------------------------")
    
    elif selection.upper() == "V":
        prodName = input("Ingrese el nombre del producto: ")
        productX = myShop.findProduct(prodName)
        if myShop.findProduct(prodName) != False:
            print(productX)
            customerI = int(input("Ingrese el ID del cliente: "))
            customerX = myShop.findCustomer(customerI)
            if myShop.findCustomer(customerI) != False:
                print(customerX)
                unitsProduct = int(input("Unidades a comprar: "))
                if productX.availableUnits >= unitsProduct:
                    newReceipt = Receipt(customerX.name, customerX.id, customerX.telefon, customerX.address, productX.name, unitsProduct * productX.price)
                    myShop.addReceipt(newReceipt)
                    productX.availableUnits -= unitsProduct
                    print("Venta exitosa!")
                    if productX.availableUnits <= 0:
                        myShop.productsList.remove(productX)
                else:
                    print("Unidades insuficientes")
            else:
                    print("Cliente no encotrado")
        else:
            print("Producto no encotrado")

    elif selection.upper() == "AV":
        myShop.salesC()

    elif selection.upper() == "MC":
        if len(myShop.customerList)>=1:
            myShop.showCustomer()
        else:
            print("Lista de clientes vacia")

    elif selection.upper() == "F":
        if len(myShop.receiptList)>=1:
            myShop.showReceipts()
        else:
            print("Lista de facturas vacia")

    elif selection.upper() == "P":
        if len(myShop.productsList)>=1:
            myShop.showProduct()
        else:
            print("No hay productos en tienda")

    elif selection.upper() == "X":
        open = False 


    

    
