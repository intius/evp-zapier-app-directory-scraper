import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
    throw new Error('Set APIFY_TOKEN before running this example.');
}

const client = new ApifyClient({ token });
const runInput = {
    "category": "sales-crm",
    "maxItems": 10
};
const run = await client.actor('evpp/zapier-app-directory').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items.slice(0, 5), null, 2));
console.log(`Fetched ${items.length} items. Open the full dataset: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
