from playwright.sync_api import Page


def test_file_downloader(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="ProfileImage_01.jpg").click()
    download = download_info.value

    print(download.path())
