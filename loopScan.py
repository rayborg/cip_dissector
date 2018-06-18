import os
import time

#To test the code below replay traffic to 'lo' interface with
#sudo tcpreplay --multiplier=1.0 --intf1=lo testReplay.pcap

def main():
    try:
        while True:
            os.system('dumpcap -i lo -a duration:05 -w fiveSec.pcap')
            time.sleep(6)
            os.system('tshark -Y "enip.command == 0x0070 and ip.src==192.168.1.7" -E header=n -T fields -E separator=, '
                      '-e cip.data -r fiveSec.pcap | gawk -F ":" \'{sensor1="0x"$23$22; print strtonum(sensor1)}\' '
                      '> cipData.data')

            #add above for graphs "| gnuplot - e "plot '-' u 0:1 w linespoints" - persist"

            time.sleep(1)
    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == "__main__":
    main()
