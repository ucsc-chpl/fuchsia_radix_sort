import subprocess
import re

vendor_id = "10DE"
device_id = "2786"
target_name = "nvidia_sm35_u64"
sort_type = "direct"
current_count = 131072
end_count = 8388608
step_count = 1
iterations = 1
warmup = 1

max_mkeys_pattern = re.compile(r"([\d.]+)\s*$")
results = []

while current_count <= end_count:
    command = [
        "./build/benchmark",
        f"{vendor_id}:{device_id}",
        target_name,
        sort_type,
        str(current_count),
        str(current_count),
        str(step_count),
        str(iterations),
        str(warmup),
        "1",  # Verify sorted results
        "0"   # Disable validation layers
    ]

    # Execute the benchmark
    print(f"Running benchmark with {current_count} keyvals...")
    try:
        result = subprocess.run(command, capture_output=True, text=True)

        # Find the Max Mkeys/s value in the output
        max_mkeys_match = max_mkeys_pattern.search(result.stdout)
        if max_mkeys_match:
            max_mkeys_value = float(max_mkeys_match.group(1))
            results.append((current_count, max_mkeys_value))
            print(f"Keyvals: {current_count}, Max Mkeys/s: {max_mkeys_value}")
        else:
            print(f"Could not find Max Mkeys/s value for {current_count} keyvals.")

    except Exception as e:
        print(f"Error executing benchmark at {current_count} keyvals: {e}")
        break
    current_count += 131072

with open("results.txt", "w") as f:
    for count, mkeys in results:
        f.write(f"({count}, {mkeys})\n")