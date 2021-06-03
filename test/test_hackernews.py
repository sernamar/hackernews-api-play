from hackernews import get_item_from_api, get_item_from_db, save_item_to_db
import datetime
import psycopg2
from unittest import mock

# next expressions needed to be able to import the GET_DATA module
import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


# comment's id and body, to test the GET_COMMENT function
COMMENT_ID = 2921983
ITEM_FROM_API = {"by": "norvig", "id": 2921983, "kids": [2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141], "parent": 2921506,
                 "text": "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?", "time": 1314211127, "type": "comment"}
ITEM_FROM_DB = (1,
                'norvig',
                2921983,
                [2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141],
                2921506,
                "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?",
                datetime.datetime(2011, 8, 24, 20, 38, 47,
                                  tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=120, name=None)),
                'comment')


def test_get_item_from_api():
    item = get_item_from_api(COMMENT_ID)
    assert item == ITEM_FROM_API


@mock.patch("psycopg2.connect")
def test_get_item_from_db(mock_connect):
    # mock the result of psycopg2.connect(DATABASE_URL)
    mock_connection = mock_connect.return_value
    # mock the result of connection.cursor()
    mock_cursor = mock_connection.cursor.return_value
    # mock the result of cursor.fetchone()
    mock_cursor.fetchone.return_value = ITEM_FROM_DB

    item = get_item_from_db(COMMENT_ID)
    assert item == ITEM_FROM_DB


@mock.patch("psycopg2.connect")
def test_save_item_to_db(mock_connect):
    # mock the result of psycopg2.connect(DATABASE_URL)
    mock_connection = mock_connect.return_value
    # mock the result of connection.cursor()
    mock_cursor = mock_connection.cursor.return_value
    # mock the value of rowcount (which the function returns when successful)
    mock_cursor.rowcount = 1

    rowcount = save_item_to_db(COMMENT_ID)
    assert rowcount == 1
