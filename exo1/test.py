# coding: utf-8

from json_to_one_level import json_to_one_level

def test_json_to_one_level_case_1():
    ret = json_to_one_level({
        u"name": {
            u"firstname": u"test"
        }
    })
    assert ret[u"name.firstname"] == u"test"

def test_json_to_one_level_case_2():
    ret = json_to_one_level({
        u'googleGroup.id': 1,
        u'metadata': {
            u'path': u'primaryEmail',
            u'id': 225.0
        }
    })
    assert u"googleGroup.id" in ret
    assert u"metadata.path" in ret
    assert u"metadata.id" in ret

def test_json_to_one_level_case_3():

    ret = json_to_one_level({
        u"names": [
            u"kevin",
            u"alexis",
            u"nicolas"
        ]
    })
    assert ret[u"names.0"] == u"kevin"
    assert ret[u"names.1"] == u"alexis"
    assert ret[u"names.2"] == u"nicolas"

def test_json_to_one_level_case_4():
    ret = json_to_one_level({
        u"names": [
            {u"value": u"kevin"},
            {u"value": u"alexis"},
            {u"value": u"nicolas"}
        ]
    })
    assert ret[u"names.0.value"] == u"kevin"
    assert ret[u"names.1.value"] == u"alexis"
    assert ret[u"names.2.value"] == u"nicolas"

