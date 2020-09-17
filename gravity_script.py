import argparse
import logging
import sys


parser = argparse.ArgumentParser(description="Crack Gravity Falls secrets!")
parser.add_argument('--str', dest="text", type=str, help='string to translate', required=True)
parser.add_argument('--crypt', dest="cypher", help='cypher code type')							# TODO: add options
parser.add_argument('--i', dest="number", type=int, help='number of position a letter moves')
parser.add_argument('-debug', dest="debug", action='store_true', help='print debug')
args = parser.parse_args()


#logging.basicConfig(level= (lambda x: int(logging.DEBUG) if args.debug else int(logging.INFO))) # TODO
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

ABECEDARY = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
	"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
SPECIAL_CHAR = [" ", ",", ".", ":", "'", "\"", "?", "!"]
MAGIC_NUMBER = 3


def caesar_cypher(position):
	return ABECEDARY[position-MAGIC_NUMBER]

def atbash_cypher(position):
	return list(reversed(ABECEDARY))[position]


def translate(char, cypher=None, number=MAGIC_NUMBER) -> str:
	if char in SPECIAL_CHAR:
		return char

	position = ABECEDARY.index(char)
	logger.debug(f"position: {position}")

	
	if cypher:
		return atbash_cypher(position)

	# default cypher
	return caesar_cypher(position)


def main(argv):

	text = args.text.upper()
	cypher = args.cypher
	number = args.number if args.number else MAGIC_NUMBER

	logger.debug(f"text: {text}")
	logger.debug(f"cypher: {cypher}")
	logger.debug(f"MAGIC_NUMBER: {MAGIC_NUMBER}")

	result = ""

	for char in text:
		result += translate(char, cypher, number)

	logger.info(f"result: {result}")

if __name__ == "__main__":
    main(sys.argv[1:])
