import logging

from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .red_team_session import RedTeamSessionsResource, AsyncRedTeamSessionsResource

logger = logging.getLogger(__name__)

class EvaluationSessionsResource(SyncAPIResource):
    @cached_property
    def red_team(self) -> RedTeamSessionsResource:
        return RedTeamSessionsResource(client=self._client)


class AsyncEvaluationSessionsResource(AsyncAPIResource):
    @cached_property
    def red_team(self) -> AsyncRedTeamSessionsResource:
        return AsyncRedTeamSessionsResource(client=self._client)
