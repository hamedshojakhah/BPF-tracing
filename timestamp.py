from bcc import BPF


# Define the BPF program
bpf_code = """
#include <linux/skbuff.h>

int kprobe__eth_type_trans(struct pt_regs *ctx, struct sk_buff *skb) {
   u64 ts = bpf_ktime_get_ns();
   bpf_trace_printk("Layer: 2, Timestamp: %llu, skb: %p\\n", ts, skb);
   return 0;
}

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


# Load the BPF program
bpf = BPF(text=bpf_code)


# Attach kprobes
bpf.attach_kprobe(event="eth_type_trans", fn_name="kprobe__eth_type_trans")
bpf.attach_kprobe(event="ip_rcv", fn_name="kprobe__ip_rcv")
bpf.attach_kprobe(event="tcp_v4_rcv", fn_name="kprobe__tcp_v4_rcv")
bpf.attach_kprobe(event="tcp_data_queue", fn_name="kprobe__tcp_data_queue")

# Print trace output
print("Tracing packet delay using packet ID... Hit Ctrl-C to end.")
bpf.trace_print()
