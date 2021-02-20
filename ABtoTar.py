import tarfile
import os.path
import logging
import argparse

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

    try:
        ab_data = open(path_to_ab, 'rb')
    except FileNotFoundError:
        logging.critical(f"Unable to open AB file at {path_to_ab}")
        return False

    ab_data.seek(8)




def build_tar_filepath(input_path, output_dir):
    input_filename = os.path.splitext(os.path.basename(input_path))[0]




if __name__ == '__main__':
    logging.info("-------------------")
    logging.info("AB to Tar")
    logging.info("By Greybeard")
    logging.info("-------------------")

    parser = argparse.ArgumentParser(description="Convert an Android Backup (AB) file to a tar")
    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True, action='store',
                        help='AB file')
    parser.add_argument('-o', '--output', dest='output_dir', type=str, default=None,
                        help='Output directory (default: same as AB file)')

    args = parser.parse_args()

    input_path = args.input_path
    output_dir = args.output_dir

    logging.info(f"Input file: {input_path}")