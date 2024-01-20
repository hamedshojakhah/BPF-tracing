# Determining network stack latency using BPF tool

BPF Compiler Collection (BCC) is a library, which facilitates the creation of the extended Berkeley Packet Filter (eBPF) programs. The main utility of eBPF programs is analyzing the operating system performance and network performance without experiencing overhead or security issues.

BCC removes the need for users to know deep technical details of eBPF, and provides many out-of-the-box starting points, such as the  `bcc-tools`  package with pre-created eBPF programs.


# I-network Tracing by BPF tools


Determining network stack validity using eBPF tool in ubuntu agent


##   Project definition:

  Project definition:
The project has been to understand the platform's transmission latency in the network and to measure interrupt handling (IRQ). These measurements are very important in order to optimize and improve the efficiency of the network in order to increase the efficiency, speed and accuracy of data transmission.
This project aims to determine the packet's delay when passing through the network stack from the moment the interrupt request (IRQ) is sent to the application layer, and this project can also be used to determine this limitation in the vice versa. And the most important tool used in this project for this project is eBPF (Extended Berkeley Packet Filter) which allows for accurate monitoring and measurement in different sections in network stacks.
The results of this project, in addition to understanding the network delay, also give the factors that play a role in it. The project will create a set of tools, protocols and methodologies that can be used to identify challenges and build future networks. The findings of this project have the potential to significantly improve network performance and efficiency.
The findings of this project are projects that not only contribute to the existing body of knowledge on network stack latency, but also provide practical tools and strategies to improve network performance and efficiency. This project demonstrates part of the ability and power of tools such as eBPF in monitoring the network and using it to improve the network and paves the way for future research and innovation in this field.

**1-**Introduction**:**
Berkeley packet filters (BPF) provide a powerful tool for intrusion detection analysis. Use BPF filtering to quickly reduce large packet captures to a reduced set of results by filtering based on specific traffic types. Both admin and non-admin users can create BPF filters.
**1-1- Project background**
Optimizing and eliminating as much delay as possible, as well as increasing efficiency in the network, has been an interesting and challenging topic for engineers and researchers in the field of computers and networks. Despite the advances in network technologies, determining the latency of a network or its infrastructure (especially in the network stack) is still a complex task due to the complex interactions between hardware and software components.
This project is designed with the aim of checking and specifying the delay of packets in the network stack while passing through the network. It also has high complexity. This project is focused on packets from the moment an interrupt request (IRQ) is initiated until the packet reaches the application layer, and vice versa.

**1-2- The importance of understanding network delay**
The presence of delay in the network plays an important role in increasing or decreasing the performance and efficiency of any network-based system. This project refers to the delay that occurs when processing a packet of data and transferring it from one point to another in the network.
Due to the following reasons, understanding the network delay is very important:

• Troubleshooting in the network platform:
When network problems arise, understanding network latency can help identify the source of the problem. This can lead to solving problems more quickly and minimizing the amount of failure and reducing the time of truble in the network.
• Network performance optimization:
  By understanding where and how delays occur in the network, engineers can be more dynamic and successful in optimizing the network, which can include creating and making positive changes in network settings, upgrading hardware (such as servers, or optimizing or replacing cables). network) or implementing new protocols.
• Quality of service in the network:
For many applications, software and network services, especially real-time services such as video streaming or online games, low latency is critical to establishing a user relationship and maintaining quality of service at the same time. Understanding network latency can help maintain quality of service for This category of programs can help.
• Planning for network capacity management:
Also, a proper understanding of network delay can help to plan the capacities available in the network. This can provide insights into how the network performs with increased load, or help make informed decisions about timing and network scaling.

**3-1- eBPF performance in network monitoring**
eBPF has led to a new generation of tools that allow developers to easily diagnose problems, innovate quickly, and extend operating system functionality. eBPF (Enhanced Berkeley Packet Filter) is a powerful tool that plays an essential role in network monitoring and helps in network optimization.
Some of the reasons to use eBPF are as follows:
• Flexibility: eBPF programs run in the kernel section, but are defined and controlled through user space. This means they can be loaded and unloaded dynamically (in real-time) without requiring kernel changes or system reboots.
• Accurate performance: eBPF can measure the latency of different segments in the network stack. This helps identify bottlenecks and optimize network performance.
• Efficiency: eBPF is designed to run with minimal overhead, making it suitable for production environments where performance is critical.
• Security: eBPF can monitor system calls and network activity in real-time, making it a valuable tool for detecting and preventing security threats.
• Fine-grained monitoring: eBPF allows fine-grained monitoring of network traffic. It can trace packets, connections, and even kernel-level events, providing detailed insight into network behavior.

**2- Python code description:**
This Python script uses BPF (Berkeley Packet Filter) to track the delay of packets in the network stack as they pass through different network layers in the Linux kernel. It uses BCC (BPF Compiler Collection) library to work with BPF programs in Python.
The parts of Python code separately are as follows:
**1-2- import BPF through the bcc library:**

    from bcc import BPF

**2-2- The BPF program is according to the following code:**

    #Define the BPF program
    bpf_code = """
    #include <linux/skbuff.h>
    int kprobe__eth_type_trans(struct pt_regs *ctx, struct sk_buff *skb) {
    u64 ts = bpf_ktime_get_ns();
    bpf_trace_printk("Layer: 2, Timestamp: %llu, skb: %p\\n", ts, skb);
    return 0;
    }
The BPF program contains the headers necessary to run in the kernel and define a data structure, and also defines a BPF map (start) to store the timestump of received packets. In the `struct pt_regs` structure, it is to create registers and prerequisites required in BPF. In the `struct sk_buff` structure, which is the main structure of the network that shows a packet, it uses a metadata structure that the packet does not hold any data and all the data is stored in the related buffers. . In order to define kprobe in the grid, the first argument is always `struct pt_regs` and `struct sk_buff`, the rest are function arguments.
**2-3- Definition of kprobe functions:**
In order to use kprobe functions to extract timestump in different layers of the network, each kprobe function must be defined first, which is as follows.
• `kprobe__eth_type_trans`Function :
First, by means of BPF and Kprobe, the starting point and entry to the `eth_type_trans` function is tracked, and then it displays its delay from the existing interface to layer number 2 of the data link layer.
• `kprobe_ip_rcv` Function :
In this function and after passing the above function, the program tracks the entry point of the `ip_rcv` function and prints its delay from the data link layer of layer number 2 (data link) to the network layer of layer number 3 (network).
• `kprobe__tcp_v4_rcv`Function :
In the third step, in order to obtain the time stump when passing from layer 3 to 4 (network layer to transport layer), it first tracks the entry point of the `kprobe__tcp_v4_rcv` function and then the delay caused by the movement and transfer from the network layer to the transport layer (transport) is printed.
• `kprobe__tcp_data_queue`Function :
In the final step of sending a packet in the network stack from the lower layers to the higher layers (transport layer to application layer) in the network layer, it first tracks the entry point of the tcp_data_queue function and the delay from the transport layer to the application layer prints .

    // Network Layer (IPv4)
    int kprobe__ip_rcv(struct pt_regs *ctx, struct sk_buff *skb) {
    u64 ts = bpf_ktime_get_ns();
    bpf_trace_printk("Layer: 3, Timestamp: %llu, skb: %p\\n", ts, skb);
    return 0;
    }
    // Transport Layer (TCP over IPv4)
    int kprobe__tcp_v4_rcv(struct pt_regs *ctx, struct sk_buff *skb) {
    u64 ts = bpf_ktime_get_ns();
    bpf_trace_printk("Layer: 4, Timestamp: %llu, skb: %p\\n", ts, skb);
    return 0;
    }
    // Application Layer
    int kprobe__tcp_data_queue(struct pt_regs *ctx, struct sk_buff *skb) {
    u64 ts = bpf_ktime_get_ns();
    bpf_trace_printk("Layer: 5, Timestamp: %llu, skb: %p\\n", ts, skb);
    return 0;
    }
    """
**4- Loading and running the BPF program:**

    bpf = BPF(text=bpf_code)

**5- Created kprobes:**
The functions defined by kprobe cause communication between special events in the kernel, which is as follows:
<![endif]-->

    bpf.attach_kprobe(event="eth_type_trans", fn_name="kprobe__eth_type_trans")
    bpf.attach_kprobe(event="ip_rcv", fn_name="kprobe__ip_rcv")
    bpf.attach_kprobe(event="tcp_v4_rcv", fn_name="kprobe__tcp_v4_rcv")
    bpf.attach_kprobe(event="tcp_data_queue", fn_name="kprobe__tcp_data_queue")
**6- Printing and extracting the output from Network Trace:**
This program and script with the help of eBPF and Python language first starts the trace in the network stack and prints the output and displays the delays in different layers of the network.
The script records timestump when packets pass through different layers of the network stack and calculates and prints the delays at each step based on ns (nano second). The output contains the packet ID and corresponding delay for each tracked event.
According to the output file and the description of the above code, this program allows us to record the time stump in all layers 2, 3 and 4 and keep it separately for each layer in order to check the occurrence of problems or delays in the network stack. .

# II. Installation of project requirements and prerequisites
In order to implement this project, we need to comply with some software requirements and install some required software and features on the Linux platform, whose commands are as follows:
**1-BPF installation:**
We install BPF in order to track points in the network bed with the following commands:

    sudo apt install bpftrace
    bpftrace -l 'tracepoint:tcp:*'
**2-Installing Netstat and Nstate:**
In order to install Netstat and Nstate to check network connections, the following codes should be used:

    sudo apt install net-tools
    sudo apt-get install ethtool

**3-Install the BCC command:**
To install tools for IP tracing in Ubuntu using BCC (BPF Compiler Collection), follow these steps:

I.  **Prerequisites:** Ensure your Ubuntu system meets the following requirements:
    
-   **Linux kernel version 4.1 or higher:** Check your kernel version using `uname -r`. If it's lower than 4.1, you'll need to upgrade your kernel.
-   **Root privileges:** Some BCC tools require root privileges to run.

II.  **Install BCC Packages:** Use the `apt` package manager to install BCC tools from the Ubuntu Universe repository. Open a terminal and run the following command:
    
```
sudo apt install bpfcc-tools
```

This will install the BCC tools, including `tcpconnect-bpfcc`, `tcpstates-bpfcc`, and `tcptop-bpfcc`, which are useful for IP tracing.

III.  **Verify Installation:** To verify that the BCC tools are installed correctly, run any of the installed tools, such as `tcpconnect-bpfcc`:

    sudo tcpconnect-bpfcc

This will print a summary of TCP connections being made on your system.

**4-Install the nicstat command:**
nicstat is a Solaris and Linux command line that prints network statistics for all network interface cards (NICs), including packets, data transfer rate (kilobytes per second), and average packet size, installed with the following command:

    sudo apt install nicstat
    nicstat 1
    ethtool -S ens33

**5-Installing the Socketstat command:**
The socketstat command lists open sockets on the Internet or a Unix domain. The following options are available:
-4 Show only IPv4 sockets.
-6 Show only IPv6 sockets.
-u Show Unix sockets as well.
which is installed by the following command:

    sudo apt-get install -y socketstat

## III.Display the calculated TIMESTAMP time
The provided script performs the following:

1.  Runs the `timestamp.py` script with a timeout of 20 seconds.** This script likely generates a file containing timestamps and other data.
    
2.  Processes the output of the `timestamp.py` script using `awk`.** It filters the output to only include lines that contain the text `bpf_trace_printk`. It then removes the single quotes from the last element of the line (which is likely a log message) and prints the PID, TID, timestamp, and log message.
    
3.  Sorts the output of the `awk` processing using `sort`.** It sorts the output by timestamp, with timestamps in the second column (which was extracted in the `awk` processing) sorted in descending order.
    
4.  **Removes duplicate lines using `awk`.** It uses a hash table to keep track of seen pairs of PID and TID, and only prints lines for which the PID and TID are not already in the hash table.
    
5.  **Sorts the output of the `awk` processing using `sort` again.** It sorts the output by timestamp (in the third column) and then by PID in ascending order.
    
6.  **Writes the processed output to a file named `log.txt`.**
    
7.  **Runs the `delta.py` script.** This script likely processes the data in the `log.txt` file further.
    

Here is a breakdown of the individual commands:

-   `sudo timeout 20s python3 timestamp.py > output.txt`: This command runs the `timestamp.py` script with a timeout of 20 seconds. If the script takes longer than 20 seconds to run, it will be terminated and an error message will be printed.
    
-   `awk -F'[:,]' '/bpf_trace_printk/ { gsub(/'\''$/, "", $8); print " " $4 " " $6 " " $8 }' output.txt`: This `awk` command filters the output of the `timestamp.py` script to only include lines that contain the text `bpf_trace_printk`. It then removes the single quotes from the last element of the line (which is likely a log message) and prints the PID, TID, timestamp, and log message.
    
-   `sort -k 2n | awk '!seen[$1, $3]++' | sort -k3 -k2n > log.txt`: This command sorts the output of the `awk` processing and removes duplicate lines. It sorts the output by timestamp in the second column (which was extracted in the `awk` processing) in descending order. Then, it uses a hash table to keep track of seen pairs of PID and TID, and only prints lines for which the PID and TID are not already in the hash table. Finally, it sorts the output by timestamp (in the third column) and then by PID in ascending order.

# IV.

this code processes a log file line by line, extracts relevant information, and calculates the time difference for specific conditions. The results are then stored in individual files in the 'delta' directory, and averages of the values in these files are calculated and appended to the respective files. This process seems to be a part of the overall project to characterize network stack latency using eBPF.

1. **Setting up Paths and Directories:**

> Log_path = 'log.txt'
>     delta_dir = 'delta'

These variables define the paths for the log file (`log.txt`) and a directory (`delta`) where the output files will be stored.

if not os.path.exists(`delta_dir`):

    os.mkdir(delta_dir)

This block checks if the 'delta' directory exists. If not, it creates the directory. This directory is used to store output files later.

2. **Functions for Calculating Average and File Operations:**

·  `calculate_average(filepath)`: Reads a CSV file specified by `filepath` and calculates the average of the values in the first column.

·  `write_average(filepath, average)`: Appends the calculated average to a CSV file specified by `filepath`.

·  `read_file_line_by_line(file_path)`: A generator function that yields lines from a file specified by `file_path` one by one.

3. **Processing Log File:**

>     lines = read_file_line_by_line(log_path)
>     first_line = next(lines)
>     layer, timestamp, skb_buff = first_line.split()

This part reads the log file line by line and splits the first line into `layer`, `timestamp`, and `skb_buff`.

for line in lines:

    next_layer, next_timestamp, next_skb_buff = line.split()
    if next_skb_buff == skb_buff:
    if next_layer > layer:
    #Write delta values to a file
    with open(f"{delta_dir}/{layer}-{next_layer}.csv", "a") as target_file:
    target_file.write(f"{int(next_timestamp) - int(timestamp)}, {skb_buff}\n")
    layer, timestamp, skb_buff = next_layer, next_timestamp, next_skb_buff

It iterates through the remaining lines, comparing `skb_buff` values. If the `skb_buff` values are equal, and the `next_layer` is greater than the current `layer`, it writes the time difference and `skb_buff` to a file in the 'delta' directory.

4. **Calculating and Writing Averages:**

   

>  for filename in os.listdir(delta_dir):
>     filepath = os.path.join(delta_dir, filename)
>     average = calculate_average(filepath)
>     write_average(filepath, average)

After processing all the files in the 'delta' directory, it calculates the average of the first column for each file and appends the average to the same file.









