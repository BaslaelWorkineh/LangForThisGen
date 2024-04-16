class MyLanguageInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            if line.startswith("vibe_check"):
                self.handle_vibe_check(line)
            elif line.startswith("big_Yikes"):
                self.handle_big_Yikes(line)
            elif line.startswith("shoutOut"):
                self.handle_shoutOut(line)
            elif line.startswith("fuckAround"):
                self.handle_fuckAround(line)
            elif line.startswith("find_out"):
                self.handle_find_out(line)

    def handle_vibe_check(self, line):
        print("Checking the vibe...")

    def handle_big_Yikes(self, line):
        print("Oh no, that's a big yikes!")

    def handle_shoutOut(self, line):
        parts = line.split('"')
        if len(parts) >= 2:
            print(parts[1])

    def handle_fuckAround(self, line):
        print("Stop messing around!")

    def handle_find_out(self, line):
        print("Trying to find out what went wrong...")


if __name__ == "__main__":
    interpreter = MyLanguageInterpreter()
    while True:
        code = input("Enter code: ")
        interpreter.interpret(code)
