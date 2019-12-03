#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import signal

if (sys.version_info.major != 3):

    print('\033[1;37mTienes que usar la versión \033[1;33m3\033[1;37m de \033[1;33mPython\033[0m \033[1;37mpara continuar...\033[0m')
    sys.exit(1)

from random import randint
from hashlib import sha256
from yaml import safe_dump as dump, safe_load as load
from base64 import b64encode, b64decode

from modules.Ciphers import shalom_v2 as shalom
from modules.UI import argprogrammer

file_ = None
file_content = None

def shalom_func(index, rest, random, hard):

    Shalom = shalom.Shalom(index=index, rest=rest)

    try:

        Shalom.hard(int(hard[1]), random=(False,), char=hard[0])

    except ValueError:

        print('El rango para agregar un byte a el mapa de caracteres no está tiene un tipo de dato correcto...')
        sys.exit(1)

    else:

        if (random != None):

            Shalom.random(random*-1 if ('-' in str(random)) else random)

    return(Shalom)

def secure_save(signum, frame):

    if (file_ != None) and (file_content != None):

        with open(file_, 'wb') as file_object:

            file_object.write(file_content)

    sys.exit(1)

signal.signal(signal.SIGTERM, secure_save)
signal.signal(signal.SIGINT, secure_save)

default_byte = ('\00', 500)
default_key_name = 'Shalom.key'
default_index = -6
default_rest = 6

group_optionals = 'Opcionales'
group_security = 'Seguridad'

parser = argprogrammer.Parser()

parser.add(['-h', '--help'], 'help', 'Mostrar ayuda y sale', group=group_optionals)

# Principales

parser.add(['-M', '--method'], 'method', 'Cifrar o Descifrar los datos del archivo. Usé "encrypt" para cifrar y "decrypt" para descifrar', uniqval=['encrypt', 'decrypt'], require=True)
parser.add(['-f', '--file'], 'file', 'Archivo objetivo', require=True)

# Relleno

parser.add(['-increment'], 'increment', 'Incrementar la clave con un byte; se necesita el rango, puede seguir la sintaxis: <byte>,<limite>. Pre-determinado: {}'.format(default_byte), default=default_byte, limit=2, type=tuple, group=group_security)
parser.add(['-random'], 'random', 'Usar el algoritmo de shuffle para ordernar al azar el mapa de caracteres', type=int, group=group_security)
parser.add(['-index'], 'index', 'El indíce para mover parte del mapa de caracteres según la especificación de Shalom. Pre-determinado: {}'.format(default_index), default=default_index, type=int, group=group_security)
parser.add(['-rest'], 'rest', 'El resto de diferencia según la especificación de Shalom. Pre-determinado: {}'.format(default_rest), type=int, default=default_rest, group=group_security)

args = parser.parse_args()

method = args.method
file_ = args.file
increment = args.increment
random = args.random
index = args.index
rest = args.rest

if not (os.path.isfile(file_)):

    print('El archivo "{}" no existe...'.format(file_))
    sys.exit(1)

try:

    wrap = shalom_func(index, rest, random, increment)

except Exception as Except:

    print('Ocurrio un error al instanciar la librería "Shalom"...')
    sys.exit(1)

try:

    with open(file_, 'rb') as file_object:

        file_content = file_object.read()

except Exception as Except:

    print('Ocurrio un error leyendo el fichero:', file_)
    sys.exit(1)

else:

    try:

        with open(file_, 'wb') as file_object:

            if (method.lower() == 'encrypt'):

                encode = dump(b64encode(file_content))
                jumps = [randint(-5000, 5000) for x in range(len(encode))]
                file_object.write(dump(wrap.encrypt(encode, jumps)).encode())

            else:

                file_object.write(b64decode(load(wrap.decrypt(load(file_content)))))

    except Exception as Except:

        print('Ocurrio un error escribiendo nuevos datos... restaurando...')

        try:

            with open(file_, 'wb') as file_object:

                file_object.write(file_content)

        except Exception as Except:

            print('Ocurrio un error al restaurar :/')
            sys.exit(1)

        else:

            print('Restaurado.')
