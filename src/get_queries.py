import aiohttp
import asyncio
import os
from tqdm import tqdm


async def fetch_queries(api_key, query_ids):
    headers = {"Authorization": f"Key {api_key}"}
    async with aiohttp.ClientSession() as session:
        results = {}
        for query_id in tqdm(query_ids):
            url = f"https://redash.lightricks.com/api/queries/{query_id}"
            async with session.get(url, headers=headers) as response:
                results[query_id] = await response.json()
        return results


def async_fetch(api_key, query_ids):
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(fetch_queries(api_key, query_ids))
    return responses


def filter_by_user(responses, emails_list):
    filtered_responses = {key: value for key, value in responses.items()
                          if value.get('user', {}).get('email') in emails_list}
    return filtered_responses


def filter_by_name(responses, exclusions):
    filtered_responses = {key: value for key, value in responses.items()
                          if not any(substring in value.get('name', '') for substring in exclusions)}
    return filtered_responses


def save_queries(queries):
    template = u"""/*
    Name: {name}
    Query ID: {query_id}
    Created By: {created_by}
    Last Updated At: {last_updated_at}
    */
    {query}"""

    for query in queries:
        query = queries[query]
        if all(key in query for key in ["id", "name", "data_source_id", "user", "updated_at", "query"]):
            filename = "queries/query_{}.txt".format(str(query["id"]))
            with open(filename, "w") as f:
                content = template.format(
                    name=query["name"],
                    query_id=query["id"],
                    created_by=query["user"]["name"],
                    last_updated_at=query["updated_at"],
                    query=query["query"],
                )
                f.write(content)
        else:
            print("Invalid query format:", query)


# redash_api_key = 'api_key_here'
query_ids = [str(i) for i in range(40000, 42527)]
responses = async_fetch(os.environ.get("REDASH_API_KEY"), query_ids)

lisf_of_emails = ['rhacohen@lightricks.com',
                  'nicky@lightricks.com',
                  'jseidman@lightricks.com',
                  'shiri@lightricks.com',
                  'mitesh@lightricks.com',
                  'jrouncefield@lightricks.com',
                  'fambrose@lightricks.com',
                  'ohochner@lightricks.com']

pd_responses = filter_by_user(responses, lisf_of_emails)
filtered_responses = filter_by_name(pd_responses, ['New Query', 'Copy of'])

save_queries(filtered_responses)
