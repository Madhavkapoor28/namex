from namex.services.name_request.auto_analyse import AnalysisIssueCodes

# Import DTOs
from .abstract import AnalysisResponseIssue
from ..response_objects import NameAnalysisIssue


class CheckIsValid(AnalysisResponseIssue):
    issue_type = AnalysisIssueCodes.CHECK_IS_VALID
    status_text = "Approved"
    issue = None

    def create_issue(self, procedure_result):
        issue = NameAnalysisIssue(
            issue_type=self.issue_type,
            line1=None,
            line2=None,
            consenting_body=None,
            designations=None,
            show_reserve_button=None,
            show_examination_button=None,
            conflicts=None,
            setup=None,
            name_actions=None
        )

        return issue