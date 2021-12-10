import pytest
import app


@pytest.fixture
def app():
    yield app


@pytest.fixture
def client():
    return app.get_census_income()
