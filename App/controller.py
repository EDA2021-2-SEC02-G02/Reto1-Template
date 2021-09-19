﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initcatalog():
    catalog=model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loaddata(catalog):
    loadartistas(catalog)
    loadobras(catalog)

def loadartistas(catalog):
    artistfile=cf.data_dir+"Artists-utf8-small.csv"
    input_file=csv.DictReader(open(artistfile,encoding="utf-8"))
    for artista in input_file:
        model.addartista(catalog,artista)

def loadobras(catalog):
    obrasfile=cf.data_dir+"Artworks-utf8-small.csv"
    input_file=csv.DictReader(open(obrasfile,encoding="utf-8"))
    for obra in input_file:
        model.addobra(catalog,obra)

# Funciones de ordenamiento
# REQ. 1: listar cronológicamente los artistas 
def addartistyear(catalog, año1, año2):
    return model.addartistyear(catalog, año1, año2)

def sortyear(catalog):
    return model.sortyear(catalog)

#REQ. 2: listar cronológicamente las adquisiciones 
def addartworkyear(catalog, fecha1, fecha2):
    return model.addartworkyear(catalog, fecha1, fecha2)

def sortdate(catalog):
    return model.sortdate(catalog)

def purchaseart(listaordenada2):
    return model.purshaseart(listaordenada2)

# Funciones de consulta sobre el catálogo
