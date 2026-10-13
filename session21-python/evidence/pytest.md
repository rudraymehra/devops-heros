# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:17:51.517756+00:00

Working directory: session21-python/backend

```text
$ uv run --python 3.13 --with-requirements requirements-dev.txt pytest -v
Installed 62 packages in 129ms
============================= test session starts ==============================
platform darwin -- Python 3.13.9, pytest-9.1.1, pluggy-1.6.0 -- /tmp/uv-cache-devops/builds-v0/.tmpG3cWjy/bin/python
cachedir: .pytest_cache
rootdir: /Users/rudraym/devops-heros/session21-python/backend
configfile: pytest.ini
plugins: platformdirs-4.13.0, anyio-4.15.1
collecting ... collected 24 items

tests/test_api.py::test_health_and_identity PASSED                       [  4%]
tests/test_api.py::test_create_read_and_list PASSED                      [  8%]
tests/test_api.py::test_filter_by_status_category_and_location PASSED    [ 12%]
tests/test_api.py::test_resolution_and_reopening PASSED                  [ 16%]
tests/test_api.py::test_resolution_cannot_be_set_on_open_request PASSED  [ 20%]
tests/test_api.py::test_edit_records_real_activity PASSED                [ 25%]
tests/test_api.py::test_invalid_updates_do_not_change_data[body0] PASSED [ 29%]
tests/test_api.py::test_invalid_updates_do_not_change_data[body1] PASSED [ 33%]
tests/test_api.py::test_invalid_updates_do_not_change_data[body2] PASSED [ 37%]
tests/test_api.py::test_invalid_updates_do_not_change_data[body3] PASSED [ 41%]
tests/test_api.py::test_invalid_reports[title- ] PASSED                  [ 45%]
tests/test_api.py::test_invalid_reports[location-] PASSED                [ 50%]
tests/test_api.py::test_invalid_reports[reporter-] PASSED                [ 54%]
tests/test_api.py::test_invalid_reports[category-UNKNOWN] PASSED         [ 58%]
tests/test_api.py::test_invalid_reports[urgency-HIGH] PASSED             [ 62%]
tests/test_api.py::test_whitespace_trimmed PASSED                        [ 66%]
tests/test_api.py::test_delete_removes_related_activity PASSED           [ 70%]
tests/test_api.py::test_missing_request[get] PASSED                      [ 75%]
tests/test_api.py::test_missing_request[put] PASSED                      [ 79%]
tests/test_api.py::test_missing_request[delete] PASSED                   [ 83%]
tests/test_api.py::test_stats PASSED                                     [ 87%]
tests/test_api.py::test_readiness_failure_keeps_liveness PASSED          [ 91%]
tests/test_api.py::test_metrics_include_requests PASSED                  [ 95%]
tests/test_api.py::test_activity_limit PASSED                            [100%]

=============================== warnings summary ===============================
../../../../../tmp/uv-cache-devops/archive-v0/erbkfAqAq9npGScG/lib/python3.13/site-packages/fastapi/testclient.py:1
  /tmp/uv-cache-devops/archive-v0/erbkfAqAq9npGScG/lib/python3.13/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 24 passed, 1 warning in 4.59s =========================

```

Exit code: 0
