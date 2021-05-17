from hackernews import get_comment_from_api
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
BODY = """{"by":"norvig","id":2921983,"kids":[2922097,2922429,2924562,2922709,2922573,2922140,2922141],"parent":2921506,"text":"Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?","time":1314211127,"type":"comment"}"""


def test_response_text():
    comment = get_comment_from_api(COMMENT_ID)
    assert comment == BODY