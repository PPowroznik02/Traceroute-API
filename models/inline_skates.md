## Inline skates model

Model defines generation of paths for inline skaters. 
Model configuration file: [inline skates](inline_skates.json)

### Speed
Default speed of inline skates is 22 km/h, it is modify by restrictions wiriten in the table below.
|  Class  | Property |  Restriction |
| ------------- | ------------- | ------------- |
| Road  |  Primary  |  22 km/h  |
| Road  |  Secondary  |  22 km/h |
| Road  |  Pedestrian  |  18 km/h  |
| Surface  |  Paved  |  16 km/h  |
| Surface  |  Asphalt  |  24 km/h  |
| Surface  |  Gravel  |  3 km/h  |
| Surface  |  Dirt  |  3 km/h  |
| Smoothness  |  Excellent  |  24 km/h  |
| Smoothness  |  Good  |  22 km/h  |
| Smoothness  |  Intermediate  |  20 km/h  |
| Smoothness  |  Bad  |  15 km/h  |
| Max slope  |  Bigger then 5%  |  17 km/h  |
| Max slope  |  Bigger then 10%  |  12 km/h  |
| Max slope  |  Smaller then 5% |  22 km/h  |


### Priority restrictions

Default priority is set to 1, it is modify by restrictions wiriten in the table below.

| Class  | Property |  Muliplier  |
| ------------- | ------------- | ------------- |
|  Road  |  Primary  |  0.4  |
|  Road  |  Secondary  |  1  |
|  Road  |  Pedestrian  |  1  |
|  Road  |  Steps  |  0.1  |
|  Surface  |  Asphalt  |  1  |
|  Surface  |  Paved  |  0.4  |
|  Surface  |  Gravel  |  0.1  |
|  Surface  |  Dirt  |  0.1  |
|  Smoothness  |  Excellent  |  1  |
|  Smoothness  |  Good  |  0.9  |
|  Smoothness  |  Intermediate  |  0.6  |
|  Smoothness  |  Bad  |  0.1  |
|  Max slope  |  Bigger then 10%  |  0.1  |

