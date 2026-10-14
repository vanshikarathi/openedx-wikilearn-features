"""
Helpers for finding @username mentions in discussion posts.

Kept free of LMS imports so it can be unit tested on its own.
"""
import html
import re

# A username ends at whitespace (including the non-breaking space the mention
# plugin inserts after a username), at '@', at HTML brackets, or at punctuation.
MENTION_RE = re.compile(r"@([^\s@<>,;:!?()\[\]{}\"'/\\]+)")


def extract_mentioned_usernames(text):
    """
    Return the unique usernames mentioned in ``text``, in order of appearance.
    """
    usernames = []
    for match in MENTION_RE.findall(html.unescape(text)):
        username = match.rstrip(".")
        if username and username not in usernames:
            usernames.append(username)
    return usernames
