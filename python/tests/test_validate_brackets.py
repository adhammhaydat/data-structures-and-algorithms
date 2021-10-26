from linked_list.stack_queue_brackets import validate_brackets

def test_validat_true():
    excepted=True

    actual=validate_brackets("{}{Code}[Fellows](())")
    assert actual==excepted
    
