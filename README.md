## ⚙️ Requerimientos

OpenCV

```
sudo apt install python3-opencv
```

CMake (Necesario para instalar dlib)

```
sudo apt install cmake
```

Python RTree

```
sudo apt install python3-rtree
```

Librerías de python

```
pip3 install dlib
pip3 install face_recognition
pip3 install pandas
pip3 install flask
```
## 🛠️ Armar el árbol

⚠️ Se van a indexar ~13k imágenes, este proceso tomará unos minutos.
```
python3 build.py
```


## ▶️ Ejecutar servidor

```
python3 server.py
```

El servidor se ejecutará en la dirección `0.0.0.0:5001`
