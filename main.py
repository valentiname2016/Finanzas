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