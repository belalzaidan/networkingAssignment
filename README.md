
# DATA2410 - Oblig 1

### Achieved goals behind this assignment.

In this assignment, we have:

- Explored the concept of Fairness Metric in computer networks and built our own program to calculate Jains Fairness Index.

- Implemented Python programs for tasks involving JFI calculation from throughput values and optional arguments handling.

- Utilized the ping utility to measure round-trip times to different hosts and analyzed the results.

- Conducted a traceroute to a remote host to understand the path discovery process.

- Prepared files with explanations for ping and traceroute results as part of the assignment submission requirements.

$~$
#### \#  **1 - Jains Fairness Index**

This part involved creating a Python program for calculating the Jain's Fairness Index (JFI). Initially, separate functions were created for each subtask. However, to optimize the program, the argparse module was used, enabling both list and file inputs in one script.

_1.1 - Task 1_


In the first task, we had to build a simple Jain's Fairness Index calculating function. This function takes the arguments from the terminal, calcuates the JFI and returns it, using this formula:

> 𝒥𝐹𝐼 = ( ∑𝑛 𝑖=1 𝑥𝑖 )^2 / 𝑛 * ∑𝑛 𝑖=1 𝑥𝑖^2

 Here's an example on input and output:

**Input:**
```
python3 jains.py [10,10,10]
```
**Output:**
```
Jains Fairness index is: 1.000
```
$~$

_1.2 - Task 2_

In this part, the program is extended to read throughput values from a file. We then use the JFI function from task 1.1 to calculate a JFI.

The program can handle inputs either directly from the terminal or from a file. Upon an invalid input, the program throws an exception and provides an error message.

Here's an example on input and output:

**Input:**
```
python3 jains.py -f ./throughput_values.txt
```
**Output:**
```
Jains Fairness index is: 0.586
```
$~$
#### \# **Task 2 - Argparse module**
_2.1 - Task 3_

This part involved creating a Python program that operates in either server (-s) or client (-c) mode. The program accepts host IP and port as optional arguments and ensures only one mode is chosen. In server mode, it listens for connections and echoes received data. In client mode, it sends a message to the server and receives a response. Default values are used if no IP or port is specified. With inavlid inputs, error messages are returned.

Examples on how you can run the program:

**✶ Server mode:**
```
python3 args.py -s -i 127.0.1.1 -p 22000
```
**✶ Client mode:**
```
python3 args.py -c -m "A message to the server"
```
$~$
#### \# **3 - Measuring round-trip time with Ping**
_3.1 - Task 4_

In this part, we performed network ping tests to various hosts, analyzed the round-trip times (RTT), and to explain the differences in minimum RTT, we can talk about many aspects. 

First of all **geographical distance**. During our analysis of round-trip time (RTT), we observed that the distance between the client and the server hosting the specific IP address significantly increases response times. For example, when accessing a local website like _oslomet.no_, the average response time was remarkably low, around 12 milliseconds. Meanwhile, when connecting to a distant server, such as _sydney.edu.au_ in Australia, the average response time was up to approximately 270 milliseconds, and this was also observed in the other tests, where the more distant a server is located, the longer it takes for its response to be recieved. Distance isn't the only determinant of online responsiveness. Other contributing factors include network queuing, the type of network, and packet loss. Together, variables shape the speed at which websites interact with users.

$~$
#### \# **4 - Internet Routes with traceroute / tracert**

_4.1 - Task 5_

This part required us to use the traceroute tool to trace the complete route from our computer to www.google.com. This is simply the idea behind traceroute, AKA tracert, where it visits every station it stops through before reaching the remote host, and then returns whether the connection succeeded or failed. The way traceroute works is by sending packets with increasing TTL values, starting at 1. Each router encountered decreases the TTL. When TTL expires, routers reply with their IP and timing data. Traceroute repeats with higher TTL until reaching the destination, recording IPs to map the route. However, results may vary due to differing traffic priorities among routers. Traceroute relies on ICMP (Internet Control Message Protocols), which some systems may block, and that may lead us to incomplete data. Still, it's a very important tool that lets us diagonise network problems and understand internet data flow.

