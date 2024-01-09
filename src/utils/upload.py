import random
import time

import http.client
import httplib2

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build


httplib2.RETRIES = 1

MAX_RETRIES = 10

RETRIABLE_EXCEPTIONS = (
    httplib2.HttpLib2Error,
    IOError,
    http.client.NotConnected,
    http.client.IncompleteRead,
    http.client.ImproperConnectionState,
    http.client.CannotSendRequest,
    http.client.CannotSendHeader,
    http.client.ResponseNotReady,
    http.client.BadStatusLine,
)


RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


CLIENT_SECRETS_FILE = input("Enter your client credential secret file path:\n")
MEDIA_FILE_PATH = input("Enter the path of the video you wish to upload:\n")

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def initialize_upload(youtube: build, options) -> None:
    """initialize the upload request"""
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category,
        ),
        status=dict(privacyStatus=options.privacyStatus),
    )

    insert_request = youtube.videos().insert(
        part=",".join(list(body.keys())),
        body=body,
        media_body=MediaFileUpload(MEDIA_FILE_PATH, chunksize=-1, resumable=True),
    )

    resumable_upload(insert_request)


def resumable_upload(request):
    """A Resumable error to retry the upload"""
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print("Uploading file...")
            _, response = request.next_chunk()
            if response is not None:
                if "id" in response:
                    print(f'Video id {response["id"]} was successfully uploaded.')
                else:
                    exit(f"The upload failed with an unexpected response: {response}")
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = "A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"

        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                exit("No longer attempting to retry.")

            max_sleep = 2**retry
            sleep_seconds = random.random() * max_sleep
            print(f"Sleeping {sleep_seconds} seconds and then retrying...")
            time.sleep(sleep_seconds)


class UplooadController:
    """Upload Controller"""


    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
    RETRIABLE_EXCEPTIONS = (
    httplib2.HttpLib2Error,
    IOError,
    http.client.NotConnected,
    http.client.IncompleteRead,
    http.client.ImproperConnectionState,
    http.client.CannotSendRequest,
    http.client.CannotSendHeader,
    http.client.ResponseNotReady,
    http.client.BadStatusLine
    )

    def __init__(self, *args, **kwargs):
        pass
