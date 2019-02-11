package main

import (
    "net/http"
    "encoding/json"
    "google.golang.org/appengine"
)

type Response struct {
    Status  string `json:"status"`
    Message string `json:"message"`
}

func main() {
    http.HandleFunc("/", handle)
    appengine.Main()
}

func handle(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(Response{Status: "ok", Message: "Hello world."})
}
