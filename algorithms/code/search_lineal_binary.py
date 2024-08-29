import time

Lista_inventario = [
    {"id": 1, "nombre": "Laptop", "precio": 1500},
    {"id": 2, "nombre": "Smartphone", "precio": 800},
    {"id": 3, "nombre": "Monitor", "precio": 300},
    {"id": 4, "nombre": "Teclado", "precio": 45},
    {"id": 5, "nombre": "Mouse", "precio": 25},
    {"id": 6, "nombre": "Impresora", "precio": 150},
    {"id": 7, "nombre": "Tablet", "precio": 250},
    {"id": 8, "nombre": "Cámara Digital", "precio": 500},
    {"id": 9, "nombre": "Auriculares", "precio": 75},
    {"id": 10, "nombre": "Reloj Inteligente", "precio": 200},
    {"id": 11, "nombre": "Disco Duro Externo", "precio": 120},
    {"id": 12, "nombre": "Router Wi-Fi", "precio": 60},
    {"id": 13, "nombre": "Memoria USB", "precio": 20},
    {"id": 14, "nombre": "Tarjeta SD", "precio": 15},
    {"id": 15, "nombre": "Altavoz Bluetooth", "precio": 85},
    {"id": 16, "nombre": "Proyector", "precio": 450},
    {"id": 17, "nombre": "Consola de Videojuegos", "precio": 400},
    {"id": 18, "nombre": "Cargador Portátil", "precio": 35},
    {"id": 19, "nombre": "Cable HDMI", "precio": 10},
    {"id": 20, "nombre": "Micrófono", "precio": 50},
    {"id": 21, "nombre": "Cámara de Seguridad", "precio": 250},
    {"id": 22, "nombre": "Smart TV", "precio": 600},
    {"id": 23, "nombre": "Lavadora", "precio": 700},
    {"id": 24, "nombre": "Refrigerador", "precio": 1200},
    {"id": 25, "nombre": "Horno Microondas", "precio": 180},
    {"id": 26, "nombre": "Aspiradora", "precio": 250},
    {"id": 27, "nombre": "Cafetera", "precio": 100},
    {"id": 28, "nombre": "Licuadora", "precio": 90},
    {"id": 29, "nombre": "Tostadora", "precio": 40},
    {"id": 30, "nombre": "Ventilador", "precio": 75},
    {"id": 31, "nombre": "Aire Acondicionado", "precio": 1500},
    {"id": 32, "nombre": "Calentador de Agua", "precio": 300},
    {"id": 33, "nombre": "Secadora de Ropa", "precio": 500},
    {"id": 34, "nombre": "Purificador de Aire", "precio": 200},
    {"id": 35, "nombre": "Deshumidificador", "precio": 250},
    {"id": 36, "nombre": "Plancha", "precio": 50},
    {"id": 37, "nombre": "Máquina de Coser", "precio": 300},
    {"id": 38, "nombre": "Cámara GoPro", "precio": 400},
    {"id": 39, "nombre": "Dron", "precio": 800},
    {"id": 40, "nombre": "Bicicleta Eléctrica", "precio": 1200},
    {"id": 41, "nombre": "Patinete Eléctrico", "precio": 600},
    {"id": 42, "nombre": "Scooter Eléctrico", "precio": 700},
    {"id": 43, "nombre": "Sistema de Sonido", "precio": 350},
    {"id": 44, "nombre": "Amplificador", "precio": 150},
    {"id": 45, "nombre": "Guitarra Eléctrica", "precio": 500},
    {"id": 46, "nombre": "Bajo Eléctrico", "precio": 550},
    {"id": 47, "nombre": "Piano Digital", "precio": 1000},
    {"id": 48, "nombre": "Batería Electrónica", "precio": 800},
    {"id": 49, "nombre": "Teclado MIDI", "precio": 200},
    {"id": 50, "nombre": "Mando a Distancia", "precio": 30},
    {"id": 51, "nombre": "Termostato Inteligente", "precio": 120},
    {"id": 52, "nombre": "Bombilla LED", "precio": 15},
    {"id": 53, "nombre": "Sensor de Movimiento", "precio": 40},
    {"id": 54, "nombre": "Enchufe Inteligente", "precio": 25},
    {"id": 55, "nombre": "Cerradura Inteligente", "precio": 200},
    {"id": 56, "nombre": "Videoportero", "precio": 180},
    {"id": 57, "nombre": "Timbre Inteligente", "precio": 120},
    {"id": 58, "nombre": "Cámara Web", "precio": 70},
    {"id": 59, "nombre": "Router Mesh", "precio": 150},
    {"id": 60, "nombre": "Switch de Red", "precio": 60},
    {"id": 61, "nombre": "Servidor NAS", "precio": 400},
    {"id": 62, "nombre": "Sistema de Alarma", "precio": 300},
    {"id": 63, "nombre": "Panel Solar", "precio": 1000},
    {"id": 64, "nombre": "Inversor Solar", "precio": 800},
    {"id": 65, "nombre": "Batería para Energía Solar", "precio": 1200},
    {"id": 66, "nombre": "Ventana Inteligente", "precio": 1500},
    {"id": 67, "nombre": "Cortina Inteligente", "precio": 300},
    {"id": 68, "nombre": "Irrigador Dental", "precio": 75},
    {"id": 69, "nombre": "Cepillo de Dientes Eléctrico", "precio": 60},
    {"id": 70, "nombre": "Secador de Pelo", "precio": 80},
    {"id": 71, "nombre": "Afeitadora Eléctrica", "precio": 100},
    {"id": 72, "nombre": "Báscula Digital", "precio": 50},
    {"id": 73, "nombre": "Cortadora de Cabello", "precio": 40},
    {"id": 74, "nombre": "Silla de Oficina", "precio": 150},
    {"id": 75, "nombre": "Escritorio", "precio": 200},
    {"id": 76, "nombre": "Lámpara de Escritorio", "precio": 50},
    {"id": 77, "nombre": "Silla Gamer", "precio": 250},
    {"id": 78, "nombre": "Auriculares con Micrófono", "precio": 100},
    {"id": 79, "nombre": "Monitor UltraWide", "precio": 500},
    {"id": 80, "nombre": "Ratón Gamer", "precio": 80},
    {"id": 81, "nombre": "Teclado Mecánico", "precio": 120},
    {"id": 82, "nombre": "Estación de Carga Inalámbrica", "precio": 40},
    {"id": 83, "nombre": "Cámara Instantánea", "precio": 130},
    {"id": 84, "nombre": "Tablet Gráfica", "precio": 200},
    {"id": 85, "nombre": "Altavoz Inteligente", "precio": 100},
    {"id": 86, "nombre": "Controlador de Juegos", "precio": 60},
    {"id": 87, "nombre": "Sintonizador de TV", "precio": 50},
    {"id": 88, "nombre": "Adaptador de Corriente", "precio": 20},
    {"id": 89, "nombre": "Estuche para Laptop", "precio": 35},
    {"id": 90, "nombre": "Cámara para Coche", "precio": 120},
    {"id": 91, "nombre": "Tira LED RGB", "precio": 30},
    {"id": 92, "nombre": "Mando Universal", "precio": 25},
    {"id": 93, "nombre": "Antena de TV", "precio": 15},
    {"id": 94, "nombre": "Escáner", "precio": 150},
    {"id": 95, "nombre": "Pizarra Digital", "precio": 350},
    {"id": 96, "nombre": "Placa de Inducción", "precio": 300},
    {"id": 97, "nombre": "Cámara Réflex", "precio": 900},
    {"id": 98, "nombre": "Microscopio", "precio": 200},
    {"id": 99, "nombre": "Cámara de Acción", "precio": 300},
    {"id": 100, "nombre": "Robot Aspirador", "precio": 400}
]

def search_product_lineal(list,criterio,value):
    print('Buscando producto con',criterio,'igual a',value)
    for product in list:
        print('Revisando producto:',product)
        if product[criterio] == value:
            print('Producto encontrado')
            return product
    return None


def search_product_binary(list,criterio,value):
    print('Buscando producto con',criterio,'igual a',value)
    list.sort(key=lambda x:x[criterio])
    print('Lista ordenada:',list)
    left=0
    right=len(list)-1
    while left<=right:
        middle=(left+right)//2
        print('Revisando producto:',list[middle])
        if list[middle][criterio]==value:
            print('Producto encontrado')
            return list[middle]
        elif list[middle][criterio]<value:
            left=middle+1
        else:
            right=middle-1

if __name__ == "__main__":
    inicio=time.time()

    result=search_product_lineal(Lista_inventario,"nombre",'Dron')
    if result != None:
        print('Producto encontrado:',result)
    else:
        print('Producto no encontrado')
    fin=time.time()
    print('Tiempo de ejecución en busqueda lineal:',fin-inicio)


    inicio_search_binari=time.time()
    result=search_product_binary(Lista_inventario,"nombre",'Dron')
    if result != None:
        print('Producto encontrado:',result)
    else:
        print('Producto no encontrado')
    fin_search_binari=time.time()
    print('Tiempo de ejecución en busqueda binaria:',fin_search_binari-inicio_search_binari)