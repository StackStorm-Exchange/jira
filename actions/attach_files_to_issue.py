from lib.base import BaseJiraAction

__all__ = [
    'AttachFilesToJiraIssueAction'
]


class AttachFilesToJiraIssueAction(BaseJiraAction):

    def run(self, issue_key, file_paths,config_profile=None):
        result = []

        if config_profile:
            self._client = self._get_client(config_profile)

        for file_path in file_paths:
            with open(file_path, 'rb') as fp:
                attachment = self._client.add_attachment(
                    issue=issue_key,
                    attachment=fp,
                    filename=None)

            item = {
                "issue": issue_key,
                "filename": attachment.filename,
                "size": attachment.size,
                "created_at": attachment.created
            }
            result.append(item)

        return result
