from daemon.terminal.colors import Color

Color.red("RED")
Color.green("GREEN")
Color.yellow("YELLOW")
Color.blue("BLUE")
Color.magenta("MAGENTA")
Color.cyan("CYAN")
Color.white("WHITE")

Color.light_red("LIGHT RED")
Color.light_green("LIGHT GREEN")
Color.light_yellow("LIGHT YELLOW")
Color.light_blue("LIGHT BLUE")
Color.light_magenta("LIGHT MAGENTA")
Color.light_cyan("LIGHT CYAN")
Color.light_white("LIGHT WHITE")


Color.red(
    "ERRORE!",
    Color.BOLD,
    Color.UNDERLINE
)


text = Color.red(
    "Questo non viene stampato",
    Color.BOLD,
    printable=False
)

print(f"STAMPA SUCCESSIVA: {text}")