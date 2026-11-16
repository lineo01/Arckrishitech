from app import kb

def test_retrieves_nepal_local_pest_knowledge():
    r = kb.search("How can I manage aphids using local plants?")
    assert r["matched"] is True
    assert r["title"] == "Titepati (Artemisia) as a traditional pest-management plant"
    assert r["sources"] and r["sources"][0]["geographic_scope"].startswith("Khumbu")


def test_retrieves_nepal_compost_knowledge():
    r = kb.search("How can I improve soil fertility with compost and leaves?")
    assert r["matched"] is True
    assert "compost" in r["title"].lower() or "manure" in r["title"].lower()


def test_unknown_question_does_not_invent_advice():
    r = kb.search("How do I grow dragon fruit in a hydroponic greenhouse?")
    assert r["matched"] is False
    assert "could not find" in r["answer"].lower()
