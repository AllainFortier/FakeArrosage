'''
Created on Sep 5, 2013

@author: ALLA
'''
import string

import pywapi


    
def test():
    weather_com_result = pywapi.get_weather_from_weather_com('CAXX0225')
    
    print pywapi.get_location_ids("kingston, CA")
    
    print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Kingston.\n\n"