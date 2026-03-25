from __future__ import annotations

import warnings

import pytest

from hiddenlayer.lib._beta import BetaWarning, warn_beta


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
