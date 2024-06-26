GO_MAIN_SNIPPET = """ 
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


EXPRESS_SNIPPET = """
const express = require("express");
const app = express();
app.get("/", (req, res) => {
    res.status(200).json({message:"Hello world"})
})
app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});

"""

