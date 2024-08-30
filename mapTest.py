import pandas as pd
import folium as F
csvFile = pd.read_csv("LongBoi.csv")

#53.0765452103364, 8.820692530590472
map = F.Map(location=(csvFile.iloc[0]["latitude"], csvFile.iloc[0]["longitude"]), zoom_start=12)
F.Marker((csvFile.iloc[0]["latitude"], csvFile.iloc[0]["longitude"]), popup='Binaur').add_to(map)
points = []

for i in range(len(csvFile)):
    points.append((csvFile.iloc[i]["latitude"], csvFile.iloc[i]["longitude"]))

F.PolyLine(locations=points, color='blue', popup="William").add_to(map)

map.show_in_browser()
map.save("Map.html")