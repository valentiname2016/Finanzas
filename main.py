from datetime import date, datetime
from portafolio import Portafolio


ACCIONES_EMPRESAS = {
    "AAPL":  "Apple Inc.",
    "AMZN":  "Amazon.com Inc.",
    "BAC":   "Bank of America",
    "GOOGL": "Alphabet (Google)",
    "JNJ":   "Johnson & Johnson",
    "JPM":   "JPMorgan Chase",
    "META":  "Meta Platforms",
    "MSFT":  "Microsoft Corp.",
    "NVDA":  "NVIDIA Corp.",
    "TSLA":  "Tesla Inc.",
    "V":     "Visa Inc.",   
    "WMT":   "Walmart Inc.",
    "XOM":   "Exxon Mobil Corp."
}

print("--- BIENVENIDO AL SIMULADOR DE INVERSIONES ---")
capital_usuario = float(input("¿Con cuánto dinero quieres empezar tu portafolio?: "))
mi_p = Portafolio(capital_usuario)
 
continuar = True
 
while continuar == True:
    print("\nBienvenido al portafolio de inversiones.")
    print("1. Ver acciones disponibles")
    print("2. Agregar Acciones")
    print("3. Comprar acciones")
    print("4. Invertir en CDT")
    print("5. Hacer Simulación")
    print("6. Ver Resumen Rentabilidad")
    print("7. Gráfica")
    print("8. Salir")
    
    opcion = input("\nSeleccione una opción: ")
 
    if opcion == "1":
        print("\nEMPRESAS DISPONIBLES")
        for ticker in ACCIONES_EMPRESAS:
            nombre = ACCIONES_EMPRESAS[ticker]
            print(f"[{ticker}] - {nombre}")
 
    elif opcion == "2":
        print("\nSELECCIONE UNA ACCIÓN PARA AGREGAR")
        for ticker in ACCIONES_EMPRESAS:
            nombre = ACCIONES_EMPRESAS[ticker]
            print(f"[{ticker}] - {nombre}")
        
        print("-" * 30)
        accion_elegida = input("Escriba el ticker que desea agregar: ").upper()
        
        if accion_elegida in ACCIONES_EMPRESAS:
            mi_p.agregar_accion(accion_elegida)
        else:
            print("Este ticker no existe.")

    elif opcion == "3":
        if len(mi_p.posiciones) == 0:
            print("\nNo has agregado acciones a tu portafolio.")
            print("Por favor agrega acciones primero")
        else:
            print("\nACCIONES DISPONIBLES")
            for ticker_agregado in mi_p.posiciones:
                nombre_empresa = ACCIONES_EMPRESAS[ticker_agregado]
                print(f"-> {ticker_agregado} ({nombre_empresa})")
            
            ticker_compra = input("\nEscriba el ticker que desea comprar: ").upper()
            
            if ticker_compra in mi_p.posiciones:
                cantidad = int(input(f"Cantidad de acciones de {ticker_compra}: "))
                fecha_str = input("Fecha de compra (AAAA-MM-DD): ")
                fecha_compra = date.fromisoformat(fecha_str)
                
                mi_p.comprar(ticker_compra, cantidad, fecha_compra)
            else:
                print("Esa acción no está agregada en el portafolio.")
 
    elif opcion == "4":
        tasa_anual = float(input("Tasa efectiva anual (ejemplo: 0.12): "))
        monto_cdt = float(input("Cuánto capital quieres invertir en el CDT: "))
        mi_p.agregar_cdt(tasa_anual, 365, monto_cdt)
        