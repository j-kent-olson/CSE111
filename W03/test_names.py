import pytest
from names import make_full_name, extract_family_name, extract_given_name

def test_make_full_name():
    assert(make_full_name("Aaa", "Bbb") == "Bbb; Aaa")
    assert(make_full_name("Abcdefghijklmnopqrstuvwxyz", "12345678910") == "12345678910; Abcdefghijklmnopqrstuvwxyz")
    assert(make_full_name("345rty67uijhgvfgty7uy6tredf", "kiuytgfvbhu765redcfr4ewsxcvghyu7ytgh") == "kiuytgfvbhu765redcfr4ewsxcvghyu7ytgh; 345rty67uijhgvfgty7uy6tredf")
    assert(make_full_name("Jack-Joe", "Billy-Bob") == "Billy-Bob; Jack-Joe")

def test_extract_family_name():
    assert(extract_family_name("Bbb; Aaa") == "Bbb")
    assert(extract_family_name("12345678910; Abcdefghijklmnopqrstuvwxyz") == "12345678910")
    assert(extract_family_name("kiuytgfvbhu765redcfr4ewsxcvghyu7ytgh; 345rty67uijhgvfgty7uy6tredf") == "kiuytgfvbhu765redcfr4ewsxcvghyu7ytgh")
    assert(extract_family_name("Billy-Bob; Jack-Joe") == "Billy-Bob")

def test_extract_given_name():
    assert(extract_given_name("Bbb; Aaa") == "Aaa")
    assert(extract_given_name("12345678910; Abcdefghijklmnopqrstuvwxyz") == "Abcdefghijklmnopqrstuvwxyz")
    assert(extract_given_name("kiuytgfvbhu765redcfr4ewsxcvghyu7ytgh; 345rty67uijhgvfgty7uy6tredf") == "345rty67uijhgvfgty7uy6tredf")
    assert(extract_given_name("Billy-Bob; Jack-Joe") == "Jack-Joe")

pytest.main(["-v", "--tb=line", "-rN", __file__])