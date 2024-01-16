
#!/usr/bin/bash


sudo timeout 20s python3 timestamp.py > output.txt
awk -F'[:,]' '/bpf_trace_printk/ { gsub(/'\''$/, "", $8); print " " $4  " " $6 " " $8 }' output.txt |  sort -k 2n  | awk '!seen[$1, $3]++' | sort -k3 -k2n > log.txt
python3 delta.py


