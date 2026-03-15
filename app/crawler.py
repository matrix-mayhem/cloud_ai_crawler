import requests
from bs4 import BeautifulSoup
import boto3
import uuid

s3 = boto3.client("s3")

BUCKET = "data-platform-bucket-1"


def crawl_page(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = [p.text for p in soup.find_all("p")]

    text = " ".join(paragraphs)

    filename = f"crawl-{uuid.uuid4()}.txt"

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=text
    )

    return text