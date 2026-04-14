from __future__ import annotations

import warnings

import pytest

from hiddenlayer.lib._beta import BetaWarning, warn_beta, check_beta_endpoint
from hiddenlayer.lib._beta_endpoints import BETA_ENDPOINTS

_beta_entries = list(BETA_ENDPOINTS.items())
_has_entries = len(_beta_entries) > 0


class TestWarnBeta:
    def test_emits_warning_on_call(self) -> None:
        with pytest.warns(BetaWarning, match=r"\[BETA\] Foo\.firstCall"):
            warn_beta("Foo.firstCall")

    def test_warning_message_format(self) -> None:
        with pytest.warns(BetaWarning) as record:
            warn_beta("Bar.analyze")

        assert len(record) == 1
        assert "[BETA] Bar.analyze" in str(record[0].message)
        assert "not GA or Production ready" in str(record[0].message)
        assert "Breaking changes may occur" in str(record[0].message)

    def test_warning_category_is_beta(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            warn_beta("Baz.create")

        assert len(caught) == 1
        assert issubclass(caught[0].category, BetaWarning)
        assert issubclass(caught[0].category, UserWarning)


class TestCheckBetaEndpoint:
    @pytest.mark.skipif(not _has_entries, reason="no beta endpoints registered")
    def test_known_beta_url_fires_warning(self) -> None:
        known_path, known_name = _beta_entries[0]
        escaped = known_name.replace(".", r"\.")
        with pytest.warns(BetaWarning, match=rf"\[BETA\] {escaped}"):
            check_beta_endpoint(known_path)

    def test_non_beta_url_no_warning(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            check_beta_endpoint("/models/v2/scan")

        beta_warnings = [w for w in caught if issubclass(w.category, BetaWarning)]
        assert len(beta_warnings) == 0

    @pytest.mark.skipif(not _has_entries, reason="no beta endpoints registered")
    def test_warning_category_is_beta_warning(self) -> None:
        known_path, _ = _beta_entries[0]
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            check_beta_endpoint(known_path)

        assert len(caught) == 1
        assert issubclass(caught[0].category, BetaWarning)
