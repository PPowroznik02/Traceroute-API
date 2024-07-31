## Car delivery model

Model defines generation of paths for delivery cars.
Model configuration file: [car delivery](car_delivery.json)

### Speed
Default speed is set to car avarage speed, it is modify by restrictions wiriten in the table below.
|  Class  | Property |  Restriction |
| ------------- | ------------- | ------------- |
| Road  |  Motorway  |  130 km/h  |
| Road  |  Trunk  |  80 km/h  |
| Road  |  Primary  |  60 km/h  |
| Road  |  Secondary  |  50 km/h |
| Road  |  Tertiary  |  40 km/h  |
| Road  |  Residential  |  30 km/h  |
| Road  |  Service  |  20 km/h  |



### Priority restrictions

Default priority is set to 1, it is modify by restrictions wiriten in the table below.

| Class  | Property |  Muliplier  |
| ------------- | ------------- | ------------- |
|  Access  |  Delivery  |  1  |
|  Access  |  Private  |  1  |
|  Acces  |  By car  |  0.4  |
|  Road  |  Motorway  |  0.5  |
|  Road  |  Trunk  |  0.7  |
|  Road  |  Primary  |  1  |
|  Road  |  Secondary  |  0.9  |
|  Road  |  Tertiary  |  0.8  |
|  Road  |  Residential  |  0.8  |
|  Road  |  Service  |  0.6  |

