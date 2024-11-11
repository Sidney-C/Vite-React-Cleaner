import subprocess
import os
import argparse

boilerplate_jsx = """import React from 'react';
import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<h1>Hello World!</h1>);"""

boilerplate_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""

boilerplate_bootstrap = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Vite + React</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", dest="name", required=True, help="Enter -n or --name followed by the name you want to give your project. Names cannot contain whitespace.")
    parser.add_argument("-f", "--framework", dest="framework", help="Enter -f or --framework followed by bootstrap to automatically include the Bootstrap 5 framework in your boilerplate code.") 
    args = parser.parse_args()
    if args.framework:
        return [args.name, args.framework]
    else:
        return [args.name, "none"]

def create_project(name):
    subprocess.run(["npm", "create", "vite@latest", name, "--", "--template", "react"], shell=True)
    
def delete_items(name, folder):
    file_path = os.path.join(name, folder)
    for item in os.listdir(file_path):
        item_path = os.path.join(file_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
       
def scaffold_project(name, path, boilerplate):
    file_path = os.path.join(name, path)
    with open(file_path, "w") as f:
        f.write(boilerplate)

try:
    args = get_args()
    name = args[0]
    framework = args[1]
    framework = framework.lower()
    create_project(name)
    delete_items(name, "src")
    delete_items(name, "src/assets")
    delete_items(name, "public")
    scaffold_project(name, "src/main.jsx", boilerplate_jsx)
    if framework == "bootstrap":
        scaffold_project(name, "index.html", boilerplate_bootstrap)
    else:
        scaffold_project(name, "index.html", boilerplate_html)
except:
    print("ERROR: No valid name given. When running this script from the command line, please enter -n or --name followed by the name you want to give your project. Names cannot contain whitespace.")