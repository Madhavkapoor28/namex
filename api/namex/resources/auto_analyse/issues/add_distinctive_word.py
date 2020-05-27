from string import Template

from namex.services.name_request.auto_analyse import AnalysisIssueCodes

# Import DTOs
from .abstract import AnalysisResponseIssue
from ..response_objects import NameAnalysisIssue
from ..response_objects import NameAction, NameActions, WordPositions


class AddDistinctiveWordIssue(AnalysisResponseIssue):
    issue_type = AnalysisIssueCodes.ADD_DISTINCTIVE_WORD
    status_text = "Further Action Required"
    issue = None

    def create_issue(self, procedure_result):
        issue = NameAnalysisIssue(
            issue_type=self.issue_type,
            line1="Requires a word at the beginning of your name that sets it apart.",
            line2=None,
            consenting_body=None,
            designations=None,
            show_reserve_button=False,
            show_examination_button=False,
            conflicts=None,
            setup=None,
            name_actions=[]
        )

        list_name = self._lc_list_items(self.analysis_response.name_tokens)

        issue.name_actions = [
            NameAction(
                type=NameActions.BRACKETS,
                position=WordPositions.START,
                message="Add a Word Here",
                word=list_name[0] if list_name.__len__() > 0 else None,
                index=0
            )
        ]

        # Setup boxes
        issue.setup = self.setup_config
        for setup_item in issue.setup:
            # Loop over properties
            for prop in vars(setup_item):
                if isinstance(setup_item.__dict__[prop], Template):
                    # Render the Template string, replacing placeholder vars
                    setattr(setup_item, prop, setup_item.__dict__[prop].safe_substitute([]))

        return issue