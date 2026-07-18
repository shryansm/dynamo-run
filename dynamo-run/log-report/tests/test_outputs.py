from pathlib import Path
import json


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"


def test_report_is_valid():
    """The report file has valid data"""
    with open("/app/report.json") as file:
        data = json.load(file)
        assert "total_requests" in data
        assert "unique_ips" in data
        assert "top_path" in data

def test_report_is_correct():
    """The report data is accurate"""
    with open("/app/report.json") as file:
        data = json.load(file)
        assert data["total_requests"] == 6
        assert data["unique_ips"] == 3
        assert data["top_path"] == "/index.html"