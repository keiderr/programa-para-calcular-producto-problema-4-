# -------------------------------------------------------
# Nombre del estudiante: [Tu Nombre Completo]
# Grupo: [Tu Grupo]
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia
# Fase 2 – Problema 4: Valor final según categoría
# -------------------------------------------------------
 
# Constante IVA definida al inicio del programa
IVA = 0.19
 
# Solicitar el precio base del producto
precio_base = float(input('Ingrese el precio base del producto: '))
 
# Validar que el precio sea mayor a cero
if precio_base <= 0:
    print('Error: el precio base debe ser mayor a cero.')
else:
    # Solicitar el código de categoría
    print('Categorías disponibles:')
    print('  1 – Producto básico (sin IVA)')
    print('  2 – Producto estándar (IVA 19%)')
    print('  3 – Producto de lujo (IVA 19% + recargo 5%)')
    categoria = int(input('Ingrese el código de categoría (1, 2 o 3): '))
 
    # Calcular valor final según categoría
    if categoria == 1:
        valor_final = precio_base
        nombre_cat = 'Producto básico'
        detalle = 'Sin IVA'
    elif categoria == 2:
        valor_final = precio_base + (precio_base * IVA)
        nombre_cat = 'Producto estándar'
        detalle = f'IVA del {IVA*100:.0f}% aplicado'
    elif categoria == 3:
        valor_final = precio_base + (precio_base * IVA) + (precio_base * 0.05)
        nombre_cat = 'Producto de lujo'
        detalle = f'IVA del {IVA*100:.0f}% + recargo del 5%'
    else:
        print('Error: código de categoría inválido. Use 1, 2 o 3.')
        valor_final = None
 
    # Mostrar resultado
    if valor_final is not None:
        print(f'\nCategoría: {nombre_cat}')
        print(f'Precio base:  ${precio_base:,.2f}')
        print(f'Ajuste:   	{detalle}')
        print(f'Valor final:  ${valor_final:,.2f}')