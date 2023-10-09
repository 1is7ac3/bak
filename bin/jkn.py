#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  AnimeFlv
#
#  Copyright 2017 1is7ac3 <isaac.qa13@gmail.com>
#  Autor: Isaac Quiroz
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import os
from lxml import html
import requests
import datetime
# version en la pantalla
version = 'JKN 17.05.21 \n'


class Episode:
    def __init__(self, name, num, url):
        self.name = name
        self.num = num
        self.url = url


class Servidor:
    def __init__(self, url, namecap):
        self.url = url
        self.namecap = namecap


class Serie:
    def __init__(self, name, url, num, capi):
        self.name = name
        self.url = url
        self.num = num
        self.capi = capi

def Clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
    return


def GetUrl(Url):
    try:
        page = requests.get(Url)
        if page.status_code == 200:
            page = page.content.decode('utf-8')
        else:
            raise ValueError(f'Error: {page.status_code}')
    except ValueError as ve:
        print(ve)
        return False
    page = html.fromstring(page)
    return page


# Realiza la busqueda de enlaces
def SearchEngine():
    searchUrl = 'https://animeflv.net'
    page = GetUrl(searchUrl)
    print(page.text)
    serieLinks = page.xpath('//a[@class="fa-play"]/@href')
    serieNames = page.xpath('//a/strong[@class="Title"]/text()')
    serieCapi = page.xpath('//a/span[@class="Capi"]/text()')
    linkNum = len(serieLinks)
    if linkNum != len(serieNames):
        print('[!] Error Faltan Enlaces!')
        return False
    # Crear lista Serie
    serieList = []
    for n in range(0, linkNum):
        serie = Serie(serieNames[n], serieLinks[n], n, serieCapi[n])
        serieList.append(serie)
    return serieList


def GetEpisodesLink(url):
    url = 'https://animeflv.net'+url
    page = GetUrl(url)
    rawLinks = page.xpath('//script[contains(., "video")]/text()')
    epNames = page.xpath('//div[@class="CapiTop"]/h1/text()')
    rawLinks = rawLinks[0].split('":"')
    stream = []

    for a in rawLinks:
        if "https:" in a:
            b = a.split('"')
            for c in b:
                if 'stream' in c:
                    stream.append(c)
                if 'embed' in c:
                    stream.append(c)

    seList = []
    for a in stream:
        servidor = Servidor(a, epNames[0])
        seList.append(servidor)
    return seList


def Download(stream, savePath, titleCapitulo):
    i = 0
    while i < len(stream):
        n = str(i)
        dl = 'youtube-dl -o "' + savePath + '/' + titleCapitulo + ' ' \
            + n + '.mp4''"' + ' ' + stream[i].url
        er = os.system(dl)
        if er == 0:
            i = len(stream)
        else:
            i += 1

def streaming(stream):
    i = 0
    while i < len(stream):
        n = str(i)
        dl = 'mpv ' + stream[i].url
        er = os.system(dl)
        if er == 0:
            i = len(stream)
        else:
            i += 1


def DisplayResult(results):
    while True:
        today = datetime.datetime.today().strftime('%H:%M del %d-%m-%Y')
        Clear()
        print(version)
        print(f'Hora de actualizacion: {today}')
        print('Compruebe la serie que desea Descargar: ')
        for busque in results:
            n = str(busque.num)
            print('[', n, ']', busque.name)
        choice = input('\n Introduzca el numero de la serie a descargar: ')
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(results):
                print('[!] Error!. El numero no esta en la lista.')
                input()
            else:
                return choice
        else:
            print('[!]Error! Introduzca un numero.')
            input()


# Función Principal
def main():
    # Mostrar Series Encontradas
    busque = SearchEngine()
    choice = DisplayResult(busque)
    # Mostrar Servidores de Descarga
    title = busque[choice].name
    servi = GetEpisodesLink(busque[choice].url)
    titleCapitulo = servi[0].namecap
    op = input('[D]escargar o [V]er: ')
    if op == 'v':
        print(title)

    # Ubicacion de Descarga
    #path = os.environ['HOME']+'/.Anime'
    # Nombre Carpeta
    #if not os.path.exists(path):
    #    os.mkdir(path)
    #folderName = title
    #savePath = os.path.join(path, folderName)
    #if not os.path.exists(savePath):
    #    os.mkdir(savePath)
    #Download(servi, savePath, titleCapitulo)


if __name__ == "__main__":
    while True:
        main()
