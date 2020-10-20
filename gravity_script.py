import argparse
import logging
import sys


parser = argparse.ArgumentParser(description="Crack Gravity Falls secrets!")
parser.add_argument('--str', dest="text", type=str, help='string to translate', required=True)
# parser.add_argument('--crypt', dest="cypher", help='cypher code type')							# TODO: add options
# parser.add_argument('--i', dest="number", type=int, help='number of position a letter moves')
parser.add_argument('-debug', dest="debug", action='store_true', help='print debug')
parser.add_argument('--se', dest="season", type=int, help='season of the episode', required=True)
parser.add_argument('--ep', dest="episode", type=int, help='episode', required=True)
args = parser.parse_args()


#logging.basicConfig(level= (lambda x: int(logging.DEBUG) if args.debug else int(logging.INFO))) # TODO
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

ABECEDARY = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
	"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
SPECIAL_CHAR = [" ", ",", ".", ":", "'", "\"", "?", "!"]
MAGIC_NUMBER = 3

class Cypher:
	def __init__(self, name, season, episodes):
		self.name = name
		self.season = season
		self.episodes = episodes


CYPHERS = []
CYPHERS.append(Cypher("caesar", 1, list(range(1,8))))
CYPHERS.append(Cypher("atbash", 1, list(range(8,15))))


def caesar_cypher(position):
	return ABECEDARY[position-MAGIC_NUMBER]

def atbash_cypher(position):
	return list(reversed(ABECEDARY))[position]


def translate(char, cypher=None, number=MAGIC_NUMBER) -> str:
	if char in SPECIAL_CHAR:
		return char

	position = ABECEDARY.index(char)
	logger.debug(f"position: {position}")

	if cypher == "caesar":
		return caesar_cypher(position)
	
	elif cypher == "atbash":
		return atbash_cypher(position)


def get_cypher(season, episode): 

	for cypher in CYPHERS:
		logger.debug(f"cypher: {cypher.id}")
		if cypher.season == season:
			if episode in cypher.episodes:
				return cypher.name
	return "error"


def main(argv):

	text = args.text.upper()
	season = args.season
	episode = args.episode

	logger.debug(f"text: {text}")
	logger.debug(f"season: {season}")
	logger.debug(f"episode: {episode}")
	logger.debug(f"MAGIC_NUMBER: {MAGIC_NUMBER}")

	cypher = get_cypher(season, episode)

	result = ""

	for char in text:
		result += translate(char, cypher)

	logger.info(f"result: {result}")

if __name__ == "__main__":
    main(sys.argv[1:])
