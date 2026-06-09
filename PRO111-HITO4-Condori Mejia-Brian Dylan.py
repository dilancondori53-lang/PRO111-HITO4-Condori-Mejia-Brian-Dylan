# Contadores generales
total_estudiantes = 0
aprobados = 0
reprobados_nota = 0
reprobados_asistencia = 0

continuar = "S"

while continuar == "S" or continuar == "s":

    print("\nREGISTRO DE ESTUDIANTE")

    nombre = input("Nombre completo: ")
    clases_programadas = int(input("Cantidad total de clases programadas: "))
    clases_asistidas = int(input("Cantidad de clases asistidas: "))
    nota = float(input("Calificación final (0 a 100): "))

    porcentaje_asistencia = (clases_asistidas * 100) / clases_programadas

    if porcentaje_asistencia >= 80:

        if nota >= 51:
            condicion = "APROBADO"
            aprobados += 1
        else:
            condicion = "REPROBADO POR NOTA"
            reprobados_nota += 1

    else:
        condicion = "REPROBADO POR ASISTENCIA"
        reprobados_asistencia += 1

    total_estudiantes += 1

    print("\nRESULTADO DEL ESTUDIANTE")
    print("Nombre:", nombre)
    print("Asistencia:", round(porcentaje_asistencia, 2), "%")
    print("Nota final:", nota)
    print("Condición:", condicion)

    continuar = input(
        "\n¿Desea registrar otro estudiante? (S/N): "
    )

if total_estudiantes > 0:
    porcentaje_aprobados = (aprobados * 100) / total_estudiantes
else:
    porcentaje_aprobados = 0

print("\n========== RESUMEN FINAL ==========")
print("Total de estudiantes:", total_estudiantes)
print("Aprobados:", aprobados)
print("Reprobados por nota:", reprobados_nota)
print("Reprobados por asistencia:", reprobados_asistencia)
print("Porcentaje de aprobados:", round(porcentaje_aprobados, 2), "%")