# Measuring-Inequality-with-Satellite-Images

## The case of Mexico

This project uses the VNP46 products from the Black Marble product suite developed by [Román et al. (2020,2021)](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_UG_v1.2_April_2021.pdf).

The project is planned with several stages in mind: __prototype__, __masive downloads__, __data analysis and modeling__, and lastly __sharing the results through diverse data products__. 

## Results of the __prototype__

### Summary

The objetive of the prototype was to develop a simple model a simple econometric model that would use __VNP46__ data and other auxiliary variables to estimate __average per capita income__ of the __alcaldias__ in the __Metropolitan Zone of Mexico City__. 

Using 2015 available government data to fit the model and 2020 data to create estimations, __the resulting model was able to predict an increase in inequality between the __alcaldias__ for the year 2020. 

This was on 2020. 
This prototype proved successful in utilizing the VNP46 data products. This particular research used the VNP46A1 product due to low data availability of other data products. This data product has multiple downsides regarding artifac effects, but are the first step to more polished products ([Román et al. (2020,2021)](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_UG_v1.2_April_2021.pdf)).

### Lessons learned from prototyping

#### Data variety and transformation

The main lesson is that the data product comes in many shapes. Data comes in HDF5 format with 26 layers but requires transformation to GeoTiff to add geographyc projection coordinates; NASA offers a python script as a starting point.

In 2021, [Román et al. (2021)](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_UG_v1.2_April_2021.pdf) published 2 new datasets: the VNP46A3 and the VNP46A4. These offer monthly and yearly pixel level mean observations, and temporal coverage has increased drastically.

If you wish to learn more and download these data products visit the [LAADS DAAC website](https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VNP46A1--5000). Below a the tile grid used by the Black Marble Product Suite (Román et al. (2020):

![Black Marble Tiles 35 horizontal and 17 vertical. The metropolitan zone of mexico city uses only h08 v07](https://github.com/dar4datascience/Measuring-Inequality-with-Satellite-Images/blob/main/proyect_snapshots/ntlGridRoman2020.jpg)

#### Flexibility

High temporal availability and pixel level readings allow the reseacher to select and zoom-in the desired area of research. In the area of economics, this idea is not new (McGregor et al., 2019), but this has never been tried for mexican capital metropolis until now.

Data was downloaded following the instructions of NASA to use `GNU wget`. An example txt script called `downloadVNP46A1.txt` is available under scripts for the researcher to get familiarized with this procedure. 

Then using python, I extracted the layer of interest for the protype and transformed the data into GeoTiff. Finally using R and the [`terra`](https://rspatial.org/terra/pkg/1-introduction.html) package I cropped the tiles downloaded to the metropolitan zone and aggregated the __pixel values__ to __municipality median aggregates__.


This process is poorly documented in `ReduceRasters.Rmd` and `HDF2GeoTiff.py`; I promise to be more clear in the next phase of the project.

Below a raw image of how the downloaded tiles look; this particular tile is from the 28 of february, the day the first COVID-19 case was reported in Mexico (Milenio, 2020; ElPaís, 2020; BBC News, 2020). Next to the image is the result of combining daily values to yearly municipality data points. These two particular plots to the right show the change in __median night time light intensity__ from the VNP46A1 and __average per capita municipal income__ from Vargas Chanes D. (coord., 2020): La desigualdad y la estructura de la ocupación en la Ciudad de México, área metropolitana y zona centro.


![3 maps. First to the left is a raw image where the cloudy formation are pixel level light intensity levels and the other two are municipal level readings of average per capita income and light intensity level of the municipalities of the metropolitan zone of mexico city](https://github.com/dar4datascience/Measuring-Inequality-with-Satellite-Images/blob/main/proyect_snapshots/resultsMap.jpg)
 
#### Read the full research!

If you got all the way down here you might be interesting in reading my bachelors thesis, were I go into depth about the Black Marble data and its potential from inequality research.

[PENDING LINK TO FINAL THESIS VERSION]

Below a plot depicting the relationship between __average per capita municipal data__ with the aggregated __vnp46A1 median municipal__ values.

![this scatter plot depicts the quas linear relationship between average income and ligth intensity per municipality. at the borders shows marginal distribution plots which are histograms at the edges of the scatter plot](https://github.com/dar4datascience/Measuring-Inequality-with-Satellite-Images/blob/Prototype-and-Bachelors-Thesis/proyect_snapshots/marginalNTLtoIngreso.png)

## STAGE 2: Massive data download of the VNP46A3 and A4

The next phase is to download the 2012 data all the up to 2021 for a more extend analysis of all of Mexico, thought smaller project analyses might pop-up.




