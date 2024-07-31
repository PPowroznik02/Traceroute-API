## Wheelchair model

Model defines generation of paths for disabled persons moving on wheelchair. 
Model configuration file: [wheelchair](wheelchair.json)

### Speed
Default speed of wcheelchair is  3 km/h, it is modify by restrictions wiriten in the table below.
|  Class  | Property |  Restriction |
| ------------- | ------------- | ------------- |
| Road type  |  Primary  |  4 km/h  |
| Road type  |  Secondary  |  4 km/h  |
| Surface  |  Asphalt  |  5 km/h  |
| Surface  |  Paved  |  5 km/h  |
| Surface  |  Gravel  |  3 km/h  |
| Surface  |  Dirt  |  1 km/h  |
| Smoothness  |  Excellent  |  5 km/h  |
| Smoothness  |  Good  |  4 km/h  |
| Smoothness  |  Intermediate  |  3 km/h  |
| Smoothness  |  Bad  |  1 km/h  |
| Max slope  |  Bigger then 6%  |  1 km/h  |
| Max slope  |  Smaller then 6% |  3 km/h  |


### Priority restrictions

Default priority is set to 1, it is modify by restrictions wiriten in the table below.

| Class  | Property |  Muliplier  |
| ------------- | ------------- | ------------- |
|  Road access  |  Private  |  0  |
|  Road  |  Primary  |  0.3  |
|  Road  |  Secondary  |  0.7  |
|  Road  |  Pedestrian  |  1  |
|  Road  |  Steps  |  0  |
|  Surface  |  Asphalt  |  1  |
|  Surface  |  Paved  |  1  |
|  Surface  |  Gravel  |  0.5  |
|  Surface  |  Dirt  |  0.3  |
|  Smoothness  |  Excellent  |  1  |
|  Smoothness  |  Good  |  0.8  |
|  Smoothness  |  Intermediate  |  0.5  |
|  Smoothness  |  Bad  |  0.1  |
|  Max slope  |  Bigger then 6%  |  0.2  |


