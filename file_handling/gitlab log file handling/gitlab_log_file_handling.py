import pandas as pd
import re

log_file_path = "gitlab_access.log"
failed_connections = []

pattern = re.compile(r'HTTP/\d\.\d"\s(4\d{2}|5\d{2})\b')

with open(log_file_path, 'rt') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            failed_connections.append(line.strip())

df = pd.DataFrame(failed_connections, columns=['Log Entry'])

print(df)

df.to_csv("failed_connections.csv", index=False)


