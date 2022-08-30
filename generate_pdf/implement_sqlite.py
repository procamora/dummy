#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from pathlib import Path  # nueva forma de trabajar con rutas
from typing import List, Text, NoReturn, Tuple, Dict

from procamora_utils.interface_sqlite import conection_sqlite
from procamora_utils.logger import get_logging

from file import File

logger: logging = get_logging(False, 'sqlite')


# Ruta absoluta de la BD
DB: Path = Path(Path(__file__).resolve().parent, "wiki.db")
DB_STRUCTURE: Path = Path(Path(__file__).resolve().parent, "wiki.db.sql")


def select_all_hashes() -> Dict[Text, File]:
    query: Text = "SELECT * FROM hashes"
    response_query: List[Dict[Text, Any]] = conection_sqlite(DB, query, is_dict=True)
    response: Dict[Text, File] = dict()
    for i in response_query:
        file: File = File(i['id'], i['file'], i['hash'])
        response[file.file] = file
    return response


def insert_file(file: Text, hash: Text) -> NoReturn:
    query: Text = f"INSERT INTO hashes(file, hash) VALUES ('{file}','{hash}');"
    logger.debug(query)
    conection_sqlite(DB, query)


def update_file(file: Text, hash: Text) -> NoReturn:
    query: Text = f"UPDATE hashes SET hash='{hash}' WHERE file LIKE '{file}';"
    logger.debug(query)
    conection_sqlite(DB, query)
