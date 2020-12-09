import os
import re
import json


protocol = "https?"
internet_archive_domains = [
    "web.archive.org",
    "www.archive.org",
    "archive.org",
    "replay.web.archive.org",
    "wayback.archive.org",
    "wayback.archive-it.org",
]
archive_today_domains = [
    "archive.today",
    "archive.is",
]


re_internet_archive = re.compile("(" + protocol + ")" + "://" + "(" + "|".join(internet_archive_domains) + ")")
re_archive_today = re.compile("(" + protocol + ")" + "://" + "(" + "|".join(archive_today_domains) + ")")


data_path = "local_data"
file_name = "es-references.ljson"


file_path = os.path.join(data_path, file_name)
matched_internet_archive = []
matched_archive_today = []
others = []
with open(file_path, "r") as fp:
    for line in fp:
        record = json.loads(line)
        is_matched = False

        match = re.match(re_archive_today, record["url"])
        if match:
            matched_archive_today.append(record)
            is_matched = True

        match = re.match(re_internet_archive, record["url"])
        if match:
            matched_internet_archive.append(record)
            is_matched = True

        if not is_matched:
            others.append(record)


for record in others:
    if "archive" in record["url"]:
        print(record["url"])

for record in others:
    if "wayback" in record["url"]:
        print(record["url"])
