import gdal, os

## List input raster files
os.chdir("YOUR_TARGET_DIRECTORY_THAT_HAS_THE_HDF5")
rasterFiles = os.listdir(os.getcwd())
print(rasterFiles)


fileExtension = ".tif"

## Open HDF file
#Ignores first file cause zero-based index so range 0
for i in range(0,len(rasterFiles)) :
  
  #Get File Name Prefix
  rasterFilePre = rasterFiles[i][:-3]
  print(rasterFilePre)

  #Iterate because gdal only takes 1 string
  hdflayer = gdal.Open(rasterFiles[i], gdal.GA_ReadOnly)
  
  #print (hdflayer.GetSubDatasets())
  # Open raster layer
  #hdflayer.GetSubDatasets()[0][0] - for first layer
  #hdflayer.GetSubDatasets()[1][0] - for second layer ...etc
  
 
 #to extract DNB at sensor radiance its the 5 layer, thus 
  subhdflayer = hdflayer.GetSubDatasets()[4][0]
  
  rlayer = gdal.Open(subhdflayer, gdal.GA_ReadOnly)
  #outputName = rlayer.GetMetadata_Dict()['long_name']
  
  #Subset the Long Name
  outputName = subhdflayer[92:] #REVIEW THIS SECTION TO GET THE NAME RIGHT
  outputNameNoSpace = outputName.strip().replace(" ","_").replace("/","_")
  outputNameFinal = outputNameNoSpace + rasterFilePre + fileExtension
  print(outputNameFinal)
  #Serves the wrong folder, one up the folder
  outputFolder = "YOUR_OUTPUT_DIRECTORY"
  
  outputRaster = outputFolder + outputNameFinal
  
  #collect bounding box coordinates
  HorizontalTileNumber = int(rlayer.GetMetadata_Dict()["HorizontalTileNumber"])
  VerticalTileNumber = int(rlayer.GetMetadata_Dict()["VerticalTileNumber"])
  WestBoundCoord = (10*HorizontalTileNumber) - 180
  NorthBoundCoord = 90-(10*VerticalTileNumber)
  EastBoundCoord = WestBoundCoord + 10
  SouthBoundCoord = NorthBoundCoord - 10
  EPSG = "-a_srs EPSG:4326" #WGS84
  
  translateOptionText = EPSG+" -a_ullr " + str(WestBoundCoord) + " " + str(NorthBoundCoord) + " " + str(EastBoundCoord) + " " + str(SouthBoundCoord)
  
  translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine(translateOptionText))
  gdal.Translate(outputRaster,rlayer, options=translateoptions)
  
  print("Output %d ready with name: %s" % (i,outputNameFinal))
  #Display image in QGIS (run it within QGIS python Console) - remove comment to display
  #iface.addRasterLayer(outputRaster, outputNameFinal)
