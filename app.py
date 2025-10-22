import os, json, argparse

def list_files(root: str):
    for entry in os.scandir(root):
        if entry.is_file():
            yield entry.name, entry.stat().st_size

def main():
    parser = argparse.ArgumentParser(description="Read files from a directory and summarize.")
    parser.add_argument("--dir", default=os.environ.get("DATA_DIR", "/app/data"),
                        help="Directory to read inside the container (default: /app/data or $DATA_DIR).")
    args = parser.parse_args()
    data_dir = args.dir

    if not os.path.isdir(data_dir):
        print(f"ERROR: directory not found: {data_dir}")
        exit(2)

    total_bytes = 0
    total_files = 0

    for name, size in list_files(data_dir):
        print(f"{name}\t{size} bytes")
        total_files += 1
        total_bytes += size

    summary = {"dir": data_dir, "files": total_files, "bytes": total_bytes}
    print(json.dumps(summary, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()