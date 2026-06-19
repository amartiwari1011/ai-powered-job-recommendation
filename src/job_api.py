from dotenv import load_dotenv
import os
from apify_client import ApifyClient

load_dotenv()
apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

#fetch linkdin jobs based on search quesry and location
def fetch_linkdin_jobs(search_query, location= "india", rows=60):

    # Prepare the Actor input
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy" : True,
            "apifyProxyGroups" : ["RESIDENTIAL"]
        }
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

#fetch naukari jobs based on search quesry and location
def fetch_naukari_jobs(search_query, location= "india", rows=60):
    # Prepare the Actor input
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs