from helpers import run_command, create_file, GO_MAIN_FILE
import os



def django_project(path ,name):
    command = "django-admin startproject "
    os.chdir(path)
    run_command(command + name)



def react_project(path, name):
    os.mkdir(path)
    os.chdir(path)
    commands = [f'npx create-react-app {name}', 'npm start']
    for command in commands:
        run_command(command)


path = input("Where do you want you project to live: ") 
projectName = input("How do you wanna call your project: ")
dirs = ["handlers", "types", "store", "middleware", "routes"]


def go_project(path, name):
    os.mkdir(path)
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





