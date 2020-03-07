import pytest
from pytest import param as p

from anglicize import anglicize, build_mapping


@pytest.mark.parametrize(
    "text, expected",
    [
        p("Abc 123", "Abc 123", id="noop"),
        p("ĂaÂâÎîȘșȚț", "AaAaIiSsTt", id="romanian"),
        p("ĄąĆćĘęŁłŃńŹźŻż", "AaCcEeLlNnZzZz", id="polish"),
        p("ÁáÉéÍíÓóÖöŐőÚúÜüŰű", "AaEeIiOoOoOoUuUuUu", id="hungarian"),
        p("ÀàÆæÇçÊêËëÈèÉéÏïÔôŒœÙùÛûŸÿ", "AaAaCcEeEeEeEeIiOoOoUuUuYy", id="french"),
        p("ÁáÉéÍíÓóÑñÚúÝý", "AaEeIiOoNnUuYy", id="spanish"),
        p("ÁáÂâÃãÀàÇçÉéÊêÍíÓóÔôÕõÚú", "AaAaAaAaCcEeEeIiOoOoOoUu", id="portuguese"),
        # Don't be fooled by the similarities, these four swear they speak diferent languages:
        p("ĆćČčĐđŠšŽž", "CcCcDdSsZz", id="bosnian-croatian-montenegrin-serbian"),
        p("ÇçËë", "CcEe", id="albanian"),
        p("ßÄäÖöÜü", "sAaOoUu", id="german"),
        p("Ĳĳ", "Ii", id="dutch"),
        p("Ëë", "Ee", id="luxembourgish"),
        p("ÐðÉéÓóÚúÝýÞþÆæÖö", "DdEeOoUuYyPpAaOo", id="icelandic"),
        p("ÆæÅåØøÉéÈèÊêÓóÒòÂâÔô", "AaAaOoEeEeEeOoOoAaOo", id="norwegian"),
        p("ÅåÄäÖö", "AaAaOo", id="swedish"),
        p("ÅåÄäÖöŠšŽž", "AaAaOoSsZz", id="finnish"),
        p("ŠšŽžÄäÖöÜü", "SsZzAaOoUu", id="estonian"),
        p("ĀāČčĒēĢģĪīĶķĻļŅņŠšŪūŽž", "AaCcEeGgIiKkLlNnSsUuZz", id="latvian"),
        p("ĄąČčĖėĘęĮįŠšŲųŪū", "AaCcEeEeIiSsUuUu", id="lithuanian"),
        p("ÇçŞşĞğIıİiÖöÜü", "CcSsGgIiIiOoUu", id="turkish"),
        p("ÄäƏəÇçĞğIıİiKkÖöŞşÜü", "AaAaCcGgIiIiKkOoSsUu", id="azerbaijani"),
        p("ÄäÇçĞğIıIiÍíÑñÖöŞşÜü", "AaCcGgIiIiIiNnOoSsUu", id="tatar"),
        p("ÇçÄäŇňÖöŞşÜüÝýŽž", "CcAaNnOoSsUuYyZz", id="turkmen"),
        p("ÄäÇçÊêIıİiÖöŞşŢţÜü", "AaCcEeIiIiOoSsTtUu", id="gagauz"),
        p("ǍǎČčŠšŽž", "AaCcSsZz", id="bulgarian-transliteration"),
        p("ᵻᶧ", "Ii", id="misc"),
    ],
)
def test_anglicize(text, expected):
    assert anglicize(text) == expected


@pytest.mark.parametrize(
    "mapping, expected",
    [
        (
            {"A": "ĂÂ", "T": "Ț", "S": "Șß"},
            {
                "ă": "a",
                "â": "a",
                "ș": "s",
                "ț": "t",
                "Ă": "A",
                "Â": "A",
                "Ș": "S",
                "Ț": "T",
                "ß": "s",
            },
        ),
    ],
)
def test_build_mapping(mapping, expected):
    assert build_mapping(mapping) == expected
