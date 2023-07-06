import csv

def csv_writer(data: list) -> None:
    with open('comments.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Content'])
        for comment in data:
            try:
                writer.writerow([comment])
            except UnicodeEncodeError:
                pass
