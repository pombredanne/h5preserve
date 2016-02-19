import pytest

from h5preserve import open as hp_open, H5PreserveFile

@pytest.mark.roundtrip
def test_roundtrip(tmpdir, obj_registry):
    tmpfile = str(tmpdir.join("test_roundtrip.h5"))
    with hp_open(tmpfile, registries=obj_registry["registries"]) as f:
        f["first"] = obj_registry["dumpable_object"]

    with hp_open(tmpfile, registries=obj_registry["registries"]) as f:
        assert f["first"] == obj_registry["dumpable_object"]

@pytest.mark.roundtrip
def test_roundtrip_without_open(tmpdir, obj_registry):
    tmpfile = str(tmpdir.join("test_roundtrip.h5"))
    with H5PreserveFile(tmpfile, registries=obj_registry["registries"]) as f:
        f["first"] = obj_registry["dumpable_object"]

    with H5PreserveFile(tmpfile, registries=obj_registry["registries"]) as f:
        assert f["first"] == obj_registry["dumpable_object"]

@pytest.mark.roundtrip
def test_roundtrip_with_defaults(tmpdir, obj_registry_with_defaults):
    obj_registry = obj_registry_with_defaults
    tmpfile = str(tmpdir.join("test_roundtrip.h5"))
    with hp_open(tmpfile, registries=obj_registry["registries"]) as f:
        f["first"] = obj_registry["dumpable_object"]

    with hp_open(tmpfile, registries=obj_registry["registries"]) as f:
        assert f["first"] == obj_registry["dumpable_object"]

@pytest.mark.roundtrip
def test_roundtrip_without_open_with_defaults(tmpdir, obj_registry_with_defaults):
    obj_registry = obj_registry_with_defaults
    tmpfile = str(tmpdir.join("test_roundtrip.h5"))
    with H5PreserveFile(tmpfile, registries=obj_registry["registries"]) as f:
        f["first"] = obj_registry["dumpable_object"]

    with H5PreserveFile(tmpfile, registries=obj_registry["registries"]) as f:
        assert f["first"] == obj_registry["dumpable_object"]
