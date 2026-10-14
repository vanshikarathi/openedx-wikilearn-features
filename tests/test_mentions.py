"""
Tests for the `wikimedia_general.mentions` module.
"""

import pytest

from openedx_wikilearn_features.wikimedia_general.mentions import extract_mentioned_usernames


@pytest.mark.parametrize(
    "text, expected",
    [
        # The mention plugin inserts "@username&nbsp;"
        ("<p>@Alice&nbsp;thanks for the help</p>", ["Alice"]),
        ("<p>Hi @Alice&nbsp;and @Bob&nbsp;see this</p>", ["Alice", "Bob"]),
        ("<p>thanks @Alice&nbsp;</p>", ["Alice"]),
        # Plain text and punctuation
        ("hello @Alice thanks", ["Alice"]),
        ("@Alice", ["Alice"]),
        ("hi @Alice, see this", ["Alice"]),
        ("great work @Alice.", ["Alice"]),
        ("@Alice\nnext line", ["Alice"]),
        # HTML around the mention
        ("<p>@Alice</p>", ["Alice"]),
        # Usernames with dots, dashes and underscores
        ("@john.doe @jane_doe @a-b", ["john.doe", "jane_doe", "a-b"]),
        # Duplicates are returned once, in order
        ("@Alice @Bob @Alice", ["Alice", "Bob"]),
        # No mentions
        ("no mentions here", []),
        ("email me at x@", []),
        ("@ alone", []),
        ("", []),
    ],
)
def test_extract_mentioned_usernames(text, expected):
    assert extract_mentioned_usernames(text) == expected
