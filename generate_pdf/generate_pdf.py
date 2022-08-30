#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dnf install librsvg2-tools
# apt install librsvg2-bin

import hashlib
import os
import logging
import re
from pathlib import Path, PurePath  # nueva forma de trabajar con rutas
from typing import Dict, Text, NoReturn, List

import pypandoc

from implement_sqlite import select_all_hashes, insert_file, update_file
from file import File
from procamora_utils.logger import get_logging

logger: logging = get_logging(False, 'generate_pdf')

WORK: Path = Path(__file__).resolve().parent.parent
WORK_CONTENT: Path = Path(WORK, 'content')
logger.info(WORK)


def get_hashsum(file: Path) -> Text:
    # https://nitratine.net/blog/post/how-to-hash-files-in-python/
    BLOCK_SIZE: int = 65536  # The size of each read from the file (4096 *16) 16 paginas de usuario

    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(str(file), 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    # print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
    return file_hash.hexdigest()


def add_absolute_path(file: Path) -> Text:
    regex: Text = r'(/images/.*)'
    absolute_path: Text = str(WORK_CONTENT)  # Ruta raiz donde encontrar images/
    return re.sub(regex, rf'{absolute_path}\1', file.read_text())


def generate_pdf(file: Path) -> bool:
    dirpath_pdf: Path = Path(WORK_CONTENT, 'pdf')
    file_pdf: Path = Path(dirpath_pdf, f'{str(file.name)[0:-3]}.pdf')  # elimino .md [0:-3]

    if not dirpath_pdf.exists():
        logger.debug(f'Create directory: {dirpath_pdf}')
        dirpath_pdf.mkdir()

    logger.info(f'Generate PDF: {file_pdf}')
    try:
        file_path: Text = add_absolute_path(file)
        #print(file_path)
        output: Text = pypandoc.convert_text(source=file_path, to='pdf', format='md', outputfile=str(file_pdf),
                                             extra_args=['-V', 'geometry:margin=1.5cm', '--pdf-engine=xelatex'])
        assert output == ""
        return True
    except RuntimeError as e:
        logger.error(f'{file} -> {e}')
        # Si falla el modo bueno se hace con otro que continua pese a no tener las imagenes
        return False


def main() -> NoReturn:
    # Obtengo recurisvamente todos los ficheros .md
    files: List[Path] = list(WORK_CONTENT.rglob("*.md"))

    all_hashes: Dict[str, File] = select_all_hashes()

    for f in files:
        file: Text = str(f)
        file_hash: Text = get_hashsum(f)
        # Si el fichero no existe se inserta en la BD
        if not file in all_hashes.keys():
            insert_file(file, file_hash)
            generate_pdf(f)
        # Si el fichero existe comprobamos que tiene el mismo hash
        elif all_hashes[file].shasum != file_hash:
            logger.info(f'{all_hashes[file]} != {file_hash}')
            update_file(file, file_hash)
            generate_pdf(f)

    logger.info('Finished')


if __name__ == '__main__':
    main()
