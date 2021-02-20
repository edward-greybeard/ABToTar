# ABToTar
Convert Android Backup files to tar.

Fun fact; Android backups are in fact tar files. To be able to open them, remove the first 24 bytes and replace with the following header:

`\x1f\x8b\x08\x00\x00\x00\x00\x00`

To save you some time, I've written a simple Python script which will do just that - as well as the normal sort of checks. If you really wanted you could probably achieve this in less than 10 lines, but you know; logging etc.

`Usage: ABtoTar.py [-h] -i INPUT_PATH [-o OUTPUT_DIR]

Convert an Android Backup (AB) file to a tar

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input INPUT_PATH
                        AB file
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        Output directory (default: same as AB file)`
