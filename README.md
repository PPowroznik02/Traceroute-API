## Installation

To install the [GraphHopper Maps](https://graphhopper.com/maps/) UI and the web service locally you [need a JVM](https://adoptium.net) (>= Java 17). Next you should copy [repistory](https://github.com/Geoinformatics-Applications-Python/final-project-super-awesome-team-name/tree/main) and [install graphhopper](https://repo1.maven.org/maven2/com/graphhopper/graphhopper-web/9.1/graphhopper-web-9.1.jar) into downloaded repistory.

This project uses several [packages](requirements.txt) that you need to install in your base environment or you can create a virtual environment with base Python 3.12 and the [requirements](requirements.txt) file.

To run FastApi you need to install uvicorn. You can do it via terminal with command:  

```bash
pip install uvicorn
```

## Execution

To run the application, run [main](main.py) file with the name of the city you are interested in specified in the argument of the uruchom() function. Make sure you enter the city name in English. 
After running, the console will ask you if you want to delete the graph-cache folder. If you are running the application again for the same city, enter 'N' in the console, and if you are running the application for a different city than the last time, enter 'Y' in the console.

## Usage
Once you executed API u can acces it under [this address](http://localhost:8000/docs).

On the fastAPI website you can enter start location, destination and [model](/models/README.md) type (car_delivery/hiking/custom/inline_skates/wheelchair). FastAPI returns .json file which contains linestring and descriptions of the route stages.

Visualization of this route is displayed under address [this address](http://localhost:8989).


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Itx05xVz)
