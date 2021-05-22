import os

def install_function():   
    
    
    os.system('picovoice_demo_mic \
    --keyword_path resources/porcupine/resources/keyword_files/raspberry-pi/porcupine_raspberry-pi.ppn \
    --context_path resources/rhino/resources/contexts/raspberry-pi/smart_lighting_raspberry-pi.rhn')
      
install_function()
