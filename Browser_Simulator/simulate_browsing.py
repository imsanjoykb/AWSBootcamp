import requests, json, random, time

def simulate_browsing():
    print("SIMULATION INITIATED")
    print("Accessing configuration")
    with open('config.json') as config_file:
        data = json.load(config_file)
        cloudfront_domain = data['cloudfront_domain']
        s3_bucket = data['s3_bucket']
        images = data['images']
        request_count = data['request_count']
        distribution = data['distribution']
        delay = data['delay']
        distribute_requests(request_count, distribution, delay, cloudfront_domain, s3_bucket, images)


def distribute_requests(request_count, distribution, delay, cloudfront_domain, s3_bucket, images):
    total_cf = 0
    total_s3 = 0
    index = 0
    while index < request_count:
        print("REQUEST {}".format(index+1))
        r = random.random()
        time.sleep(delay)
        for image in images:
            if r <= distribution:
                total_s3 = total_s3 + page_request("https://{}.s3.amazonaws.com/{}".format(s3_bucket, image))
            else:
                total_cf = total_cf + page_request("https://{}/{}".format(cloudfront_domain, image))
        index += 1
    print("RESULTS: Total CF: {} Kb, Total S3: {} Kb".format(total_cf/1024, total_s3/1024))


def page_request(url):
    print('Request: {}'.format(url))
    results = requests.get(url)
    result_size = 0
    if results.status_code == 200:
        result_size = len(results.content)
    print("Response: {}, Size: {} Kb".format(results.status_code, result_size/1024))
    return result_size


if __name__ == "__main__":
    simulate_browsing()
