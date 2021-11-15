from context import action

class Test_basic_action:

    def test_init(self):
        act = action.Action('N', (-1, 0), 0)

        assert act.name == 'N'
        assert act.effect == (-1, 0)
        assert act.step == 0

    def test_get_effect_move(self):
        map = [[2378, 2378, 2378],
            [2378, 2378, 2378],
            [2378, 2378, 2378]]
        loc = (1,1)
        act = action.Action('N', (-1, 0), 0)

        assert act.get_effect(loc, map) == (0,1)

    def test_get_effect_blocked_top(self):
        map = [[2378, 2378, 2378],
            [2378, 2378, 2378],
            [2378, 2378, 2378]]
        loc = (0,1)
        act = action.Action('N', (-1, 0), 0)

        assert act.get_effect(loc, map) == (0,1)

    def test_get_effect_blocked_bottom(self):
        map = [[2378, 2378, 2378],
            [2378, 2378, 2378],
            [2378, 2378, 2378]]
        loc = (2,1)
        act = action.Action('S', (1, 0), 0)

        assert act.get_effect(loc, map) == (2,1)

