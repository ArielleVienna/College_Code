import arcpy
#1: Create Script for Unique value or Graduated Color map
# path to the already created ArcGIS Pro Project
project = arcpy.mp.ArcGISProject(r"D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab06\392_Lab06.aprx")
# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check if layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Check if it has a 'renderer' attribute
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is 'GarageParking'
            if layer.name == "GarageParking":
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                # Tell arcpy which field we want to base our choropleth off of
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have 
                symbology.renderer.breakCount = 5
                # Set the color ramp
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT GarageParking")
# Save this copy in the same folder, but a different file name. We do not want to overwrite the original file!
project.saveACopy(r"D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab06\392_Lab06_Created.aprx")

print("it worked!")
