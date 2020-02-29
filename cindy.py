class usuario:
    def __init__(self,nombre,apellido,edad,pago,cuenta ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.metodo_de_pago = pago
        self.cuenta = cuenta
class prenda:
    def __init__(self, tipo, talla, genero, color, precio):
        self.tipo = tipo
        self.talla = talla
        self.genero = genero
        self.color = color
        self.precio = precio


listaprendas = list()
listausuario= list()
print("*************************************************")
print ("BIENVENIDO A LA WEB DE COMPRAS ONLINE DE CINDY")
print("*************************************************")
print("Tipo de Usuario")
print("1.Administrador")
print("2.Comprador")
tipo_de_usuario= int(input())
if tipo_de_usuario == 1:
    print("Registrar Prendas")
    print("Tipo de Prenda")
    print("A.Camisas")
    print("B.Pantalones")
    print("C.Zapatos")
    tipo_de_prenda= input()
    print("Ingrese la Talla")
    talla_prenda= input()
    print("Ingrese el Genero")
    genero_prenda= input()
    print("Ingrese el Color")
    color_prenda= input()
    print("Ingrese el precio")
    precio_prenda= input()
    prenda= prenda(tipo_de_prenda, talla_prenda, genero_prenda, color_prenda, precio_prenda)
    listaprendas.append(prenda)
    help(list)
    breakpoint()

if tipo_de_usuario == 2:
    print("BIENVENIDO AL MENU DE COMPRAS")
    print("******************************")
    print("1.CAMISAS-MUJER")
    print("******************************")
    print("2.PANTALONES-MUJER")
    print("******************************")
    print("3.ZAPATOS-MUJER")
    print("******************************")
    print("4.CAMISAS-HOMBRE")
    print("******************************")
    print("5.PANTALONES-HOMBRE")
    print("******************************")
    print("6.ZAPATOS-HOMBRE")
    print("******************************")
    seleccion= int(input())
    if seleccion == 1:
        print("Las Camisas de Mujer disponibles son")
        for prenda in listaprendas:
            print("El precio de las camisas es de 10 dolares")
    if seleccion == 2:
        print("Los Pantalones de Mujer disponibles son")
        for prenda in listaprendas:
            print("el precio de los pantalones es de 10 dolares")
    if seleccion == 3:
        print("Los Zapatos de Mujer disponibles son")
        for prenda in listaprendas:
            print("el precio de los zapatos es de 10 dolares")
    if seleccion == 4:
        print("Las Camisas de Hombre disponibles son")
        for prenda in listaprendas:
            print("el precio de las camisas es de 10 dolares")
    if seleccion == 5:
        print("Los Pantalones de Hombre disponibles son")
        for prenda in listaprendas:
            print("el precio de los pantalones es de 10 dolares")
    if seleccion == 6:
        print("Los Zapatos de Hombre disponibles son")
        for prenda in listaprendas:
            print("el precio de los zapatos es de 10 dolares")
    prendas_usuario= input()
    precio_total: str = input()
    precio_prenda= input()


print("el total de su compra es de ")
print("1.Desea concretar el pedido?")
print("2.Desea salir")
pago_salir= input()

if pago_salir == 1:
    print("Para concretar su pedido porfavor registrese")
    print("Ingrese su nombre")
    nombre= input()
    print("ingrese su apellido")
    apellido=input()
    print("ingrese su edad")
    edad= input()
    print("El total de su compra es de")
    precio_total
    print("seleccione el metodo de pago de su preferencia")
    print("1.visa")
    print("2.mastercard")
    print("3.pago en tienda")
    metodo_pago= input()
    if metodo_pago == 1:
            print("ingrese los datos de su Visa")
            print("ingrese el numero de tarjeta")
            numero_visa= input()
            print("Ingrese el nombre impreso en la tarjeta")
            nombre_visa= input()
            print("Verificando Datos")
            print("Seleccione la tienda de su preferencia para retirar su pedido")
            print("1.Porlamar")
            print("2.Pampatar")
            direccion= input()
            print("el total de su compra es de ")
            precio_total
            print("desea continuar con la compra?")
            print("1.SI")
            print("2.NO")
            continuar= input()
            if continuar == 1:
                print("SU PAGO A SIDO EXITOSO, PUEDE RETIRAR SU PEDIDO EN TRES (3) DIAS HABILES")
                print("GRACIAS POR SU COMPRA")
            if continuar == 2:
                print("Salir")
                print("GRACIAS POR VISITAR NUESTRA WEB")
    if metodo_pago == 2:
            print("Ingrese los datos de su Mastercard")
            print("Ingrese el numero de tarjeta")
            numero_master= input()
            print("Ingrese el nombre impreso en la  tarjeta")
            nombre_master= input()
            print("Verificando Datos")
            print("Seleccione la tienda de su preferencia para retirar su pedido")
            print("1.Porlamar")
            print("2.Pampatar")
            direccion= input()
            print("El total de su compra es de ")
            precio_total
            print("Desea continuar con la compra")
            print("1.SI")
            print("2.NO")
            continuar= input()
            if continuar == 1:
                print("SU PAGO HA SIDP EXITOSO, PUEDE RETIRAR SU PEDIDO EN TRES (3) DIAS HABILES")
                print("GRACIAS POR SU COMPRA")
            if continuar == 2:
                print("Salir")
                print("GRACIAS POR VISITAR NUESTRA WEB")

    if metodo_pago == 3:
            print("El total de su compra es de ")
            precio_total
            print("Seleccione la tienda de su preferencia")
            print("1.Porlamar")
            print("2.Pampatar")
            direccion= input()
            if direccion == 1:
                print("Puede Recoger su Pedido en tres (3) dias habiles en la tienda de Porlamar")
                print("GRACIAS POR SU COMPRA")
            if direccion == 2:
                print("Puede Recoger su Pedido en tres (3) dias habiles en la tienda de Pampatar")
                print("GRACIAS POR SU COMPRA")
usuario = usuario(nombre, apellido, edad, metodo_pago)
listausuario.append(usuario)
help(list)
if pago_salir == 2:
    print("Salir")
    print("GRACIAS POR VISITAR NUESTRA WEB")
