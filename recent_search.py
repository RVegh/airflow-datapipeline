import json
import os
from webbrowser import get
import requests

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url():
    query = "AluraOnline"
    tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,text"
    user_fields = "expansions=author_id&user.fields=id,name,username,created_at"
    filters = "start_time=2022-03-03T00:00:00.00Z&end_time=2022-03-08T00:00:00.00Z"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&{}".format(
        query, tweet_fields,user_fields,filters

    )
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def paginate(url, headers, next_token=""):
    if next_token:
        full_url == f"{url}&next_token={next_token}"
    else:
        full_url = url
    data = connect_to_endpoint(url, headers)
    yield data
    if "next_token" in data.get("meta", {}):
        yield from paginate(url, headers, data["meta"]["next_token"])




def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()



