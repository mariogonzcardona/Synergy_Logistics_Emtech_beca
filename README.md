# Beca Santander EmTech
![santander](https://emtech.digital/santanderskills/landing/img/santander_1.png)

![EmTech](https://emtech.digital/santanderskills/landing/img/logo_emtech.png)

# Proyecto Synergy Logistics

Este proyecto está desarrollado en Python 3.9

Synergy Logistics es una empresa dedicada a la intermediación de servicios de importación y exportación de diferentes productos. Actualmente la empresa cuenta con una base de datos que refleja las rutas más importantes que opera desde el año 2015, con su respectivo origen y destino, año, producto, modo de transporte y valor total. Su propósito, es que a partir de estos datos se genere un análisis que sirva de la base para la estructuración de su estrategia operativa.

## Consigna

- Opción 1) Rutas de importación y exportación. Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más demandadas. Acorde a los flujos de importación y exportación, ¿cuáles son esas 10 rutas? ¿le conviene implementar esa estrategia? ¿porqué?

- Opción 2) Medio de transporte utilizado. ¿Cuáles son los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las importaciones y exportaciones? ¿Cuál es medio de transporte que podrían reducir?

- Opción 3) Valor total de importaciones y exportaciones. Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones e importaciones ¿en qué grupo de países debería enfocar sus esfuerzos?

## Tecnología

En este proyecto se enlistan las siguientes librerías para poder desarrollar los puntos solicitados.
| Plugin | Versión |
| ------ | ------ |
| asgiref | 3.5.0 |
| numpy | 1.22.1 |
| pandas | 1.4.0 |
| python-dateutil | 2.8.2 |
| pytz | 2021.3 |
| six | 1.16.0 |
| tabulate | 0.8.9 |
| tzdata | 2021.5 |

## Instalación

Para poder ejecutar el programa es necesario crear un ambiente virtual e instalar las dependencias en el archivo requirements.txt, ejecute main.py.

```sh
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
python main.py
```

## Ejecución en Google Colab
Se realizo el proyecto en Google Colab, para realizar y comprobar los resultados de acuerdo a los tres puntos solicitados, a continuación, se muestran algunas imágenes de la ejecución del programa.

#### Proyecto Relacionado
- [Google Colaboratory](https://colab.research.google.com/drive/1q4Q2mAKcIbEAHZw89yywpDY9MzjVaHRY?usp=sharing): Este proyecto está elaborado para comprobar la obtención de resultados a través de Pandas.

### Imágenes Librerías y DataFrame de Pandas
![google_imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_imports.png?raw=true)
![google_df](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_dataframe.png?raw=true)

### Imágenes Opción 1
![google_opt1_imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt1_imp.png?raw=true)
![google_opt1_exp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt1_exp.png?raw=true)

### Imágenes Opción 2
![google_opt2](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt2.png?raw=true)
![google_opt2_graf](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt2_grf.png?raw=true)

### Imágenes Opción 3
![google_opt3_imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt3_imp.png?raw=true)
![google_opt3_exp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/google_opt3_exp.png?raw=true)

## Ejecución en Consola
Este programa cuenta con un login y un register a través de un menú interactivo por consola

#### Primera sección Login, Register y Exit:
```sh
--------------------------------------------------
1. Login
2. Register
3. Exit
--------------------------------------------------
Select an option: 1
Enter your email: mario@hotmail.com
Enter your password: Test01.
Login successful
```

#### Para la sección del Menu:
```sh
--------------------------------------------------
1. Show Most demanded Import and Export Routes
2. Show Most demanded types of transport for Import and Export
3. Show Countries that generate 80% of the value of exports and imports
4. Exit
--------------------------------------------------
Select an option: 1
```

#### Para las opciones del Punto 1:
```sh
--------------------------------------------------
1. Show the 10 most demanded routes for Import
2. Show the 10 most demanded routes for Export
3. Exit
--------------------------------------------------
```

#### Punto 1: Rutas más demandadas para importaciones y exportaciones.
![Opt1_Imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt1_Imp.png?raw=true)
![Opt1_Exp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt1_Exp.png?raw=true)

#### Para las opciones del Punto 2:
```sh
--------------------------------------------------
1. Show the most demanded transports for Imports
2. Show the most demanded transports for Exports
3. Exit
--------------------------------------------------
```

#### Punto 2: Tipos de transporte más demandados para importaciones y exportaciones.
![Opt1_Imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt2_Imp.png?raw=true)
![Opt1_Exp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt2_Exp.png?raw=true)

#### Para las opciones del Punto 3:
```sh
--------------------------------------------------
1. Show the Countries that generate 80% of the value of imports
2.  Show the Countries that generate 80% of the value of exports
3. Exit
--------------------------------------------------
```

####  Punto 3: Países que generan el 80% del valor de las importaciones y exportaciones.
![Opt1_Imp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt3_Imp.png?raw=true)
![Opt1_Exp](https://github.com/mariogonzcardona/Synergy_Logistics_Emtech_beca/blob/main/Fotos/Opt3_Exp.png?raw=true)

## Licencia

Apache License

## Desarrollador
#### Mario Alejandro Gonzalez Cardona 

**Free Software, Hell Yeah!**