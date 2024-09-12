import os

import requests
from dotenv import load_dotenv

from libs.github.application import GithubAPI
from libs.mkdown.parser import MarkDownParser
from libs.tistory.tistory import TistoryUploader

load_dotenv()

gh = GithubAPI(
    user=os.environ['GH_ID'],
    repo_name=os.environ['GH_REPO']
)

sha = gh.repository.get_latest_sha_on_commit()
addition_files = gh.repository.get_added_file_by_latest_commits(sha)

if len(addition_files) <= 1:
    read_url = addition_files[0]["raw_url"]

    if read_url:
        r = requests.get(read_url)

        markdown_parser = MarkDownParser(r.text)

        TistoryUploader(
            tsession=os.environ["TSESSION"],
            domain=os.environ["TISTORY_BLOG_DOMAIN"],
        ).execute(
            title=markdown_parser.get_markdown_title(),
            content=markdown_parser.get_markdown_to_html
        )
