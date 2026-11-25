import json
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
if not APIFY_TOKEN:
    raise SystemExit("Set APIFY_TOKEN before running this example.")

client = ApifyClient(APIFY_TOKEN)
run_input = json.loads('''{"category":"sales-crm","maxItems":10}''')
run = client.actor("evpp/zapier-app-directory").call(run_input=run_input)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(json.dumps(items[:5], indent=2, ensure_ascii=False))
print(f"Fetched {len(items)} items. Open the full dataset: https://console.apify.com/storage/datasets/{run['defaultDatasetId']}")
