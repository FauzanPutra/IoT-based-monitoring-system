# Team Members:<br />

* M1 . Fauzan Mala Ekaputra A18KE0312 <br /> 
* M2 . Raja Falih Ghufran A18KE0324 <br />
* M3 . Mohammad Haizal Khan A17KE0317 <br />


# Project Proposal

## Problem statement

In a traditional meter reading system, energy meters only measure total consumption without information on when the energy is consumed. This increases the difficulty for consumers to estimate the bill at the end of the month. For countries that charge different prices for consumption based on time of day and the season, being able to visualize the consumption of energy in real-time can help to reduce the energy bill for the customers. Reference shows that provided with real-time feedback, homeowners' electricity consumption is reduced by approximately 3-5% on average. Although 3-5% sounds small, the relatively small percentage benefits in terms of savings are multiplied by millions of users, which eventually can cause a huge difference. Other than that, the traditional meter reading process heavily relies on human labor. For instance, the laborious task to send bills to customers needs to be done manually in the traditional meter reading system. If the customers are not in the house, the reading cannot be taken. Due to the manual reading, the meter reading is error-prone and time-consuming

From the following case here are several problems to be solved :

*  The measuring energy utilization at household is not able to accurately realize the consumer energy utilization. 
*  Traditional meter reading system relies on human resources, lower efficiency, and accuracy.
*  The procedures of sending the bills to the customer are very laborious and cumbersome. The readings cannot be taken if no one is available at the home.
*  Traditional meter reading system does not provide any scope for the user to conserve energy and does it provide energy consumption predictions for the near future that enables the user to act in a more planned way.


## Purposed topic :
to design and develop an *IoT-based monitoring system for electricity consumption recording purposes*.

## System architechture

![plot](architechture.PNG)


## Sensor

we will be using rasperberry pi 

here are the sample video of the group member accesing the raspberry pi via VNC viewer



https://user-images.githubusercontent.com/75777945/146175242-39d33112-e8b4-4d0f-9083-a4352e5d928c.mp4


## Cloud

For the cloud system we decided to use *pythonAnywhere* 

the following video shows our member setting up the system 


https://user-images.githubusercontent.com/75777945/146185044-b95c1844-e08c-448f-b2bb-68d58993d117.mp4

To complete  the requirement of the milestone we used the pythonAnywhere , but we discover that by using another software known as Grafana .
We decided to use this dashboard because grafana has a built in time series database system known as InfluxDB that can support our IoT monitoring System.


## Dashboard

InfluxDB is an open-source schemaless time-series database with optional 
closed-source components developed by InfluxData, written in Go programming 
language and optimized to handle time-series data. One of the most convenient 
feature of InfluxDB is it comes with Grafana support. Grafana is an open-source 
visualization and analytics software that allows query and visualization of the data. 
Beautiful representation of data can be formed in Grafana in various graphs and 
visualizations.

The following figure is the sample of the dashboard that is created via grafana

![dashboard](https://user-images.githubusercontent.com/75777945/146176717-f2588e67-6f8b-42d5-adfb-3afa7b351331.PNG)

# How to Run The Code 

## Set up raspberry pi OS and enable VNC,  serial port and camera

1.	Install Raspbian Buster (os for raspberry pi)
Raspbian download link: https://www.raspberrypi.org/software/
2.	Install VNC Viewer - to access raspberry pi from laptop
VNC Viewer download link: https://www.realvnc.com/en/connect/download/viewer/
3.	Insert sim card with raspbian installed into raspberry pi, connect raspberry pi with keyboard, mouse and monitor for the first time.
4.	In raspberry pi, configure time zone, language keyboard, connect to internet
5.	In Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces,
6.	Enable camera , VNC and serial port on your rasperbery pi 
7.	Then restart, type ifconfig in the terminal, look for the ip address of the raspberry pi.
8.	Enter the ip address to the vnc viewer

## Set up static ip  address for the raspberry pi

1.  Check the router ip by typing sudo route -n in the terminal
2.  In terminal, type sudo nano /etc/dhcpcd.conf
3.  Add the following code to the start of the dhcpcd.conf
```
interface wlan0
static ip_address 192.168.188.146
static routers=192.168.188.1
static domain_name_servers = 8.8.8.8 8.8.4.4

```

4. To confirm that the static ip address has been set, shutdown the raspberry pi. Power off and switch on the raspberry pi again.     Check the ip address with ifconfig again in the terminal. It should be the same as the one set in dhcpcd.conf file.

## Install OpenCV in Virtual Environment

1. update the rasperberry pi

```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
```

```
sudo apt-get install libfontconfig1-dev libcairo2-dev
sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5sudo apt-get install python3-dev

```
2. Create virtual environment and install numpy

```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo rm -rf ~/.cache/pip

```

```
sudo pip install virtualenv virtualenvwrapper
```

```
nano ~/.bashrc
```

```
mkvirtualenv cv -p python3
```

3. Activate the virtual environment

```
workon cv
```

4. Install the openCV

```
pip install opencv-contrib-python==4.1.0.25
```

## test the following OpenCV installation by running the following code

```
# import the opencv library
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

```
if you see the camera activtated that means youre ready for the next step

## installing grafana

1.	Add the APT key used to authenticate packages:

wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
2.	Add the Grafana APT repository:

echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
3.	Install Grafana:

sudo apt-get update
sudo apt-get install -y grafana
Grafana is now installed, but not yet running. 

4.	To make sure Grafana starts up even if the Raspberry Pi is restarted, we need to enable and start the Grafana Systemctl service.
Enable the Grafana server:

sudo /bin/systemctl enable grafana-server

Start the Grafana server:

sudo /bin/systemctl start grafana-server
Grafana is now running on the machine and is accessible from any device on the local network. To access the grafana:
a)	Open a browser and go to http://<ip address>:3000, where the IP address is the address that you used to connect to the Raspberry Pi earlier. You’re greeted with the Grafana login page.
  
b)	Log in to Grafana with the default username admin, and the default password admin.
  
c)	Change the password for the admin user when asked.

 ## Install InfluxDB
  
 E) Install Influx DB

1.	For users running on Raspbian OS (Raspbian Buster here), add the repository 
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -

echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
2.	Update the package list again so that the apt package manager searches the repository that we just added for packages. The operating system does not automatically do this.
sudo apt update

3.	Install the InfluxDB software.
sudo apt install influxdb

4.	To start the influxDB at boot, use the systemctl service manager to enable the InfluxDB service file.
Run the following two commands to enable InfluxDB to start at boot on your Raspberry Pi.
sudo systemctl unmask influxdb
sudo systemctl enable influxdb
The first command we use unmasks the influxdb service file. Unmasking the service ensures that we can enable and start the service as a masked service is unable to be started.

The second command enables the influxdb service. This command will tell the service manager to keep an eye on the “influxdb.service” file and set up the service based on its contents.

5.	To start up the InfluxDB server, we will need to run the following command. The service manager will then start up the service and begin monitoring it.
sudo systemctl start influxdb

Now the influxDB has been installed
To test the installation, type influx in the terminal. No errors mean installation is successful.
Some commands for InfluxDB
To talk to the database, run influx in the terminal (or influx -precision rfc3339 to open influx with readable date and time)
1.	InfluxDB comes with no databases by default, so our first task will be to create one.
To create a database: CREATE DATABASE <DBNAME>
Eg.  CREATE DATABASE mydatabase 
  
2.	Before we can start modifying our new database, we must tell the CLI to “use” it.
To use a database: USE <DBNAME>
Eg. USE mydatabase
A data point consists of the time, a measurement name such as “temperature”, and at least one field. You can also use tags which are indexed pieces of data that are a string only. Tags are essential for optimizing database lookups.
If you are familiar with the general layout of an SQL table, you can consider “time” to be the primary index, measurement as the table name, and the tags and fields as the column names.
You do not need to specify the timestamp unless you want to specify a specific time and date for the data point.
Below we have included the basic format of an InfluxDB data point.
<measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]
For this example database, we are going to be storing measurements of the “temperature” of various locations around a house.
So for this, we will be inserting data points with a measurement name of “temperature” and a tag key of “location“, and a field key of “value“.
For our first sample point, we will be saying the location is the “living_room“, and the value is “20” .
INSERT temperature,location=kitchen value=20

3.	To query this data, use “SELECT“.
Eg. SELECT * FROM temperature
Eg. SELECT value FROM temperature WHERE location='kitchen'
  
## install tesseract 
  
  ```
pip install pillow
sudo apt-get install tesseract-ocr
pip install pytesseract

  ```
## download tessdata
  
  github link for test data : https://github.com/Shreeshrii/tessdata_ssd/blob/master/ssd_alphanum_plus.traineddata
  
## RUN the code
  
Move the tessdata file to /usr/share/tesseract-ocr/4.00/tessdata/
cd FYP_Automated_Meter_Reading

sudo mv ssd_alphanum_plus.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

Once everything is set up, run the program with 
python main.py

 


