from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgBnxxyyIdTYhae__vonrHEvhrFUZmyB9T-Q0JGW9Ro3zJTvao60hgPoSua6ba6NFm9KpwGkyXvU5A2tBhDe47aA4bcKWGIy3oJVB1eDq-e3y-QkdhIUAmOkjk1T8UU1yiplIyp6yK0HMZI1war8gVO8v5Ez2_bF3OeVdS1TW6G4vO8gxzZyCID8YGbXPQIawBCTZngMxqHypny_KNRrQuAL_1YJaPGd-LwGHolKPLAMo-yS90N68CDVRLvyvdaDB_KjDVjThrtXF6qhrhCjWCL7UA-hLC7IdHG9NWrj4-1loxc8VfnqRlnF60LlKzafOLIU1J15YpvGOCsKiF0NbbIaAAAAAU9z4jMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5785203412:AAHYMLUM26NPXKJWJ8hC-wx9FIw8loKhIcM")
BOT_NAME = getenv("BOT_NAME", "N1Asistant") 
API_ID = int(getenv("API_ID", "12878302")
API_HASH = getenv("API_HASH", "1ce756e879790d465304f48c36294883")
BOT_USERNAME = getenv("BOT_USERNAME", "N1MusicRobot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
