from src.main import get_gists_for_user
from aioresponses import aioresponses
import pytest

@pytest.mark.asyncio
async def test_fetch_gists():

    user = "octocat"
    url = f"https://api.github.com/users/{user}/gists"
    expected_response = [{"url": url}]
    expected_status = 200

    # Mock the HTTP GET request
    with aioresponses() as mock:
        mock.get(url, payload=expected_response)

        status, response = await get_gists_for_user(user)

        # Validate the response
        assert response == expected_response
        assert status == expected_status
