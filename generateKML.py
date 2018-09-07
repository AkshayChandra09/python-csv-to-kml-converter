"""
Created on 7th Sept
Author: Akshay C
"""
import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

#function to browse files
def browse():
    global  inFile
    inFile=askopenfilename()


#function to convert CSV to KML
def kmlFunction(outFile="./newLocs.kml"):
    df = pandas.read_csv(inFile)
    kml = simplekml.Kml()
    for lat, lon in zip(df["Latitude"], df["Longitude"]):
        kml.newpoint(coords=[(lon, lat)])
    kml.save(outFile)


# to create UI
root=tkinter.Tk()
root.title("KML Generator")
label=tkinter.Label(root, text="This program generates a KML file")
label.pack()
browseButton=tkinter.Button(root,text="Browse CSV", command=browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="Generate KML", command=kmlFunction)
kmlButton.pack()
root.mainloop()

