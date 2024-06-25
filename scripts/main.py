from scripts.helpers import run_command, create_file, GO_MAIN_FILE
import os



def django_project(path ,name):
    command = "django-admin startproject "
    os.chdir(path)
    run_command(command + name)



def react_project(path, name):
    os.chdir(path)
    name = name.replace(" ", "_").lower()
    commands = [f'npx create-react-app {name}', 'npm start']
    run_command(commands[0])
    os.chdir(f"{path}/{name}")
    for i in range(1, len(commands)):
        run_command(commands[i])



dirs = ["handlers", "types", "store", "middleware", "routes"]

def go_project(path, name):
    os.chdir(path)

    middlewareFiles = ["jwt.go", "authentication.go"]


    command = f"go mod init {name}"
    run_command(command)
    create_file("main.go")
    with open("main.go", "w") as f:
        f.write(GO_MAIN_FILE)
        os.mkdir(f"{path}/pkg")
        os.chdir(f"{path}/pkg")
        for dir in dirs:
            os.mkdir(dir)
            if dir == "middleware":
                os.chdir(dir) 
                for file in middlewareFiles:
                    create_file(file)
                    with open(file, "w") as f:
                        f.write("package middleware")
                os.chdir(f"{path}/pkg")





