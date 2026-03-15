import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("crawler-results")


def summarize_text(text, url):

    summary = text[:200]

    table.put_item(
        Item={
            "url": url,
            "summary": summary
        }
    )

    return summary