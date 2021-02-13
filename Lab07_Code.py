#can combine all the 7 bands for the Landsat Image. You could emit band 6 though since that is a thermal band. 
import arcpy

#If does not run, change .TIF to .tif

# RS Composite Bands - bringing them in and combining them. 
source = r"D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab07"
band1 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B1.TIF")
band2 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B2.TIF")
band3 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B3.TIF")
band4 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B4.TIF")
band5 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B5.TIF")
band7 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B7.TIF")
composite = arcpy.CompositeBands_management([band1, band2, band3, band4, band5, band7], source + "\combined.TIF")

# Hillshade - creating the Hillshade
source = r"D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab07"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.TIF", source + r"\Hillshade.TIF", azimuth, altitude, shadows, z_factor)

# Slope - creating the Slope
source = r"D:\Fall Semester Senior Year\GIS Programming (GEOG 392)\Lab07"
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.TIF", source + r"\Slope.TIF", output_measurement, z_factor) 

print("It worked!")


