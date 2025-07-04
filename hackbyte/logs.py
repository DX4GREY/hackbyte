from .ansi_colors import Fore as F, Style as S

def success(msg):
	print(f"{F.GREEN}[+] {msg}{S.RESET}")

def error(msg):
	print(f"{F.RED}[-] {msg}{S.RESET}")

def warn(msg):
	print(f"{F.YELLOW}[!] {msg}{S.RESET}")

def info(msg):
	print(f"{F.CYAN}[i] {msg}{S.RESET}")

def custom(tag, msg, color):
	"""
	tag: string like 'DEBUG', 'NOTE', etc.
	msg: the message string
	color: ansi_colors.Fore color (e.g. F.MAGENTA)
	"""
	print(f"{color}[{tag}] {msg}{S.RESET}")