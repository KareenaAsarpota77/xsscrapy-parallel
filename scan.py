import subprocess
import time
from urllib.parse import urlparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

input_file = "targets.txt"

with open(input_file, "r") as f:
    targets = [line.strip() for line in f if line.strip()]

output_dir = "scan_results"
os.makedirs(output_dir, exist_ok=True)

xsscrapy_dir = "xsscrapy"

# Number of parallel scans (tune this!)
MAX_WORKERS = 5

def scan_url(url, timeout):
    parsed = urlparse(url)
    site_name = parsed.netloc.replace(":", "_")
    path_name = parsed.path.strip("/").replace("/", "_")

    file_name = f"{site_name}_{path_name}.txt" if path_name else f"{site_name}.txt"
    output_file = os.path.join(output_dir, file_name)

    try:
        result = subprocess.run(
            ["python", "xsscrapy.py", "-u", url],
            cwd=xsscrapy_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        with open(output_file, "w") as f:
            f.write(result.stdout if result.stdout else "No output captured.")

        return f"Done: {url}"

    except subprocess.TimeoutExpired as e:
        with open(output_file, "w") as f:
            f.write(e.stdout if e.stdout else "Timeout - no output.")
        return f"Timeout: {url}"


# Total runtime limit
total_runtime = 5 * 60
start_time = time.time()

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = []

    for url in targets:
        remaining = total_runtime - (time.time() - start_time)
        if remaining <= 0:
            break

        futures.append(executor.submit(scan_url, url, remaining))

    for future in as_completed(futures):
        print(future.result())

print("Scanning completed.")
