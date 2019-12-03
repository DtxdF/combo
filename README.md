# Combo

> Combo es una pequeña herramienta para cifrar/descifrar archivos usando el algoritmo de [Shalom](https://github.com/DtxdF/Shalom)

# Ejemplos

*Para ver la ayuda*

```bash
./combo.py -h


  Opcionales:
  ----------

    -h, --help              Mostrar ayuda y sale

  Parámetros principales:
  ----------------------

    -M, --method            Cifrar o Descifrar los datos del archivo. Usé "encrypt" para cifrar y "decrypt" para descifrar
    -f, --file              Archivo objetivo

  Seguridad:
  ---------

    -increment              Incrementar la clave con un byte; se necesita el rango, puede seguir la sintaxis: <byte>,<limite>. Pre-determinado: ('\x00', 500)
    -random                 Usar el algoritmo de shuffle para ordernar al azar el mapa de caracteres
    -index                  El indíce para mover parte del mapa de caracteres según la especificación de Shalom. Pre-determinado: -6
    -rest                   El resto de diferencia según la especificación de Shalom. Pre-determinado: 6
```

*Para cifrar un archivo*

Creó el archivo a cifrar:

```bash
cat > test.txt
Hello Friend.
```
Lo descifro:

```bash
./combo.py -f test.txt -M encrypt
```

Vemos el contenido del archivo:

```bash
cat test.txt

- [-1466, 1511]
- [-2481, 2526]
- [1982, -1872]
- [-1619, 1736]
- [-3082, 3204]
- [-3941, 4050]
- [2195, -2069]
- [-3932, 4065]
- [2305, -2261]
- [4237, -4101]
- [-1892, 1914]
- [3172, -3128]
- [-3301, 3345]
- [2990, -2893]
- [-3043, 3103]
- [-4107, 4219]
- [-4281, 4380]
- [2056, -1945]
- [-4029, 4091]
- [-3224, 3310]
- [-1834, 1918]
- [2978, -2887]
- [-1687, 1770]
- [-4381, 4493]
- [613, -518]
- [1556, -1446]
- [2936, -2817]
- [-4491, 4615]
- [294, -163]
- [-1449, 1548]
- [767, -647]
- [-761, 872]
- [-3199, 3260]
- [3295, -3186]
- [-1008, 1068]
- [4597, -4465]
- [3957, -3835]
- [4819, -4709]
- [845, -711]
- [-2478, 2538]
- [-2874, 2947]
- [-2405, 2427]
```

*Tu archivo puede tener un contenido diferente*

Ahora para descifrarlo:

```bash
./combo.py -f test.txt -M decrypt
cat test.txt
Hello Friend.
```

*Puede tardar un poco sí es un archivo de gran tamaño*

~ DtxdF (**DtxdF@protonmail.com**)
