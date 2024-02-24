import argparse
from google.cloud import storage

def count_files_by_storage_class(bucket_name, project_id):
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()

    storage_class_count = {}

    for blob in blobs:
        storage_class = blob.storage_class
        if storage_class in storage_class_count:
            storage_class_count[storage_class] += 1
        else:
            storage_class_count[storage_class] = 1

    return storage_class_count

def main():
    parser = argparse.ArgumentParser(description='Count files in a Google Cloud Storage bucket by storage class.')
    parser.add_argument('project_id', type=str, help='Google Cloud project ID.')
    parser.add_argument('bucket_name', type=str, help='Name of the Google Cloud Storage bucket.')

    args = parser.parse_args()

    counts = count_files_by_storage_class(args.bucket_name, args.project_id)
    for storage_class, count in counts.items():
        print(f"{storage_class}: {count}")

if __name__ == '__main__':
    main()
