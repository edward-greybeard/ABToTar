# ABtoTar.py
# Change the Android Backup file (*.ab) into a tar for fun and profit.
# Basically; remove the first 24 bytes and replace them with a tar header.
# Ed Greybeard 2021

from tarfile import is_tarfile
import os.path
import logging
import argparse
from sys import exit

AB_HEADER = b"ANDROID BACKUP"
TAR_HEADER = b"\x1f\x8b\x08\x00\x00\x00\x00\x00"
IGNORE_OFFSET = 24


logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', level='DEBUG')

def extract_tar_from_ab(path_to_ab, output_dir=None):
    """
    An AB file is a tar with 8 bytes added to the start.
    This will extract the tar to the same directory as the AB file unless output_dir is specified.
    :param path_to_ab:
    :param output_dir:
    :return:
    """
    if output_dir is None:
        output_dir = os.path.dirname(path_to_ab)

    # Check we can open the file
    try:
        ab_data = open(path_to_ab, 'rb')
    except:
        logging.critical(f"Unable to open AB file at {path_to_ab}")
        return False

    # Check the AB file header is intact
    ab_bytes_to_remove = ab_data.read(24)

    if ab_bytes_to_remove[:14] == AB_HEADER:
        logging.info("AB Header checked and intact")
    else:
        logging.error("AB Header not found; is it definitely the right file?")
        return False

    # Open the target tar file
    output_path = build_tar_filepath(input_path, output_dir)

    try:
        output_file = open(output_path, 'wb')
    except:
        logging.error("Unable to open file at {output_path}")
        return False

    logging.info("Writing tar header..")
    output_file.write(TAR_HEADER)

    logging.info("Writing rest of AB file..")
    output_file.write(ab_data.read())

    logging.info("..done.")
    logging.info("Closing files..")

    output_file.close()
    ab_data.close()

    # quick verify
    try:
        test_val = is_tarfile(output_path)
        logging.info("Output verified OK")
        return True
    except:
        logging.error("Verification failed; maybe it's encrypted?")
        return False


def build_tar_filepath(input_path, output_dir):
    input_filename = os.path.splitext(os.path.basename(input_path))[0]
    output_filename = f"{input_filename}.tar.gz"
    logging.info(f"Output filename: {output_filename}")
    output_filepath = os.path.join(output_dir, output_filename)
    return output_filepath


if __name__ == '__main__':
    logging.info("-------------------")
    logging.info("AB to Tar")
    logging.info("By Greybeard")
    logging.info("-------------------")
    logging.info("Global variables:")
    logging.info(f"AB_HEADER:        {AB_HEADER}")
    logging.info(f"TAR_HEADER:       {TAR_HEADER}")
    logging.info(f"BYTES TO IGNORE:  {IGNORE_OFFSET}")

    parser = argparse.ArgumentParser(description="Convert an Android Backup (AB) file to a tar")
    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True, action='store',
                        help='AB file')
    parser.add_argument('-o', '--output', dest='output_dir', type=str, default=None,
                        help='Output directory (default: same as AB file)')

    args = parser.parse_args()

    input_path = args.input_path
    output_dir = args.output_dir

    if os.path.exists(input_path) is not True:
        logging.critical(f"{input_path} not found. Exiting..")
        exit(1)

    logging.info(f"Input file: {input_path}")

    if extract_tar_from_ab(input_path, output_dir) is True:
        logging.info("Processing complete.")
    else:
        logging.info("Error with processing. Exiting..")


