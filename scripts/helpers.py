import subprocess
def create_file(file_name:str):
    with open(file_name, 'w') as f:
        f.write("")
        


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout)
        else:
            print("Error executing command:")
            print(result.stderr)
    except Exception as e:
        print(e)



GO_MAIN_FILE = """ 
package main 

import ( 
    "fmt" 
    "log" 
    "net/http"
) 

func main(){
    mux := http.NewServeMux()
    mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello world")
    })
    log.Fatal(http.ListenAndServe(":8080", mux)) 

}


""" 
