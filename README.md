# Inflatable Cushion

The purpose of the of this solution is to provide and controllable cushion using an ESP8266, solenoid valves, relays and an air pump.
Parts
1.	Inflatable cushion stack
2.	Controller Unit
3.	Pump (Coleman Quick pump 120V)
4.	Router (TP-LINK  TL-WR740N)
   

![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/OKVAE4334_2.png "PARTS")
![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/router2.jpg "ROUTER")

## Basic Setup

### Connect the router
Connect the router to power (The router supports a wide variety of voltages) the default SSID BEDTEST and the default password is bedtest01, the Controller Unit will connect automatically to the router using the default SSID and password.
Hint: You can plug the router to your house internet using the ethernet cable, the router will act as an extension of your main internet. 
Connect the Controller Unit
Plug the Controller Unit to the Power, the ESP8266 inside the Controller Unit will connect automatically to the router. Once the Controller Unit and the Router are connected controller unit will flash a blue LED twice and power the Pump and solenoid valves for 1 second.
Warning: The controller unit supports US and EU power, but the air pump is only rated to 120V. I have not tested the pump I higher voltages

### Control the Controller Unit
Connect to the router using any smart phone or computer using SSID BEDTEST and password bedtest01. Once connected use the following URLs to control the Controller Uni.

| URL | DESCRIPTION |
| ------ | ------ |
| http://192.168.0.101/?pump=on | Inflate the cushion |
| http://192.168.0.101/?pump=off | Deflate the cushion |
| http://192.168.0.101/?pump=stop | Stop pump and close the valves |

Hit: Save the URLs to your smart phone Home Screen on iOS and Android

### Performance Issues
Due to performance issues with the air pump not having enough suction power, the deflate function is not working as expected, unplug the connector from the pump right side (long tube) and leave it unplugged. To deflate the cushion, unplug the tube from the cushion.
 
![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/OKVAE4334_4.png "Dont Connect")

## Component Details

### Cushion Stack
The stack is composed of 3 layers. The bottom 2 layers are inflatable and the top layer is stuffed cushion. All the layers are held together using Velcro strips.
Hit: The cushion stack has security belts at the bottom in order to secure it to the bed. 

### Controller Unit

The controller unit uses custom 3D printed parts in order to connect the solenoid valves (1/2 threaded pipe) and the vinyl tube (5/8)
   
Using Relays, the solenoid valves are turned on of by the microcontroller


## Air Flow

### Inflate
Then the Controller unit is se to Inflate the 

![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/inflate.jpg "Inflate Air Flow")
 
### Deflate
The opposite happens when the Controller Unit is set to deflate redirecting the air flow without having to reverse the motor. 
![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/deflate.jpg "Defalte Air Flow")

## DIAGRAM
 
![alt text](https://raw.githubusercontent.com/markwinap/Inflatable-Cushion/master/Images/Diagram.png "Diagram")

## FUSION 360 Models
https://a360.co/2Kxu4mj