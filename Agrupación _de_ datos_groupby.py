# Contar cuántas veces aparece cada nombre de entidad
agrupacion = df.groupby('NOM_ENTIDAD')['ID_ENTIDAD'].count()
print(agrupacion)


# Calcular la media del ID_ENTIDAD para cada NOM_ENTIDAD
agrupacion = df.groupby('NOM_ENTIDAD')['ID_ENTIDAD'].mean()
print(agrupacion)


# Sumar los valores de ID_ENTIDAD para cada NOM_ENTIDAD
agrupacion = df.groupby('NOM_ENTIDAD')['ID_ENTIDAD'].sum()
print(agrupacion)

