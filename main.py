import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('YOUR NETWORK IP HERE')
IP_DEVICE = config('YOUR DEVICE IP HERE')

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  connected_ip = line.decode('utf-8').split()[3]

  if connected_ip == IP_DEVICE:
      subprocess.Popen(["say", "Luke just connected to the network"])
