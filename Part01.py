import arcpy 
arcpy.env.workspace = r'D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab04'
#arcpy.CreateFileGDB_management(arcpy.env.workspace, 'Lab05.gdb')

csv_path = r'D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab04\garages.csv'
garage_name = 'Garage_Points'
garagesXY = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_name)

input_layer = garagesXY
arcpy.FeatureClassToGeodatabase_conversion(input_layer, arcpy.env.workspace + '\Lab05.gdb')
workspace = r'D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab04\Lab05.gdb'
garage_points = workspace +  '\\' + garage_name

campus = r'D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings =  workspace + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, workspace + '\GaragePointsReprojected', spatial_ref)

garageName_input = input('Please Enter a Garage Name: ')
bufferSize_input = int(input('Please Enter a Buffer Size: '))


whereClause ="Name = '%s'" % garageName_input

GaragePointsReprojected = workspace + '\GaragePointsReprojected'
cursor = arcpy.SearchCursor(GaragePointsReprojected, where_clause=whereClause)

shouldProceed = False
for row in cursor:
    if row.getValue("Name") == garageName_input:
        shouldProceed = True

if shouldProceed:
    buildingBuff = "\Copy_%s_Buffer_%s" % (garageName_input, bufferSize_input)
    buildingFeature = arcpy.Select_analysis(GaragePointsReprojected, workspace + "\Copy_%s" % (garageName_input), whereClause)
    garageBuffered = arcpy.Buffer_analysis(buildingFeature, workspace + buildingBuff, bufferSize_input)
    arcpy.Intersect_analysis([garageBuffered, buildings], workspace + '\garage_building_intersection', 'ALL')
    arcpy.TableToTable_conversion(workspace + '\garage_building_intersection.dbf', 'D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab04', 'nearbyBuildings01.csv' )
    print("It worked!")

else:
    print("It failed...")