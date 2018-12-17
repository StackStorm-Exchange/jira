from lib.base import BaseJiraAction
from lib.formatters import to_comment_dict

__all__ = [
    'CommentJiraIssueAction'
]


class CommentJiraIssueAction(BaseJiraAction):

    def run(self, issue_key, comment_text, config_profile=None):

        super(CommentJiraIssueAction, self)._run(config_profile)

        comment = self._client.add_comment(issue_key, comment_text)
        result = to_comment_dict(comment)
        return result
