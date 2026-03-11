def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert expected_activity in data
    assert expected_fields.issubset(data[expected_activity].keys())
