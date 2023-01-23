
#include "WiFi.h"
#include <Wire.h>

  int rssi1;
  int rssi2;
  int rssi3;
  int rssi4;
  int rssi5;

  bool opinionator_detection;
  bool forest_detection;
  bool emotion_detection;
  bool animal_detection;
  bool philip_detection;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  Serial.println("Setup done");

  //set the initial values of the variables
  rssi5 = 100;
  rssi4 = 100;
  rssi3 = 100;
  rssi2 = 100;
  rssi1 = 100;

  // Start the I2C Bus as Master
  Wire.begin();
}

void loop() {
  
  if (WiFi.scanComplete() == -2){
    int n = WiFi.scanNetworks(true, true);
    Serial.println("scanning start");
    //do the calculations while the new scan is on
    if(rssi1 < rssi2 and rssi1 < rssi3 and rssi1 < rssi4 and rssi1 < rssi5) {
      //send wifi1
      int x = 1;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi2 and rssi2 < rssi3 and rssi2 < rssi4 and rssi2 < rssi5) {
      //send wifi2
      int x = 2;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi3 and rssi2 > rssi3 and rssi3 < rssi4 and rssi3 < rssi5) {
      //send wifi3
      int x = 3;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi4 and rssi2 > rssi4 and rssi3 > rssi4 and rssi4 < rssi5) {
      //send wifi4
      int x = 4;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi5 and rssi2 > rssi5 and rssi3 > rssi5 and rssi4 > rssi5) {
      //send wifi5
      int x = 5;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    }
    if(rssi1 > 80 and rssi2 > 80 and rssi3 > 80 and rssi4 > 80 and rssi5 >80) {
      int x = 6;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    }
  }
  if (WiFi.scanComplete() == -1){
    Serial.println("In progress");
    if(rssi1 < rssi2 and rssi1 < rssi3 and rssi1 < rssi4 and rssi1 < rssi5) {
      //send wifi1
      int x = 1;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi2 and rssi2 < rssi3 and rssi2 < rssi4 and rssi2 < rssi5) {
      //send wifi2
      int x = 2;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi3 and rssi2 > rssi3 and rssi3 < rssi4 and rssi3 < rssi5) {
      //send wifi3
      int x = 3;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi4 and rssi2 > rssi4 and rssi3 > rssi4 and rssi4 < rssi5) {
      //send wifi4
      int x = 4;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    } else if (rssi1 > rssi5 and rssi2 > rssi5 and rssi3 > rssi5 and rssi4 > rssi5) {
      //send wifi5
      int x = 5;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    };
    if(rssi1 > 80 and rssi2 > 80 and rssi3 > 80 and rssi4 > 80 and rssi5 >80) {
      int x = 6;
      Wire.beginTransmission(0x41); // transmit to device #9
      Wire.write(x);              // sends x 
      Wire.endTransmission();    // stop transmitting
      Serial.println("Transmission send with:");
      Serial.println(x);
    }
  }
  if (WiFi.scanComplete() > 0) {
    Serial.println("Scan complete");
    opinionator_detection = false;
    forest_detection = false;
    emotion_detection = false;
    animal_detection = false;
    philip_detection = false;
    //Serial.println(WiFi.scanComplete());
    for (int i = 0; i < WiFi.scanComplete(); ++i) {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
      if(WiFi.SSID(i) == "opinionator") {
        rssi1 = abs(WiFi.RSSI(i));
        opinionator_detection = true;
      } else if (WiFi.SSID(i) == "emotion") {
        rssi2 = abs(WiFi.RSSI(i));
        emotion_detection = true;
        Serial.print(emotion_detection);
      } else if (WiFi.SSID(i) == "forest") {
        rssi3 = abs(WiFi.RSSI(i));
        forest_detection = true;
      }
      else if (WiFi.SSID(i) == "animal") {
        rssi4 = abs(WiFi.RSSI(i));
        animal_detection = true;
      } else if (WiFi.SSID(i) == "phillip") {
        rssi5 = abs(WiFi.RSSI(i));
        philip_detection = true;
      }
     }
     //clean up
     Serial.print(emotion_detection);
     if(!opinionator_detection) {
      rssi1 = 100;
      Serial.println("No opinion");
     }
     if (!forest_detection) {
      rssi3 = 100;
       Serial.println("No forest");
     }
     if (!emotion_detection) {
      rssi2 = 100;
      Serial.println("No emotion");
     }
     if (!animal_detection) {
      rssi4 = 100;
     }
     if(!philip_detection) {
      rssi5 = 100;
     }
    Serial.println(rssi2); 
    WiFi.scanDelete();
  }
  //Serial.println("Booo!");
  delay(100);
}
