import re
import subprocess as sp
import time

from geopy.geocoders import Nominatim


def coords():  ##This is getting the gps location where you curently at and we will use this to find the current weather conditions off that place
    wt = 5
    accuracy = 3
    while True:
        print('Locatie word opgevraagd even geduld aub.')
        print('10%')
        time.sleep(1)
        print('20%')
        time.sleep(1)
        print('30%')
        time.sleep(1)
        print('40%')
        time.sleep(1)
        print('50%')
        time.sleep(1)
        print('60%')
        time.sleep(0.5)
        print('70%')
        pshellcomm = ['powershell']
        pshellcomm.append('add-type -assemblyname system.device; ' \
                          '$loc = new-object system.device.location.geocoordinatewatcher;' \
                          '$loc.start(); ' \
                          'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) ' \
                          '{start-sleep -milliseconds 100}; ' \
                          '$acc = %d; ' \
                          'while($loc.position.location.horizontalaccuracy -gt $acc) ' \
                          '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; ' \
                          '$loc.position.location.latitude; ' \
                          '$loc.position.location.longitude; ' \
                          '$loc.position.location.horizontalaccuracy; ' \
                          '$loc.stop()' % (accuracy))
        p = sp.Popen(pshellcomm, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        (out, err) = p.communicate()
        out = re.split('\n', out)
        lat = out[0]
        long = out[1]
        lat = '&lat=' + lat
        long = '&lon=' + long
        return lat + long


def coordscityname():  ##This is getting the GPS state location and we will use this to add to our GUI later.
    wt = 5
    accuracy = 3
    while True:
        time.sleep(1)
        print('80%')
        time.sleep(1)
        print('90%')
        time.sleep(1)
        print('99%')
        time.sleep(1)
        print('Done')
        pshellcomm = ['powershell']
        pshellcomm.append('add-type -assemblyname system.device; ' \
                          '$loc = new-object system.device.location.geocoordinatewatcher;' \
                          '$loc.start(); ' \
                          'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) ' \
                          '{start-sleep -milliseconds 100}; ' \
                          '$acc = %d; ' \
                          'while($loc.position.location.horizontalaccuracy -gt $acc) ' \
                          '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; ' \
                          '$loc.position.location.latitude; ' \
                          '$loc.position.location.longitude; ' \
                          '$loc.position.location.horizontalaccuracy; ' \
                          '$loc.stop()' % (accuracy))
        p = sp.Popen(pshellcomm, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        (out, err) = p.communicate()
        out = re.split('\n', out)
        lat = out[0]
        long = out[1]
        geolocator = Nominatim(user_agent="geoapiExercises")
        Latitude = lat
        Longitude = long
        Latitude = Latitude.replace(',', '.')
        Longitude = Longitude.replace(',', '.')
        location = geolocator.reverse(Latitude + "," + Longitude)
        address = location.raw['address']
        state = address.get('state')
        return state

    ## I did not write this code. This code is from https://stackoverflow.com/users/13530325/j-f-22
