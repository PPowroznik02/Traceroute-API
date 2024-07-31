## Hiking model

Model defines generation of paths hinking. 
Model configuration file: [hiking](hiking.json)

### Speed
Default hiking speed is foot avarage speed, it is modify by restrictions wiriten in the table below.

|  Class  | Property |  Muliplier |
| ------------- | ------------- | ------------- |
| Surface  |  Gravel  |  0.8  |
| Surface  |  Dirt  |  0.7 |
| Smoothness  |  Bad  |  0.8  |
| Max slope  |  Bigger then 5%  |  0.9 |
| Max slope  |  Bigger then 10%  |  0.8  |
| Max slope  |  Bigger then 15% |  0.7  |
| Max slope  |  Bigger then 20%  |  0.6  |
| Max slope  |  Bigger then 25%  |  0.45  |
| Max slope  |  Bigger then 30% |  0.35 |




### Priority restrictions

Default priority is set to 1, it is modify by restrictions wiriten in the table below.

| Class  | Property |  Muliplier  |
| ------------- | ------------- | ------------- |
|  Road  |  Primary  |  0.1  |
|  Road  |  Secondary  |  0.1  |
|  Road  |  Pedestrian  |  0.5  |
|  Road  |  Track  |  1  |
|  Road  |  Path  |  1  |
|  Road  |  Tertiary  |  0.5  |
|  Road  |  Residential  |  0.1  |
|  Road  |  Service  |  0.1  |
|  Road  |  Footway  |  0.5  |
|  Foot network  |  Missing  |  1  |
|  Surface  |  Asphalt  |  0.4  |
|  Surface  |  Paved  |  0.8  |
|  Surface  |  Gravel  |  1  |
|  Surface  |  Dirt  |  1  |
|  Max slope  |  Bigger then 10%  |  0.8  |
|  Max slope  |  Less then 10%  |  1  |
