#!/usr/bin/env/python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="use the interface argument with the python script to change its MAC address")
    return parser.parse_args()

def change_mac(interface):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["macchanger", "-r", interface])
    subprocess.call(["ifconfig", interface, "up"])
    print("Congratulations you have changed your MAC address for " + interface + " Thank you for using Random MAC by Fingas")

(options,arguments) = get_arguments()
change_mac(options.interface)
