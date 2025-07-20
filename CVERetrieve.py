import datetime
import nvdlib
import pandas as pd
import iocextract

from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)
one_day_ago = now - timedelta(days=1)

# Calculate time range for past 24 hours in correct ISO 8601 format
#now = datetime.now(datetime.timezone.utc)
#one_day_ago = now - datetime.timedelta(days=1)
pubStartDate = one_day_ago.strftime("%Y-%m-%d %H:%M")
pubEndDate = now.strftime("%Y-%m-%d %H:%M")
print(f"Fetching CVEs published from {pubStartDate} to {pubEndDate}")
results = nvdlib.searchCVE(pubStartDate=pubStartDate, pubEndDate=pubEndDate)


data = []
for cve in results:
    cve_id = cve.id
    description = cve.descriptions[0].value if cve.descriptions else ""
    # Extract IOCs from description
    iocs = set()
    iocs.update(iocextract.extract_ips(description))
    iocs.update(iocextract.extract_urls(description))
    iocs.update(iocextract.extract_hashes(description))
    ioc_str = ', '.join(iocs) if iocs else 'None'
    data.append({'CVE ID': cve_id, 'Description': description, 'IOCs': ioc_str, 'Raw': cve})

# Create DataFrame
df = pd.DataFrame(data)

# Write to Excel
df.to_excel('latest_cves_with_iocs.xlsx', index=False)
print("Excel file 'latest_cves_with_iocs.xlsx' created successfully.")
