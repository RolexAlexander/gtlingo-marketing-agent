"""Zero-cost verification of the real Facebook Graph API integration,
mocking the network layer entirely so this can run for free before any
real post is attempted.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from marketing_agent.tools import publish_post


class TestPublishOrStagePost(unittest.TestCase):
    def test_stages_when_no_credentials(self):
        with patch.object(publish_post, "MOCK", False), patch.object(
            publish_post, "META_PAGE_ACCESS_TOKEN", ""
        ), patch.object(publish_post, "META_PAGE_ID", ""):
            result = publish_post.publish_or_stage_post("a caption", "/no/such/file.png")
        self.assertEqual(result["status"], "staged")
        staged = json.loads(Path(result["staged_path"]).read_text())
        self.assertEqual(staged["caption"], "a caption")

    def test_mock_mode_always_stages(self):
        with patch.object(publish_post, "MOCK", True), patch.object(
            publish_post, "META_PAGE_ACCESS_TOKEN", "fake"
        ), patch.object(publish_post, "META_PAGE_ID", "fake"):
            result = publish_post.publish_or_stage_post("caption", "/no/such/file.png")
        self.assertEqual(result["status"], "staged")

    def test_real_publish_hits_correct_graph_api_endpoint(self):
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {"id": "123_456", "post_id": "123_456"}

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp.write(b"fake-image-bytes")
            tmp_path = tmp.name

        with patch.object(publish_post, "MOCK", False), patch.object(
            publish_post, "META_PAGE_ACCESS_TOKEN", "fake-token"
        ), patch.object(publish_post, "META_PAGE_ID", "1234567890"), patch(
            "marketing_agent.tools.publish_post.requests.post", return_value=fake_response
        ) as mock_post:
            result = publish_post.publish_or_stage_post("caption text", tmp_path)

        called_url = mock_post.call_args[0][0]
        self.assertEqual(called_url, "https://graph.facebook.com/v21.0/1234567890/photos")
        kwargs = mock_post.call_args[1]
        self.assertEqual(kwargs["data"]["access_token"], "fake-token")
        self.assertEqual(kwargs["data"]["caption"], "caption text")
        self.assertIn("source", kwargs["files"])
        self.assertEqual(result["status"], "published")

    def test_network_failure_returns_error_not_crash(self):
        with patch.object(publish_post, "MOCK", False), patch.object(
            publish_post, "META_PAGE_ACCESS_TOKEN", "fake"
        ), patch.object(publish_post, "META_PAGE_ID", "fake"), patch(
            "marketing_agent.tools.publish_post.requests.post", side_effect=ConnectionError("boom")
        ):
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                tmp.write(b"x")
                tmp_path = tmp.name
            result = publish_post.publish_or_stage_post("caption", tmp_path)
        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
