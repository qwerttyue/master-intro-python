# Primeros pasos

## Instalar python en local

### Instalar en Windows
Instalar desde Microsoft Sttore o [Descargar la última versión en la pagina oficial](https://www.python.org/downloads/windows/)


### Instalar en Mac 
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
```
$ brew install python
```

### Instalar en Linux

```
$ sudo apt-get update
```
```
$ sudo apt-get install python3
```

### Para verificar la versión instalada en Mac y Linux
```
$ python --version
```

Para Mac y Linux, también se instalar mediante instalar python mediante [Pyenv](https://github.com/pyenv/pyenv), que es un gestor de versiones de python. Muchas veces es necesario tener varias versiones de python en el ordenador.

## El interprete de python

### Desde consola

- Para iniciar el interprete de python desde consola
```
$ python
```

- Para salir del interprete
    - ctrl+D 
    - o es escribir quit()

- Algunos comandos desde la consola:
```
print('hello world')

1+1

'hola'

"Hello" * 3

```

- Ejecutar un fichero .py:
```
$ python <fichero.py>
```

En windows:
```
$ python .\<fichero.py>
```

- Ejecutar un fichero .py como script:
```
$ ./<fichero.py>
```

Este comando puede dar error de permiso denegado, lo que significa que el fichero .py no tiene permisos necesarios para poder ser ejecutado. Para dar permiso de ejecución al fichero:
```
$ chmod +x <fichero.py>
```
