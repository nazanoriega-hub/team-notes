import pytest
from notes import add_note, list_notes, delete_note

@pytest.fixture(autouse=True)
def clear_notes():
    from notes import notes
    notes.clear()

def test_add_note():
    result = add_note("Primera nota")
    assert result == "Primera nota"
    assert "Primera nota" in list_notes()

def test_list_notes():
    add_note("Nota 1")
    add_note("Nota 2")
    assert list_notes() == ["Nota 1", "Nota 2"]

def test_delete_note_exists():
    add_note("Eliminar esta")
    assert delete_note("Eliminar esta") is True
    assert "Eliminar esta" not in list_notes()

def test_delete_note_not_exists():
    add_note("Nota existente")
    assert delete_note("Inexistente") is False
    assert list_notes() == ["Nota existente"]
