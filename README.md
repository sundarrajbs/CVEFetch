
# CVE Retrieve and IOC Extractor

This tool automatically retrieves the latest Common Vulnerabilities and Exposures (CVEs) from the National Vulnerability Database (NVD) for the past 24 hours, extracts relevant Indicators of Compromise (IOCs) such as IP addresses, URLs, and file hashes from each CVE’s description, and exports the data to an Excel spreadsheet.

## Features

- Fetches CVEs published in the last 24 hours using the [nvdlib](https://pypi.org/project/nvdlib/) library.
- Extracts IOCs (IPs, URLs, hashes) from CVE descriptions with [iocextract](https://github.com/InQuest/iocextract).
- Exports results to an Excel file for easy analysis and reporting.


## Requirements

- Python 3.7+
- pip


### Python Libraries

Install required libraries with:

```bash
pip install nvdlib pandas openpyxl iocextract
```


## Usage

1. **Clone this repository:**

```bash
git clone https://github.com/sundarrajbs/CVEFetch.git
cd CVEFetch
```

2. **Run the script:**

```bash
python CVERetrieve.py
```

The script will fetch CVEs from the last 24 hours and write a file named `latest_cves_last_24hrs.xlsx`.

## Script Overview

- Calculates current UTC time and 24 hours before.
- Fetches CVE data with publication dates within the last 24 hours.
- Extracts IOCs from each CVE’s description field.
- Outputs structured data to an Excel spreadsheet.

Example of script logic:

```python
from datetime import datetime, timedelta, timezone
import nvdlib, pandas as pd, iocextract

now = datetime.now(timezone.utc)
one_day_ago = now - timedelta(days=1)
pubStartDate = one_day_ago.strftime("%Y-%m-%dT%H:%M:%S:000Z")
pubEndDate = now.strftime("%Y-%m-%dT%H:%M:%S:000Z")
results = nvdlib.searchCVE(pubStartDate=pubStartDate, pubEndDate=pubEndDate)

data = []
for cve in results:
    # extract IOCs etc...
    pass
# Write to Excel as in CVERetrieve.py
```


## Output

- **latest_cves_last_24hrs.xlsx**
Contains columns:
    - CVE ID
    - Description
    - IOCs (comma-separated, if found)


## Troubleshooting

- Ensure all dependencies are installed (see above).
- For errors related to date formats or imports, review the import statements as shown in the script.
- The script uses UTC for all timestamps to be consistent with the NVD API.