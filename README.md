# Blender-Python Scripts

## Configure Environment
1. Create a virtual environment & Download [fake-bpy-module](https://github.com/nutti/fake-bpy-module)
    
    ```bash
    # Note: use python 3.12 above for Blender 4.2
    python -m venv .venv
    .venv/Scripts/activate
    pip install fake-bpy-module-4.2
    ```

2. Install [Blender Development](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development) vscode Extension

3. Create `.vscode.settings.json`

    ```json
    {
        "python.analysis.extraPaths": [
            "${workspaceFolder}/.venv/Lib/site-packages/"
        ]
    }
    ```

4. Run Blender from vscode

    Choose the version of your blender after "**Blender: Start**".

    ![alt text](/images/image.png)


5. Write a script & Run the script

    Select "**Blender: Run Script**".

<br>

## Download API Document
https://docs.blender.org/api/current/blender_python_reference_4_3.zip

<br>

## Open API Docs with module
In *.venv/Lib/site-packages*, create the following ***document.py***.

```python
import webbrowser

html_file_path = <path/to/blender_python_reference_4_3/index.html>
webbrowser.open(html_file_path)
```

We can run this module by **`python -m document`** after the venv activated.

<br>

## Building Other Documents
### Blender Manual
1. Clone the repository

    ```bash
    git clone https://projects.blender.org/blender/blender-manual.git
    ```

2. Create a virtual environment & Download requirements
    
    ```bash
    cd blender-manual
    python -m .venv venv
    .venv/Scripts/activate
    pip install -r requirements.txt
    ```

3. Build the whole document

    ```bash
    mkdir build
    sphinx-build -M html manual build
    ```


<br>

### Developer Document
1. Clone the repository

    ```bash
    git clone https://projects.blender.org/blender/blender-developer-docs.git
    ```

2. Create a virtual environment & Download requirements
    
    ```bash
    cd blender-developer-docs
    python -m .venv venv
    .venv/Scripts/activate
    pip install -r requirements.txt
    ```

3. Build the whole document

    ```bash
    mkdocs build
    ```

<br>
