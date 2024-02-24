# GCS Storage Class File Counter

This Python script automates the process of counting files stored in Google Cloud Storage (GCS) buckets, categorized by their storage class (e.g., STANDARD, NEARLINE, COLDLINE, ARCHIVE). It's designed to help GCS users efficiently manage and analyze their storage utilization across different storage classes, facilitating cost optimization and data organization strategies. By accepting project ID and bucket name as command-line arguments, the script offers flexibility and ease of use, making it suitable for both ad-hoc analyses and integration into larger cloud management workflows.

## Features
- **Automated File Counting**: Quickly counts files in specified GCS buckets, broken down by storage class.
- **Flexible Usage**: Accepts Google Cloud project ID and bucket name as command-line arguments for easy customization.
- **Cost Management Aid**: Helps in identifying storage distribution across classes, aiding in cost optimization efforts.

## How to Use
1. Ensure you have Python 3.6+ and the `google-cloud-storage` library installed.
2. Set up authentication by configuring your environment with Google Cloud credentials.
3. Run the script from the command line, specifying your project ID and bucket name:
   ```bash
   python count_storage_classes.py <your-project-id> <your-bucket-name>

The script will print counts directly to the standard output (stdout). For example, it may look like this:
```
STANDARD: 1500
NEARLINE: 100
COLDLINE: 50
ARCHIVE: 25
```
If you need to save it to a file instead of just viewing it in the terminal, you can redirect the output to a file when you run it:
```bash
python count_storage_classes.py <your-project-id> <your-bucket-name> > output.txt
```
Thanks to ChatGPT 4 for assisting with the setup of this repository.
