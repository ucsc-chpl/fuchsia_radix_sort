import subprocess
import re

# just running ./build/benchmark will give you this information
vendor_id = "10DE"
device_id = "2786"
target_name = "nvidia_sm35_u32"
sort_type = "direct"
current_count = 131072
end_count = 8388608
step_count = 131072
iterations = 8#128
warmup = 8#8

command = [
        "./build/benchmark",
        f"{vendor_id}:{device_id}",
        target_name,
        sort_type,
        str(current_count),
        str(end_count),
        str(step_count),
        str(iterations),
        str(warmup),
        "1",  # Verify sorted results
        "0"   # Disable validation layers
]

try:
    result = subprocess.run(command, capture_output=True, text=True) 
    with open("results.txt", "w") as f:
        f.write(f"{result.stdout}\n")

except Exception as e:
        print(f"Error executing benchmark from {current_count} to {end_count} keyvals: {e}")