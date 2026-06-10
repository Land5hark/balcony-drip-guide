#!/usr/bin/env python3
"""Tests for the title-aware promotion URL preflight."""

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "verify-promotion-live-urls.py"
SPEC = importlib.util.spec_from_file_location("verify_promotion_live_urls", SCRIPT)
VERIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFIER)


class VerifyPromotionLiveUrlsTest(unittest.TestCase):
    def test_parse_title_normalizes_entities_and_whitespace(self):
        body = "<html><title>  The Drip &mdash; Weekly\n Newsletter </title></html>"
        self.assertEqual(VERIFIER.parse_title(body), "The Drip — Weekly Newsletter")

    def test_canonical_url_strips_utm_and_adds_trailing_slash(self):
        url = (
            "https://balcony-drip-guide.pages.dev/posts/example"
            "?utm_source=twitter&utm_medium=social"
        )
        self.assertEqual(
            VERIFIER.canonical_url(url),
            "https://balcony-drip-guide.pages.dev/posts/example/",
        )

    def test_canonical_url_rejects_placeholder_and_foreign_host(self):
        self.assertIsNone(
            VERIFIER.canonical_url("https://balcony-drip-guide.pages.dev/posts/...")
        )
        self.assertIsNone(VERIFIER.canonical_url("https://example.com/posts/example/"))

    def test_collect_urls_deduplicates_utm_variants(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            asset_dir = Path(temp_dir)
            (asset_dir / "pack.md").write_text(
                "\n".join(
                    [
                        "https://balcony-drip-guide.pages.dev/posts/example/",
                        "https://balcony-drip-guide.pages.dev/posts/example/?utm_source=x",
                        "https://balcony-drip-guide.pages.dev/posts/...",
                    ]
                )
            )
            self.assertEqual(
                VERIFIER.collect_urls([asset_dir]),
                ["https://balcony-drip-guide.pages.dev/posts/example/"],
            )

    def test_verify_passes_matching_live_title(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            public_dir, asset_dir = self.make_fixture(Path(temp_dir))
            with patch.object(
                VERIFIER, "fetch_title", return_value=(200, "Example · The Balcony Drip", "")
            ):
                checks = VERIFIER.verify(public_dir, [asset_dir], timeout=1)
            self.assertEqual(checks[0]["status"], "pass")
            self.assertEqual(checks[0]["problems"], [])

    def test_verify_rejects_homepage_fallback_title(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            public_dir, asset_dir = self.make_fixture(Path(temp_dir))
            with patch.object(
                VERIFIER,
                "fetch_title",
                return_value=(200, "The Balcony Drip — Homepage", ""),
            ):
                checks = VERIFIER.verify(public_dir, [asset_dir], timeout=1)
            self.assertEqual(checks[0]["status"], "fail")
            self.assertIn(
                "live title does not match local rendered title", checks[0]["problems"]
            )

    def test_verify_rejects_missing_local_page(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            public_dir = temp_path / "public"
            asset_dir = temp_path / "promotion"
            public_dir.mkdir()
            asset_dir.mkdir()
            (asset_dir / "pack.md").write_text(
                "https://balcony-drip-guide.pages.dev/posts/missing/"
            )
            with patch.object(
                VERIFIER, "fetch_title", return_value=(200, "Missing · The Balcony Drip", "")
            ):
                checks = VERIFIER.verify(public_dir, [asset_dir], timeout=1)
            self.assertEqual(checks[0]["status"], "fail")
            self.assertIn("local rendered page missing", checks[0]["problems"])

    @staticmethod
    def make_fixture(temp_path):
        public_dir = temp_path / "public"
        asset_dir = temp_path / "promotion"
        page_dir = public_dir / "posts" / "example"
        page_dir.mkdir(parents=True)
        asset_dir.mkdir()
        (page_dir / "index.html").write_text(
            "<html><title>Example · The Balcony Drip</title></html>"
        )
        (asset_dir / "pack.md").write_text(
            "https://balcony-drip-guide.pages.dev/posts/example/?utm_source=twitter"
        )
        return public_dir, asset_dir


if __name__ == "__main__":
    unittest.main()
