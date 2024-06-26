from scripts.helpers import run_command, create_file
from scripts.snippets import GO_MAIN_SNIPPET, EXPRESS_SNIPPET
import os
DIRS = ["handlers", "types", "store", "middleware", "routes"]
COMMON_FILES = [".gitignore", "README.md"]



class Project:
    def __init__(self, path, name) -> None:
        self.path = path 
        self.name = name
        for file in COMMON_FILES:
            with open(file, "w") as f:
                f.write("")
    def django(self):
        command = "django-admin startproject "
        os.chdir(self.path)
        run_command(command + self.name)


    def react(self):
        os.chdir(self.path)
        name = self.name.replace(" ", "_").lower()
        commands = [f'npx create-react-app {name} -y', 'npm start']
        run_command(commands[0])
        os.chdir(f"{self.path}/{name}")
        for command in commands:
            run_command(command)


    def express(self):
        init_command = "npm init -y"
        install_express = "npm install express"
        os.chdir(self.path)
        run_command(init_command)
        run_command(install_express)
        with open("app.js", "w") as f:
            f.write(EXPRESS_SNIPPET)
        for dir in DIRS:
            os.mkdir(dir)

    def go(self):
        os.chdir(self.path)

        middlewareFiles = ["jwt.go", "authentication.go"]


        command = f"go mod init {self.name}"
        run_command(command)
        create_file("main.go")
        with open("main.go", "w") as f:
            f.write(GO_MAIN_SNIPPET)
            os.mkdir(f"{self.path}/pkg")
            os.chdir(f"{self.path}/pkg")
            for dir in DIRS:
                os.mkdir(dir)
                if dir == "middleware":
                    os.chdir(dir) 
                    for file in middlewareFiles:
                        create_file(file)
                        with open(file, "w") as f:
                            f.write("package middleware")
                    os.chdir(f"{self.path}/pkg")

    



    






